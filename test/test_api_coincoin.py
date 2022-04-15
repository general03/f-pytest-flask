import pytest 

def get_app_url(create_app):
    with create_app.test_client() as test_client:
        return test_client.get('/coincoin')

@pytest.mark.coincoin
def test_mocking_get_api_endpoint(mocker):

    def mock_data_url():
        return '<img src="domain.tld/image.png" />'

    mocker.patch('test_api_coincoin.get_app_url', mock_data_url)

    assert get_app_url() == mock_data_url()
