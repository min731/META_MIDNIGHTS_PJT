from flask import Flask, request, jsonify, send_file
import pickle
from gtts import gTTS

from models.openai_api import OpenAIChat
from models.get_contents import GetContents
from models.make_input import make_input

app = Flask(__name__)
openai_chatbot = OpenAIChat()
get_contents = GetContents()

@app.route("/", methods=["get"])
def home():
    return 'hello!'


@app.route("/answer",methods=['POST'])
def test():
    input_json = request.json
    input_ = make_input(input_json["id"], input_json["content"])

    result = openai_chatbot.get_answer(input_)
    print("sumery >> " + result)

    return jsonify({"items": [{"id": input_json["id"], "content": result}]})


@app.route("/send_sound",methods=['POST'])
def send_sound():
    input_json = request.json
    print(input_json)
    input_ = make_input(input_json["id"], input_json["content"])

    result = openai_chatbot.get_answer(input_)
    sumery = '. '.join(result[:90].split('. ')[:-1])
    print("sumery >> " + sumery)

    tts = gTTS(text=sumery, lang='ko')
    filename='resource/temp.mp3'
    tts.save(filename)

    content =   {"items": [{"id": input_json["id"], "content": input_json["content"]}]}

    return send_file(filename, mimetype='audio/mp3')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

