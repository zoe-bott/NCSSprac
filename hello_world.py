from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/lol', methods = ['GET', 'POST'])
def lol():
    text = request.values.get('text').lower()
    response = "I don't understand, sorry"

    if text == 'hello' or text == 'hi' or text == 'hey':
        response = 'Hi there, nice to meet you!'

    return jsonify({
        'response_type': 'in_channel',
        'text': f'{response}',
    })

@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
  return jsonify({
    'version': '0.1',
    'response': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': 'Hello, welcome to my bot, the zobot!'
      }
    }
  })



if __name__ == '__main__':
    app.run()