# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
# несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, colour, name):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = False

    def go(self):
        if self.speed != 0:
            return f'Машина движется'
        else:
            return f'Машина стоит'

    def stop(self):
        if self.speed == 0:
            return f'Машина стоит'
        else:
            return f'Машина движется'

    def turn(self, direction='straight'):  # я не понял, как получать входные данные направления
        if direction != 'straight':
            return f'{self.name} повернула {direction}'
        else:
            return f'Машина едет прямо'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        max_speed = 60
        if self.speed > max_speed:
            return f'Вы превысили скорость'
        else:
            return f'Текущая скорость {self.name} - {self.speed} км/ч'


class WorkCar(Car):
    def show_speed(self):
        max_speed = 40
        if self.speed > max_speed:
            return f'Вы превысили скорость'
        else:
            return f'Текущая скорость {self.name} - {self.speed} км/ч'


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)
        self.is_police = True


car1 = Car(80, 'белый', 'камаз')
car2 = TownCar(40, 'черный', 'ваз')
car3 = TownCar(100, 'черный', 'ваз')
car4 = WorkCar(30, 'синий', 'bmw')
car5 = WorkCar(100, 'синий', 'bmw')
car6 = SportCar(160, 'красный', 'audi')
car7 = PoliceCar(110, 'хаки', 'БТР')
print(car1.go())
print(car1.stop())
print(car1.turn())
print(car1.show_speed())
print(car2.show_speed())
print(car3.show_speed())
print(car4.show_speed())
print(car5.show_speed())
print(car6.show_speed())
print(car7.is_police)
print(car2.is_police)
