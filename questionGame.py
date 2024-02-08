class Question:
    def __init__(self):
        self.questions = {
            1: {
                "question": 'What is capital city of Indonesia?: ',
                "answer": "Jakarta",
            },
            2: {
                "question": "What is capital city of Russia?: ",
                "answer": "Moskow",
            },
            3: {
                "question": "What is capital city of Amerika?: ",
                "answer": "Washington",
            },
            4: {
                "question": "What is capital city of China?: ",
                "answer": "Beijing",
            }
        }
        
    def generate_question(self, question):
        for key, value in question.items():
            correct_answer = value['answer'].lower()
            userAnswer = input(f"{value['question']}")
            if correct_answer == userAnswer.lower():
                print("You right")
            else:
                print(f"you wrong, the answer is {correct_answer}")
    
    
    def play(self):
        question = self.questions
        self.generate_question(question)

    
quiz = Question()
quiz.play()