import os
import pytest
import tempfile
from pathlib import Path

@pytest.fixture
def temp_recording_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname

@pytest.fixture
def mock_window_title():
    return "Test Window"
