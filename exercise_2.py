# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых
# больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования
# списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [elem for count, elem in enumerate(my_list) if my_list[count] > my_list[count-1] and count > 0]
print(new_list)
