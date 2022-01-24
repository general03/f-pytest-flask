
def test_homepage(create_app):
    with create_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Hello" in response.data