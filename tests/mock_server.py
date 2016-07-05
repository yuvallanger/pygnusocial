from functools import wraps
from flask import Flask, jsonify
from flask import request
APP = Flask(__name__)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'


def requires_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({'error': 'Invalid credentials.'})
        return func(*args, **kwargs)
    return decorated


@APP.route('/api/help/test.json')
def help_test():
    return jsonify('ok')


@APP.route('/api/get<ext>')
def get(ext: str):
    return jsonify('Hello world!')


@APP.route('/api/account/verify_credentials.json')
@requires_auth
def verify_credentials():
    return jsonify('ok')


APP.run()
