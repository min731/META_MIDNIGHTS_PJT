from pathlib import Path
import json
import pickle

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

from models.get_contents import GetContents


class OpenAIChat():
    def __init__(self) -> None:
        self.prompt = self.get_prompt()
        self.model = self.get_model()
    
    def get_model(self) -> ChatOpenAI:
        secret_path = Path("resource").joinpath("secret.json")
        secrets = json.loads(open(secret_path).read())
        openai_api_key = secrets["OPENAI_API_KEY"]
        chat_model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
        conversation = ConversationChain(
            prompt=self.prompt,
            llm=chat_model,
            verbose=False,
            memory=ConversationBufferWindowMemory(memory_key='history', ai_prefix="AI Assistant", k=5)
        )
        return conversation
    
    def get_prompt(self) -> ChatPromptTemplate:
        template = """
                Current conversation:
                {history}
                Human: {input}
                AI Assistant:"""

        prompt = PromptTemplate(input_variables=["history","input"], template=template)
        return prompt
    
    def get_answer(self, text) -> str:
        return self.model.predict(input=text)
        
        
if __name__ == '__main__':
    openai_chatbot = OpenAIChat()
    get_contents = GetContents()
    
    # text = "판소리북와 다ㅇ비파의 차이저ㅁ이 뭐야?"
    
    with open('instruments_contents/instruments_content.pickle', 'rb') as f:
        instruments_contents = pickle.load(f)

    all_instruments = instruments_contents.keys()

    while True:
        text = input("Human >> ")
        if 'quit' in text:
            break
        req_instruments = get_contents.get_instruments(text)
        correct_text = get_contents.get_correct_text(text)

        # input_ = '' + correct_text
        # for req_instrument in req_instruments:
        #     input_ += req_instrument+'에 대한 설명이야.'+instruments_contents[req_instrument]

        result = openai_chatbot.get_answer(text)
        print("Chabot >> " + result)

    # classification_server = "http://192.168.0.32:8000/nlp/classification"
    # emotion = server_connection.get_emotion(classification_server, result)
    # print(emotion)