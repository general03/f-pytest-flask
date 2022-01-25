import pytest

@pytest.mark.route
def test_homepage(create_app):
    with create_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Hello" in response.data

@pytest.mark.route
@pytest.mark.parametrize("param", [1, "2", -3])
def test_param_other(create_app, param):
    with create_app.test_client() as test_client:
        response = test_client.get(f"/other?page={param}")
        assert response.status_code == 200
        assert bytes(f"Page : {param}", "utf-8") in response.data
