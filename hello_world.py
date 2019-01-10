from flask import Flask, request, jsonify
import requests
import ujson

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/lol', methods = ['GET', 'POST'])
def lol():
    text = request.values.get('text').lower()
    response = "I don't understand, sorry!"

    if text == 'hello' or text == 'hi' or text == 'hey':
        response = 'Hi there, nice to meet you!'

    return jsonify({
        'response_type': 'in_channel',
        'text': f'{response}',
    })

@app.route('/trivia', methods = ['GET', 'POST'])
def trivia():
    url = "https://opentdb.com/api.php?amount=1&category=10&difficulty=easy"
    response = requests.get(url)
    question = response.json()['results'][0]['question']
    answers = response.json()['results'][0]['incorrect_answers']
    answers.append(response.json()['results'][0]['correct_answer'])
    

    return f'<h1>{question}</h1> '

@app.route('/joke', methods = ['GET', 'POST'])
def jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url).json()
    setup = response['setup']
    punchline = response['punchline']

    return f'{setup}<br>{punchline}'

@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
    data = request.get_json()

    # The request structure is deeply nested
    # We expect the requested intent to have a slot called 'Query'
    try:
        query = request.json['request']['intent']['slots']['Query']['value']
        response_text = 'You said: ' + query
    except KeyError:
        response_text = 'Did you say something?'

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
    app.run(debug=True)