from flaskapp import app 
from flask import request 
from bot2 import on_enter_state, on_input

state = 'NO QUERY'
data = {}


@app.route('/reminder', methods=['GET'])
def slack_ask():
    global state, data
    output = ""
    
    input_text = request.values['question']
    if input_text:
        state, data, output_on_input = on_input(state, input_text, data)
    else:
        output_on_enter = on_enter_state(state, data)

    if output_on_enter:
        output += output_on_enter

    return output

if __name__ == '__main__':
    app.run(debug=True)