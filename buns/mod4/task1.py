numders_tuple = tuple(input('Введите строку из чисел через пробел: ').split())
numbers_set = set(numders_tuple)
if len(numbers_set) == 1:
    print('Все числа равны')
elif len(numbers_set) != len(numders_tuple):
    print('Есть равные и неравные числа')
else:
    print('Все числа разные')