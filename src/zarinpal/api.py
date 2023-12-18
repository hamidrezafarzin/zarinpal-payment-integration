import requests
import logging
from error_handling import (
    ZarinPalError,
    ValidationException,
    TerminalException,
    PaymentRequestException,
    PaymentVerifyException,
    MyPaymentException,
)


class ZarinPalPayment:
    REQUEST_URL = "https://api.zarinpal.com/pg/v4/payment/request.json"
    VERIFY_URL = "https://api.zarinpal.com/pg/v4/payment/verify.json"
    START_PAYMENT_URL = "https://www.zarinpal.com/pg/StartPay/{}"
    HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}

    def __init__(self, merchant_id: str, amount: int):
        self.merchant_id = merchant_id
        self.amount = amount

    def _make_request(self, url, data):
        try:
            response = requests.post(url, json=data, headers=self.HEADERS)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.critical(e)
            raise MyPaymentException(f"Request failed: {e}")

    def _handle_zarinpal_errors(self, response_data):
        errors = response_data.get("errors", {})
        if errors:
            error_code = errors.get("code", -1)
            message = errors.get("message", "Unknown error")
            validations = errors.get("validations", [])
            if validations:
                validation_messages = [
                    validation["description"] for validation in validations
                ]
                message += f" Validations: {', '.join(validation_messages)}"

            if error_code == -9:
                raise ValidationException(error_code, message)
            elif error_code in [-10, -11, -12, -15, -16, -17]:
                raise TerminalException(error_code, message)
            elif error_code in [-30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40]:
                raise PaymentRequestException(error_code, message)
            elif error_code in [-50, -51, -52, -53, -54, 101]:
                raise PaymentVerifyException(error_code, message)
            else:
                raise ZarinPalError(error_code, message)

    def request_payment(
        self, callback_url: str, description: str, mobile: str, email: str
    ) -> dict:
        data = {
            "merchant_id": self.merchant_id,
            "amount": self.amount,
            "callback_url": callback_url,
            "description": description,
            "metadata": {
                "mobile": mobile,
                "email": email,
            },
        }
        try:
            response_data = self._make_request(self.REQUEST_URL, data)
            self._handle_zarinpal_errors(response_data)
            authority = response_data["data"]["authority"]
            payment_url = self._redirect_to_payment_gateway(authority)
            return {
                "success": True,
                "data": {"authority": authority, "payment_url": payment_url},
                "error": None,
                "response_data": response_data,
            }
        except ZarinPalError as e:
            return {
                "success": False,
                "data": None,
                "error": str(e),
                "response_data": response_data,
            }
        except MyPaymentException as e:
            return {
                "success": False,
                "data": None,
                "error": str(e),
                "response_data": response_data,
            }

    def _redirect_to_payment_gateway(self, authority: str) -> str:
        return self.START_PAYMENT_URL.format(authority)

    def verify_payment(self, authority: str) -> dict:
        data = {
            "merchant_id": self.merchant_id,
            "amount": self.amount,
            "authority": authority,
        }
        try:
            response_data = self._make_request(self.VERIFY_URL, data)
            self._handle_zarinpal_errors(response_data)
            verification_code = response_data["data"]["code"]
            if verification_code == 101:
                return {
                    "success": True,
                    "data": {"code": verification_code},
                    "error": None,
                    "response_data": response_data,
                }
        except ZarinPalError as e:
            return {
                "success": False,
                "data": None,
                "error": str(e),
                "response_data": response_data,
            }
        except MyPaymentException as e:
            return {
                "success": False,
                "data": None,
                "error": str(e),
                "response_data": response_data,
            }
