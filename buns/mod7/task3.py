import functools
import time

class timers():
    def __init__(self) -> None:
        self.allTime = time.time()
    
    def end(self):
        print('В классе:{}'.format(time.time() - self.allTime))

    def func(self, func):
        a = func
        self.end()

#print ('Время выполнения в таймере: {} секунд.'.format(round(end - start, 16)))

def timer(func):   
    start = timers()
    @functools.wraps(func)    
    def wrapper(n):
        a = func(n)
        #start.end()
        return a
    
    
    return wrapper


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



def awe(n):
    a = 1
    for i in range(n):
        for k in range(n):
            for j in range(n):
                for q in range(n):
                    a += 1
    return a




@timer
@memoize
def fibonacci(n):
    '''Возвращает число Фибоначчи'''
    if n < 2:
        awe(100)
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


startK = timers()
startK.func(fibonacci(250))





startK = timers()
#otv = awe(100)
startK.func(awe(100))

print('end')