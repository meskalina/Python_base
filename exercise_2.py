# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, title, size):
        self.title = title
        self.size = size

    @abstractmethod
    def coat_consumption(self):
        pass

    @abstractmethod
    def costume_consumption(self):
        pass

    @property
    def total_consumption(self):
        return (self.size / 6.5 + 0.5) + (2 * self.size + 0.3)


class Coat(Cloth):
    def coat_consumption(self):
        coat_consumption = self.size / 6.5 + 0.5
        return coat_consumption

    def costume_consumption(self):
        pass


class Costume(Cloth):
    def costume_consumption(self):
        costume_consumption = 2 * self.size + 0.3
        return costume_consumption

    def coat_consumption(self):
        pass


coat = Coat('qwe', 2)
costume = Costume('asd', 3)
print(coat.total_consumption)
print(coat.coat_consumption())
print(costume.costume_consumption())
