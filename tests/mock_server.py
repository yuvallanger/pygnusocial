from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/api/help/test.json')
def help_test():
    return jsonify('ok')


app.run()
