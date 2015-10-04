#!/usr/bin/env python
import configargparse
from apiclient.scoring import get_consumer_scoring
from util.validations import validate_zipcode, validate_income, validate_url, validate_age


DEFAULT_ENDPOINT = 'http://not_real.com/customer_scoring'
DEFAULT_INCOME = '50000'
DEFAULT_ZIPCODE = '60201'
DEFAULT_AGE = '35'
PROPENSITY_MODIFIER = 2
RESULT_LINE = 'Modified propensity score:'


def parse_arguments():
    parser = configargparse.ArgParser()
    parser.add('-e', '--endpoint', required=False,
               help='Consumer scoring API endpoint against which making calls \
                (defaults to http://not_real.com/customer_scoring)')
    parser.add('-i', '--income', required=False,
               help='Consumer\'s income whose scoring we want to get (defaults to 50000)')
    parser.add('-z', '--zipcode', required=False,
               help='Consumer\'s zipcode whose scoring we want to get (defaults to 60201)')
    parser.add('-a', '--age', required=False, help='Consumer\'s age whose scoring we want to get (defaults to 35)')
    args = vars(parser.parse_args())
    return args


def set_query_defaults(args):
    options = {'endpoint': args['endpoint'] if args['endpoint'] else DEFAULT_ENDPOINT,
               'income': args['income'] if args['income'] else DEFAULT_INCOME,
               'zipcode': args['zipcode'] if args['zipcode'] else DEFAULT_ZIPCODE,
               'age': args['age'] if args['age'] else DEFAULT_AGE}
    return options


def validate_arguments(args):
    validate_url(args['endpoint'])
    validate_income(args['income'])
    validate_zipcode(args['zipcode'])
    validate_age(args['age'])


def modify_propensity(orig_prop):
    return orig_prop + PROPENSITY_MODIFIER


def main():
    args = parse_arguments()
    validate_arguments(args)
    options = set_query_defaults(args)
    result = get_consumer_scoring(options['endpoint'],
                                  options['income'],
                                  options['zipcode'],
                                  options['age'])
    print(RESULT_LINE)
    print(str(modify_propensity(result['propensity'])))


if __name__ == '__main__':
    main()
