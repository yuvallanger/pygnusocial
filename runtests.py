#!/usr/bin/env python
from subprocess import Popen, run

server = Popen('./tests/mock_server.py')
run('py.test tests', shell=True)
server.kill()
