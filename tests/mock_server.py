#!/usr/bin/env python3
'Dummy server for pygnusocial tests.'
from functools import wraps
from flask import Flask, jsonify
from flask import request, Response
from conftest import RESPONSE_STRING, USERNAME, PASSWORD, CURDIR
APP = Flask(__name__)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == USERNAME and password == PASSWORD


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


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
    return jsonify(RESPONSE_STRING)


@APP.route('/api/get_auth<ext>')
@requires_auth
def get_auth(ext: str):
    return jsonify(RESPONSE_STRING)


@APP.route('/api/account/verify_credentials.json')
@requires_auth
def verify_credentials():
    return jsonify('ok')


@APP.route('/api/post.json', methods=['POST'])
@requires_auth
def post():
    return jsonify(RESPONSE_STRING)


@APP.route('/api/statusnet/config.json')
def config():
    with open(CURDIR + 'config.json') as f:
        data = f.readline()
        return data


APP.run()
