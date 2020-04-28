# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input()


my_list = list(input('Введите любое слово: '))
for elem in my_list:
    if my_list.index(elem) % 2 == 1:
        index_popped_item = my_list.index(elem)
        popped_item = my_list.pop(index_popped_item)
        my_list.insert(index_popped_item-1, popped_item)
print(my_list)
