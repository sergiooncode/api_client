from mock import Mock, patch
from nose.tools import raises, assert_raises
import json
from requests.exceptions import HTTPError
from apiclient import scoring


@patch('apiclient.scoring.requests.get')
def test_get_consumer_scoring_200(mock_get):
    expected_string = '{"ping": "pong"}'
    mock_response = Mock(status=200, return_value=expected_string)
    expected_json = json.loads(expected_string)
    print(expected_json)
    endpoint = 'http://example.com'
    income = '100'
    zipcode = '60606'
    age = '23'

    mock_get.return_value = mock_response

    result = scoring.get_consumer_scoring(endpoint, income, zipcode, age)

    assert result
    assert mock_response.json.called
    assert mock_get.called


@patch('apiclient.scoring.requests.get')
@raises(HTTPError)
def test_get_consumer_scoring_404(mock_get):
    mock_response = Mock(status=404)
    mock_get.side_effect = HTTPError(mock_response, 'not found')
    endpoint = 'http://example.com'
    income = '100'
    zipcode = '60614'
    age = '23'

    scoring.get_consumer_scoring(endpoint, income, zipcode, age)

    assert mock_get.called
    assert_raises(HTTPError)
