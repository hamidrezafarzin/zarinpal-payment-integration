import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "zarinpal-payment-integration",
    version = "0.0.1",
    author = "Hamidreza Farzin",
    author_email = "hamidfarzin1382@gmail.com",
    description = "This Python package provides a simple interface for interacting with the ZarinPal payment gateway. It allows you to make payment requests, verify payments, and handle errors gracefully.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/hamidrezafarzin/zarinpal-payment-integration",
    project_urls = {
        "Author": "https://github.com/hamidrezafarzin",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'requests',
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.7"
)