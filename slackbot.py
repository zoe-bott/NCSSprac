from flask import request, Flask, jsonify
from bot2 import on_enter_state, on_input


app = Flask(__name__)
state = 'NO QUERY'
data = {}


@app.route('/reminder', methods=['GET'])
def slack_ask():
    global state, data
    output = ""
    
    input_text = request.values.get('text')
    if input_text:
        state, data, output_on_input = on_input(state, input_text, data)
        if output_on_input:
            output+= output_on_input
    else:
        output_on_enter = on_enter_state(state, data)

        if output_on_enter:
            output += output_on_enter

    return output

if __name__ == '__main__':
    app.run(debug=True)