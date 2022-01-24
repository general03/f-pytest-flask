from urllib import request
import pytest
from api import get_api_url

def get_api_file():
    
    return get_api_url()

def test_mocking_get_api_file(mocker):

    def mock_data_url():
        return 'http://mydomain.tld/mockdata'

    mocker.patch('test_api_call_file.get_api_url', mock_data_url)

    assert get_api_file() == mock_data_url()

def test_get_api_url_url():

    assert 'https://random-d.uk/api' in get_api_file()