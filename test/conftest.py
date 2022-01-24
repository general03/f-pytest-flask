import pytest
from app import app

@pytest.fixture
def create_app():
    return app