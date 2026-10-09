


def addImprov(func):
    def wrapper(a,b):
        print("Adding two numbers")
        return func(a,b)
    return wrapper

@addImprov
def add_nums(a,b):
    return a+b


res = add_nums(5,6)

print(res)