import functools

def memoize(func):
    fib_data = dict()

    @functools.wraps(func)
    def wrapped(n):
        if n not in fib_data:
            fib_data[n] = func(n)
            return fib_data[n]
        else:
            return fib_data[n]
    return wrapped

@memoize
def fibonacci(n):
    '''Возвращает число Фибоначчи'''
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))
print(fibonacci.__name__)
print(fibonacci.__doc__)