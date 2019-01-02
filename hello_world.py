from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!!!'

@app.route('/lol')
def lol():
    text = request.values.get('text')
    return f'lol {text}'

if __name__ == '__main__':
    app.run()