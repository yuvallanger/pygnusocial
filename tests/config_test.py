from os.path import join
import json
from conftest import CURDIR, SERVER_URL
from gnusocial.config import config

def test_config():
    """Test function for gnusocial.config.config function.
    It should return a dict with the same contents as in config.json file.
    """
    conf = json.load(open(join(CURDIR, 'responses', 'statusnet', 'config.json')))
    assert conf == config(SERVER_URL)
