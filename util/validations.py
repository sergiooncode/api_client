from urlparse import urlparse
import re


def validate_url(endpoint):
    if endpoint:
        if not urlparse(endpoint).scheme:
            raise Exception('The url scheme must be provided')
        if not urlparse(endpoint).netloc:
            raise Exception('The domain and path of the url must be provided')


def validate_income(income):
    if income:
        try:
            float(income)
        except:
            raise Exception('The income value must be a numeric value')


def validate_zipcode(zipcode):
    if zipcode:
        if not re.match('^\d{5}(-\d{4})?$', zipcode):
            raise Exception('The zipcode is not in the right US format')


def validate_age(age):
    if age:
        if not age.isdigit():
            raise Exception('The age must be a numeric and integer value')
