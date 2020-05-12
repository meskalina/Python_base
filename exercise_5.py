# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
# завершить программу.


def sigma():
    result = 0
    while True:
        numbers = input('Введите числа через пробел или q для выхода: ').split()
        for i in numbers:
            if i == 'q':
                print(f'Сумма равна {result}.')
                return
            else:
                result += int(i)
        print(f'Сумма равна {result}')


sigma()
