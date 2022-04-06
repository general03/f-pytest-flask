from urllib import request
from api import get_api_url
from pathlib import Path
import pytest 

def get_api_file():
    
    return get_api_url()

def test_mocking_get_api_file(mocker):

    def mock_data_url():
        return 'http://mydomain.tld/mockdata'

    mocker.patch('test_api_call_file.get_api_url', mock_data_url)

    assert get_api_file() == mock_data_url()

def test_get_api_url_url():

    assert 'https://random-d.uk/api' in get_api_file()


@pytest.mark.usefixtures("clean_folder_export_html")
def test_clean_export_html():
    assert Path('./htmlcov/index.html').exists() == False