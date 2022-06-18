from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Amo Karina Cardoso FML</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)