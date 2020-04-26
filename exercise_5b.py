# или другой способ, не совсем точный


rate = [7, 5, 3, 3, 2]
try:
    user_score = int(input('Введите рейтинг: '))
    rate.append(user_score)
    rate.sort(reverse=True)
    print(rate)
except ValueError:
    print('Вводите только числа!')
