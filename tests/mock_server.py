from functools import wraps
from flask import Flask, jsonify
from flask import request, Response
APP = Flask(__name__)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


def requires_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return func(*args, **kwargs)
    return decorated


@APP.route('/api/help/test.json')
def help_test():
    return jsonify('ok')


@APP.route('/api/get<ext>')
def get(ext: str):
    return jsonify('Hello world!')


APP.run()
