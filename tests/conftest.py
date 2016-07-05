from subprocess import Popen
from time import sleep
from os.path import dirname, join


def run_server():
    return Popen(['python', join(dirname(__file__), 'mock_server.py')])


SERVER_URL = 'http://127.0.0.1:5000'
