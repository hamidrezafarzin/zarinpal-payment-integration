# error_handling.py

class ZarinPalError(Exception):
    def __init__(self, code, fa_message):
        self.code = code
        self.fa_message = fa_message
        super().__init__(fa_message)

    def __str__(self):
        return f"ZarinPalError: Code {self.code} - {self.fa_message}"


class ValidationException(ZarinPalError):
    pass


class TerminalException(ZarinPalError):
    pass


class PaymentRequestException(ZarinPalError):
    pass


class PaymentVerifyException(ZarinPalError):
    pass

class MyPaymentException(Exception):
    pass
