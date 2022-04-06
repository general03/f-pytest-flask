import pytest
from pathlib import Path
from app import app

@pytest.fixture(scope="session")
def create_app():
    return app

@pytest.fixture
def clean_folder_export_html():
    for file in Path('./htmlcov').iterdir():
        file.unlink()