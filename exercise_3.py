# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите число: ')

if number == '0':
    print('Сумма равна нулю')
elif int(number) < 0:
    print('Введите положительное число')
else:
    number_1 = int(number)
    number_2 = int(number*2)
    number_3 = int(number*3)
    sum = number_1 + number_2 + number_3
    print(number, '+', number*2, '+', number*3, '=', sum)