from PyQt5.QtWidgets import QApplication

from random import choice, shuffle
from time import sleep

app = QApplication([])

from m2 import *
fromm m3 import *

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2,
                 wrong_answer3)
        self.question=question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer1 = wrong_answer2
        self.wrong_answer1 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
        self.isAsking = True
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question("Скільки сузір'їв перетинає Сонце протягом року?", "13", "12", "88", "11")
q2 = Question("Затеменення Сонця відбувається при:". "повного Місяця", "нового", "першої чверті", "останньої чверті")
q3 = Question("Телескоп - це:", "Окуляр", "Яблуко", "Прилад")

window.show()
app.exec_()
