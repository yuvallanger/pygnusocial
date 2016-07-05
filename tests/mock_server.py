from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/api/help/test.json')
def help_test():
    return jsonify('ok')


@app.route('/api/get.as')
def get_as():
    return jsonify('Hello world!')


@app.route('/api/get.json')
def get_json():
    return jsonify({'Hello': 'world'})


app.run()
