import pytest
from typing import Dict

@pytest.fixture
def fixture_key_value() -> Dict[str, str]:
    return {
        "key": "mock_key",
        "value": "mock_key",
    }
