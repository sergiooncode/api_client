import unittest
import run


class RunTest(unittest.TestCase):
    def test_set_defaults_when_no_args_given(self):
        args = {'endpoint': None,
                'income': None,
                'zipcode': None,
                'age': None}

        options = run.set_query_defaults(args)

        self.assertEqual('http://not_real.com/customer_scoring', options['endpoint'])
        self.assertEqual('50000', options['income'])
        self.assertEqual('60201', options['zipcode'])
        self.assertEqual('35', options['age'])

    def test_set_defaults_when_all_arg_given(self):
        args = {'endpoint': 'http://example.com/test',
                'income': '60000',
                'zipcode': '60606',
                'age': '27'}

        options = run.set_query_defaults(args)

        self.assertEqual('http://example.com/test', options['endpoint'])
        self.assertEqual('60000', options['income'])
        self.assertEqual('60606', options['zipcode'])
        self.assertEqual('27', options['age'])

    def test_set_defaults_when_only_endpoint_arg_given(self):
        args = {'endpoint': 'http://example.com/test',
                'income': None,
                'zipcode': None,
                'age': None}

        options = run.set_query_defaults(args)

        self.assertEqual('http://example.com/test', options['endpoint'])
        self.assertEqual('50000', options['income'])
        self.assertEqual('60201', options['zipcode'])
        self.assertEqual('35', options['age'])

    def test_set_defaults_when_only_income_arg_given(self):
        args = {'endpoint': None,
                'income': '60000',
                'zipcode': None,
                'age': None}

        options = run.set_query_defaults(args)

        self.assertEqual('http://not_real.com/customer_scoring', options['endpoint'])
        self.assertEqual('60000', options['income'])
        self.assertEqual('60201', options['zipcode'])
        self.assertEqual('35', options['age'])

    def test_set_defaults_when_only_zipcode_arg_given(self):
        args = {'endpoint': None,
                'income': None,
                'zipcode': '60606',
                'age': None}

        options = run.set_query_defaults(args)

        self.assertEqual('http://not_real.com/customer_scoring', options['endpoint'])
        self.assertEqual('50000', options['income'])
        self.assertEqual('60606', options['zipcode'])
        self.assertEqual('35', options['age'])

    def test_set_defaults_when_only_age_arg_given(self):
        args = {'endpoint': None,
                'income': None,
                'zipcode': None,
                'age': '27'}

        options = run.set_query_defaults(args)

        self.assertEqual('http://not_real.com/customer_scoring', options['endpoint'])
        self.assertEqual('50000', options['income'])
        self.assertEqual('60201', options['zipcode'])
        self.assertEqual('27', options['age'])
