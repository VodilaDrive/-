array = list(map(int, input("Введите целые числа в любом порядке, через пробел: ").split()))
element = int(input("Введите любое положительное целое число из полученного списка: "))

def merge_sort(L): # сортировка слиянием
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

print('Сортированный список', merge_sort(array))
left = float(array[0])
right = float(array[-1])
if element < left or element > right:
        print('Числа нет в диапазоне')
else:
        print('Индекс элемента, ближайшего минимального от введенного числа ', binary_search(array, element, 0, len(array) - 1))