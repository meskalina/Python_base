# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе
# класса Worker. В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self):
        self.surname = input('Введите фамилию сотрудника: ')
        self.name = input('Введите имя сотрудника: ')
        self.position = input('Введите должность сотрудника: ')
        self._income = {"wage": float(input('Введите его оклад: ')), "bonus": float(input('Введите его премию: '))}


class Position(Worker):
    def get_full_name(self):
        print(self.surname + ' ' + self.name)

    def get_total_income(self):
        print(sum(self._income.values()))


some_worker = Position()
some_worker.get_full_name()
some_worker.get_total_income()
