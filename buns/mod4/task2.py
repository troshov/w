def power(a, n):
    if n == 1:
        return a
    elif n == 2:
        return a * a
    elif n % 2 == 1:
        return a * power(a, n - 1)       
    else:
        return power(power(a, 2), n / 2)

numbers_tuple = tuple(input("Введите число и степень, в которую необходимо возвести число: ").split())
print(power(int(numbers_tuple[0]), int(numbers_tuple[1])))