# Import the flask library
from flask import Flask, request, jsonify

import ujson

# Create your web server
app = Flask(__name__)

# When people visit the home page '/'
@app.route('/')
def index():
  return 'Hello! I echo things back.'


# When we receive a request from Alexa
@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
  data = request.get_json()
  request_type = data['request']['type']
  if request_type == 'IntentRequest':
    query = data['request']['intent']['slots']['query']['value']
    response_text = 'You said: ' + query
  else:
    response_text = 'Say something!'

  return jsonify({
    'version': '0.1',
    'response': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': response_text,
      },
      'shouldEndSession': False,  # Keep the app alive
    }
  })


if __name__ == '__main__':
  # Start the web server!
  app.run()