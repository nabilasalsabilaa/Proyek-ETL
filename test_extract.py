import pytest
from utils.extract import extract_data

def test_extract_data():
    data, timestamp = extract_data()
    assert isinstance(data, list)
    assert isinstance(timestamp, str)
    assert len(data) > 0
    assert 'title' in data[0]