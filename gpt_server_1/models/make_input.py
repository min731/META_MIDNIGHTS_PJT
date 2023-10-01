import pickle

from models.get_contents import GetContents


get_contents = GetContents()

def make_input(id_, contents):
    id_dic = {"1": "단소", "2": "태평소", "3": "대금", "4": "북", "5": "나각", 
              "6": "장구", "7": "자바라", "8": "특종", "9": "아쟁", "10": "가야금", 
              "11": "진고", "12": "노고(뇌고)", "13": "어", "14": "운라"}
    
    with open('instruments_contents/instruments_content.pickle', 'rb') as f:
            instruments_contents = pickle.load(f)
    
    all_instruments = instruments_contents.keys()

    req_instruments = get_contents.get_instruments(contents)
    correct_text = get_contents.get_correct_text(contents)

    if req_instruments == []:
        input_ = '' + correct_text
        input_ += id_dic[id_]+'에 대한 참고자료 : '+instruments_contents[id_dic[id_]]
    else:
        input_ = '' + correct_text
        for req_instrument in req_instruments:
            input_ += req_instrument+'에 대한 설명이야.'+instruments_contents[req_instrument]

    print(f"input text : {input_}")

    return input_