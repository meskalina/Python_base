# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(num1, num2, num3):
    z = [num1, num2, num3]
    z.remove(min(num1, num2, num3))
    return sum(z)


print(my_func(int(input('Enter some num: ')),
              int(input('Enter some num: ')),
              int(input('Enter some num: '))))
