from zarinpal.api import ZarinPalPayment

merchant_id = "your_merchant_id"
amount = 1000  # replace with your desired amount
payment_handler = ZarinPalPayment(merchant_id, amount)

# Request Payment
callback_url = "https://example.com/callback"
description = "Payment for a product"
mobile = "1234567890"
email = "user@example.com"
payment_request_result = payment_handler.request_payment(callback_url, description, mobile, email)
print(payment_request_result)