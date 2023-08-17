import os
from flask import Flask, request, jsonify
from chatgpt import ChatGPTBOT

app = Flask(__name__)
chatbot = ChatGPTBOT(os.environ.get('API_KEY'))
chatbot.initialize_gpt3()


@app.route('/create_prompt', methods=['POST'])
def create_prompt():
    data = request.json
    prompt = data.get('prompt')
    if prompt:
        chatbot.create_prompt(prompt)
        return "Prompt created successfully"
    else:
        return "Prompt cannot be empty", 400


@app.route('/get_response/<int:index>', methods=['GET'])
def get_response(index):
    response = chatbot.get_response(index)
    return jsonify({"response": response})


@app.route('/update_prompt/<int:index>', methods=['PUT'])
def update_prompt(index):
    data = request.json
    new_prompt = data.get('new_prompt')
    if new_prompt:
        result = chatbot.update_prompt(index, new_prompt)
        return result
    else:
        return "New prompt cannot be empty", 400


if __name__ == '__main__':
    app.run(debug=True, port=3000, load_dotenv=True)
