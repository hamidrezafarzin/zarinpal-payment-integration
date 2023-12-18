from zarinpal.api import ZarinPalPayment

merchant_id = "your_merchant_id"
amount = 1000  # replace with your desired amount
payment_handler = ZarinPalPayment(merchant_id, amount)
authority = "Your_authority_code"
verification_result = payment_handler.verify_payment(authority)
print(verification_result)
