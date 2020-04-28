# Реализовать структуру «Рейтинг», представляющую собой невозрастающий набор натуральных
# чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.


rate = [7, 5, 3, 3, 2]
try:
    user_score = int(input('Введите рейтинг: '))
    for elem in rate:
        if user_score > elem:
            rate.insert(rate.index(elem), user_score)
            print(rate)
            break
        elif user_score == elem:
            continue
        elif user_score <= rate[-1]:
            rate.append(user_score)
            print(rate)
            break
except ValueError:
    print('Вводите только числа!')
