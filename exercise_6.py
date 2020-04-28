# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.


list_goods = []
analysis_dict = {}
name_list = []
price_list = []
quantity_list = []
measure_set = set()
key_1, key_2, key_3, key_4 = 'название', 'цена', 'количество', 'ед'
goods_quantity_in_data_base = 3
count = 1
try:
    while count <= goods_quantity_in_data_base:     # в техзадании условие не указано
        name = input(f'Введите {key_1} {count} товара: ')
        price = int(input(f'Введите {key_2} {count} товара: '))
        quantity = int(input(f'Введите {key_3} {count} товара: '))
        measure = input(f'Введите {key_4} измерения: ')
        dict_goods = {key_1: name, key_2: price, key_3: quantity, key_4: measure}
        tuple_goods = (count, dict_goods)
        list_goods.append(tuple_goods)
        name_list.append(list_goods[count-1][1][key_1])
        price_list.append(list_goods[count-1][1][key_2])
        quantity_list.append(list_goods[count-1][1][key_3])
        measure_set.add(list_goods[count-1][1][key_4])
        count += 1
except ValueError:
    print('Вводите в это поле число!')
analysis_dict = {key_1: name_list, key_2: price_list, key_3: quantity_list, key_4: list(measure_set)}
for elem in list_goods:
    print(elem)
for key, value in analysis_dict.items():
    print(f'{key}:{value}')
