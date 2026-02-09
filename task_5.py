from pprint import pprint # импортировал функцию pprint для красивого вывода с форматированием

class TestCase(): 

    def __init__(self):
        self.steps = {} # инициализировал атрибут для сбора шагов и их значений
        self.result = None # инициализировал атрибут для сбора результатов

    def set_step(self, step_number, step_text): # метод добавляет в словарь steps шаг тест-кейса по ключу
        self.steps[step_number] = step_text

    def delete_step(self, step_number): # метод удаляет в словарь steps шаг тест-кейса по ключу
        if step_number in self.steps:
            del self.steps[step_number]

    def set_result(self, result): # метод добавляет ожидаемый результат
        self.result = result 

    def get_test_case(self): # метод выводит шаги и результат в требуемом формате
        pprint({'Шаги': self.steps, 'Ожидаемый результат': self.result})