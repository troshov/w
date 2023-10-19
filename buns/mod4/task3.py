def min_del(a, b):
    if a == b:
        return a
    elif a > b:
        return min_del(a - b, b)
    else:
        return min_del(a, b - a)
    
numbers_tuple = tuple(input("Введите числа для определения НОД: ").split())
print(min_del(int(numbers_tuple[0]), int(numbers_tuple[1])))