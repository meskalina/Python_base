# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления
# на ноль.


def division(num1, num2):
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print('Делить на ноль можно только в универе!')


try:
    division(float(input('Введите делимое: ')), float(input('Введите делитель: ')))
except (NameError, ValueError):
    print('Это не число!')
