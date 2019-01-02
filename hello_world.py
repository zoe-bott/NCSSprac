from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/lol', methods = ['GET', 'POST'])
def lol():
    text = request.values.get('text')
    return (f'hello {text}')
    '''return jsonify({
        'response_type': 'in_channel',
        'text': f'lol {text}',
    })'''


if __name__ == '__main__':
    app.run()