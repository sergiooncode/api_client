import unittest
from util import validations


class ValidationsTest(unittest.TestCase):
    def test_no_valid_scheme(self):
        url = 'no_valid_url'

        self.assertRaises(Exception, lambda: validations.validate_url(url))

    def test_no_valid_network_locator(self):
        url = 'http://'

        self.assertRaises(Exception, lambda: validations.validate_url(url))

    def test_no_valid_income(self):
        income = 'afgf'

        self.assertRaises(Exception, lambda: validations.validate_income(income))

    def test_no_valid_zipcode(self):
        zipcode = '64gyt'

        self.assertRaises(Exception, lambda: validations.validate_zipcode(zipcode))

    def test_no_valid_age(self):
        age = 'yt'

        self.assertRaises(Exception, lambda: validations.validate_age(age))
