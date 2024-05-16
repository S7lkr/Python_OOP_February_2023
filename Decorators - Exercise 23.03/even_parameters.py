def even_parameters(func):
    def wrapper(*args):
        if list(filter(lambda n: isinstance(n, str), args)) or list(filter(lambda n: n % 2 != 0, args)):
            return "Please use only even numbers!"
        return func(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))