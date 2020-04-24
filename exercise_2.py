# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_seconds = abs(int(input('Введите количество секунд: ')))

hours = user_seconds // 3600
# last_user_seconds = user_seconds - hours * 3600
minutes = (user_seconds - hours*3600) // 60
seconds = (user_seconds - hours*3600) - minutes*60

# if hours == 0:
#     if minutes == 0:
#         print(f"{seconds} секунд")
#     else:
#         print(f"{minutes} минут {seconds} секунд")
# else:
#         print(f"{hours} часов {minutes} минут {seconds} секунд")
if hours < 10:
    if minutes < 10:
        if seconds < 10:
            print(f'0{hours}:0{minutes}:0{seconds}')
        else:
            print(f'0{hours}:0{minutes}:{seconds}')
    elif seconds < 10:
        print(f'0{hours}:{minutes}:0{seconds}')
    else:
        print(f'0{hours}:{minutes}:{seconds}')
elif minutes < 10:
        if seconds < 10:
            print(f'{hours}:0{minutes}:0{seconds}')
        else:
            print(f'{hours}:0{minutes}:{seconds}')
else:
    print(f'{hours}:{minutes}:{seconds}')