def validate_args(func):
    def wrapper(*args):
        if len(args) != 1:
            print("Not enough arguments" if len(args) < 1 else "Too many arguments")
            return
        if not isinstance(args[0], int):
            print("Wrong types")
            return
        if args[0] < 0:
            print("Negative argument")
            return
        return func(*args)
    return wrapper

@validate_args
def alfa(*args):
    for i in args:
        print(i ** 2)

alfa()
alfa(1,2,3,4)
alfa("12")
alfa(-2)
alfa(4)