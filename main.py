from data import questions_data
import html
from questions_data import QuestionData
from brain import QuizBrain
from user_interface import QuizInterface


questions_bank = []

for question in questions_data:
    question_text = html.unescape(question["question"])
    answer_text = question["correct_answer"]
    all_question = QuestionData(question_text, answer_text)
    questions_bank.append(all_question)

questions_quiz = QuizBrain(questions_bank)
interface = QuizInterface(questions_quiz)


print("Game over")


