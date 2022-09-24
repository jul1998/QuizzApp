
class QuizBrain:

    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def check_if_more_question(self):
        return len(self.question_list) > self.question_number

    def ask_user_next_question(self):
        global current_question
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"{self.question_number}/{current_question.q_text} True or False? "

        # self.check_user_answer(user_input)

    def check_user_answer(self, user_answer: str):
        current_answer = current_question.a_text
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            return True
        else:
            return False

        print(f"Your score: {self.score}/{len(self.question_list)}")
        print("\n")



