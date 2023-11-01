def armstrong_numbers_generator():
    x = 1
    num_return = 0
    while num_return <= 88:
        sum_x = sum(int(num)**3 for num in str(x))
        x += 1
        if sum_x == x - 1:
            num_return += 1
            yield x - 1

generator = armstrong_numbers_generator()

def get_armstrong_numbers():
    return next(generator)

for i in range(5):
    print(get_armstrong_numbers(), end=" ")