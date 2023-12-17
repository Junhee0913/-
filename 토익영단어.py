import random

class Vocabulary:
    def __init__(self):
        self.words = {
            'position': '직책,두다',
            'certificate': '증명서',
            'ideal': '이상적인',
            'degree' : '학위',
            'application' : '지원,신청',
            'candidate' : '지원자,후보자',
            'requirement' : '필요조건',
            'experience' : '경험,체험',
            'interview' : '면접',
            'ethic' : '윤리,도덕',
            'hire' : '고용하다',
            'employee' : '직원',
            'immediately' : '즉시,바로',
            'invite' : '초대하다',
            'qualified' : '자격이 있는,적격의',
            # 여기에 더 많은 단어 추가
        }

    def get_random_word(self):
        return random.choice(list(self.words.keys()))

    def quiz(self):
        word = self.get_random_word()
        answer = self.words[word]

        print(f'단어: {word}')
        user_input = input('뜻을 입력하세요: ')

        if user_input.lower() == answer.lower():
            print('정답입니다!')
        else:
            print(f'틀렸습니다. 정답은 {answer} 입니다.')

def main():
    vocabulary = Vocabulary()

    while True:
        print("\n==== 영어 단어 학습 프로그램 ====")
        print("1. 퀴즈 시작")
        print("2. 종료")
        
        choice = input("선택하세요 (1 또는 2): ")

        if choice == '1':
            vocabulary.quiz()
        elif choice == '2':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()
