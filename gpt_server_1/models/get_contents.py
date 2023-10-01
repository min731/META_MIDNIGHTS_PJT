from konlpy.tag import Komoran
import pickle

class GetContents():
    def __init__(self) -> None:
        self.komoran = Komoran(userdic="custom_dict/custom_dict.txt")
        self.all_instruments = [
            '아쟁', '특종', '징', '중고', 
            '장고', '월금', '박', '꽹가리',
            '자바라', '피리', '편경', '나발',
            '좌고', '거문고', '와공후', '편종',
            '진고', '대금', '대고', '단소', '어', 
            '갈고', '당비파', '나각', '태평소', 
            '뇌고', '수공후', '뇌도', '소고', 
            '북', '판소리북', '슬', '가야금'
        ]
        

    def get_instruments(self, question):
        poses = self.komoran.pos(question)
        req_instruments = [pose[0] for pose in poses if pose[1]=='NNP' and pose[0] in self.all_instruments]

        return req_instruments
    
    def get_correct_text(self, question):
        poses = self.komoran.morphs(question)
        correct_text = ' '.join(poses)

        return correct_text


if __name__ == '__main__':
    question = "판소리북와 다ㅇ비파의 차이저ㅁ이 뭐야?"

    get_contents = GetContents()

    req_instruments = get_contents.get_instruments(question)
    print(req_instruments)