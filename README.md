# ZarinPal Payment Python Client

A Python client for integrating ZarinPal payment gateway into your Python applications.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Error Handling](#error-handling)
- [License](#license)

## Introduction

This Python package provides a simple interface for interacting with the ZarinPal payment gateway. It allows you to make payment requests, verify payments, and handle errors gracefully.

## Features

- Request payments with ease
- Verify payment transactions
- Graceful error handling for ZarinPal-specific errors
- ...

## Installation

You can install the package using pip:

```bash
pip install zarinpal-payment-integration
```

## Usage

```python 
from zarinpal.api import ZarinPalPayment

# Initialize ZarinPalPayment with your merchant_id and amount
payment_instance = ZarinPalPayment("your_merchant_id", 10000)

# Make a payment request
result = payment_instance.request_payment("your_callback_url", "Payment for something", "user_mobile", "user_email")
print(result)

# Verify a payment
verification_result = payment_instance.verify_payment("payment_authority")
print(verification_result)
```
## Examples
For more detailed examples, check the [examples](https://github.com/hamidrezafarzin/zarinpal-payment-integration/tree/main/examples) directory in this repository.

## Error Handling
The package includes robust error handling for ZarinPal-specific errors. For more information on error codes and messages, refer to the [ZarinPal API documentation](https://www.zarinpal.com/docs/paymentGateway/errorList.html).

## License
This project is licensed under the MIT License.
