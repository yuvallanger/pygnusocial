"""Global constants for tests."""
from os.path import dirname, abspath
CURDIR = dirname(abspath(__file__)) + '/'
SERVER_URL = 'http://127.0.0.1:5000'
RESPONSE_STRING = 'Hello world!'
USERNAME = 'admin'
PASSWORD = 'secret'
ERROR_STRING = 'Error string'
ERROR_DICT = {'error': ERROR_STRING}
