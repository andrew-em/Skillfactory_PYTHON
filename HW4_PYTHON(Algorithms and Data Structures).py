
input_nums = input("Введите несколько чисел через пробел:").split()
for i in input_nums:
    if not i.isdigit():
        input_nums = input("Ошибка ввода. Вводите только числа через пробел:").split()
    else: pass

input_num = input("Введите число:").split()
for j in input_num:
    if j.isdigit() is not True:
        input_num = input("Ошибка ввода. Введите только число:").split()
    else: pass

list1 = [input_nums]
list2 = [input_num]
list_sum =list1 + list2

new_list = []
for number in list_sum:
    new_list += number

final_list = [int(i) for i in new_list]


def insertionSort(list):
    for num1 in range(1, len(list)):
        el = list[num1]
        num2 = num1 - 1
        while list[num2] > el and num2 >= 0:
            list[num2 + 1] = list[num2]
            num2 -= 1
        list[num2 + 1] = el
    return list

print("Отсортированный по возрастанию список:", insertionSort(final_list))


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
         return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

mass = insertionSort(final_list)
array = mass
element = input_num

print("Номер позиции элемента, соответствующего условиям:",binary_search(array, element, 0, len(array) - 1))

