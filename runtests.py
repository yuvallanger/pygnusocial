#!/usr/bin/env python
from subprocess import Popen, run

server = Popen('./tests/mock_server.py')
return_code = run('py.test tests', shell=True).returncode
server.kill()
quit(code=return_code)
