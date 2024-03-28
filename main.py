import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

# Вопросы по древнегреческой мифологии
questions = [
    {"question": "Кто из олимпийских богов является богиней мудрости и военного искусства?",
     "image": "C:\\Users\\qwerty\\pr38\\athena.jpg", "options": ["Афина", "Гера", "Афродита", "Деметра"],
     "correct": "Афина"},
    {"question": "Какой титан был владыкой времени в древнегреческой мифологии?", "image": "C:\\Users\\qwerty\\pr38\\cronus.jpg", "options": ["Кронос", "Уран", "Океан", "Зевс"], "correct": "Кронос"},
    {"question": "Как звали главного героя трагедии Софокла 'Царь Эдип'?", "image": "C:\\Users\\qwerty\\pr38\\oedipus.jpg", "options": ["Ахиллес", "Геракл", "Одиссей", "Эдип"], "correct": "Эдип"},
    {"question": "Как звали бога подземного мира в древнегреческой мифологии?", "image": "C:\\Users\\qwerty\\pr38\\hades.jpg", "options": ["Плутон", "Зевс", "Хаос", "Аид"], "correct": "Аид"},
    {"question": "Как звали бога солнца в древнегреческой мифологии?", "image": "C:\\Users\\qwerty\\pr38\\apollo.jpg", "options": ["Гелиос", "Аполлон", "Феб", "Арес"], "correct": "Аполлон"},
    {"question": "Как звали бога войны в древнегреческой мифологии?", "image": "C:\\Users\\qwerty\\pr38\\ares.jpg", "options": ["Дионис", "Арес", "Гермес", "Геракл"], "correct": "Арес"},
    {"question": "Какой титан является матерью богов и королевой богинь в древнегреческой мифологии?", "image": "rhea.jpg", "options": ["Рея", "Темида", "Мнемосина", "Лето"], "correct": "Рея"},
    {"question": "Как звали бога торговли и воровства в древнегреческой мифологии?", "image": "hermes.jpg", "options": ["Гермес", "Геракл", "Гефест", "Посейдон"], "correct": "Гермес"},
    {"question": "Какая богиня была покровительницей семьи и домашнего очага в древнегреческой мифологии?",
     "image": "C:\\Users\\qwerty\\pr38\\hestia.jpg",
     "options": ["Гера", "Деметра", "Афина", "Гестия"],
     "correct": "Гестия"},
    {"question": "Как звали богиню охоты и дикой природы в древнегреческой мифологии?",
     "image": "C:\\Users\\qwerty\\pr38\\artemis.jpg",
     "options": ["Афродита", "Гера", "Артемида", "Афина"],
     "correct": "Артемида"}
]


class TestApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.test_screen = TestScreen(name='test')
        self.result_screen = ResultScreen(name='result')
        self.sm.add_widget(self.test_screen)
        self.sm.add_widget(self.result_screen)
        return self.sm

class TestScreen(Screen):
    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        self.current_question = 0
        self.score = 0
        self.questions_order = list(range(len(questions)))
        random.shuffle(self.questions_order)
        self.load_question()

    def load_question(self):
        if self.current_question < len(questions):
            q_index = self.questions_order[self.current_question]
            q_data = questions[q_index]
            self.clear_widgets()
            layout = BoxLayout(orientation='vertical')
            image = Image(source=q_data['image'])
            layout.add_widget(image)
            question_label = Label(text=q_data['question'])
            layout.add_widget(question_label)
            options_layout = BoxLayout(orientation='vertical')
            for option in q_data['options']:
                button = Button(text=option, on_press=self.check_answer)
                options_layout.add_widget(button)
            layout.add_widget(options_layout)
            self.add_widget(layout)
        else:
            self.parent.get_screen('result').update_result(self.score, len(questions))
            self.parent.current = 'result'

    def check_answer(self, instance):
        q_index = self.questions_order[self.current_question]
        correct_answer = questions[q_index]['correct']
        if instance.text == correct_answer:
            self.score += 1
        self.current_question += 1
        self.load_question()

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.result_label = Label()
        self.add_widget(self.result_label)

    def update_result(self, score, total_questions):
        self.result_label.text = f'Вы набрали {score} из {total_questions} баллов.'

if __name__ == '__main__':
    TestApp().run()
