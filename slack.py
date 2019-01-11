from flask import Flask, jsonify, request
from bot import on_enter_state, on_input
import requests

app = Flask(__name__)

state = 'SETUP'
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url).json()
setup = response['setup']
punchline = response['punchline']
context = {'setup': setup, 'punchline': punchline}

@app.route('/slack/slash', methods=['GET', 'POST'])
def slack_event():
  global state, context
  payload = request.values
  print(payload)  # Print payload for debugging.

  if payload:
    on_enter_state('SETUP', context)
    user_input = payload.get('text')
    on_input('SETUP', user_input, context)
    # todo: finish this slack interface!

if __name__ == '__main__':
  app.run()
