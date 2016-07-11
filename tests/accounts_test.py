"Unit tests for gnusocial.accounts module."
from functools import partial
import pytest
from gnusocial.utils import AuthenticationError
from gnusocial.accounts import verify_credentials
from conftest import SERVER_URL, USERNAME, PASSWORD


def test_verify_credentials():
    """Test function for gnusocial.accounts.verify_credentials function.
    It should raise gnusocial.utils.AuthenticationError if
    credentials are invalid.
    It should return None if everything is fine.
    """
    verify = partial(verify_credentials, SERVER_URL, USERNAME)
    assert verify(PASSWORD) is None
    with pytest.raises(AuthenticationError):
        verify(PASSWORD[:-1])
