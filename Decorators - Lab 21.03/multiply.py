# def multiply(times):
#     return lambda f: lambda *args, **kwargs: f(*args, **kwargs) * times   # -> abomination :D


def multiply(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * times
        return wrapper
    return decorator


@multiply(3)        # "@multiply" will call 3 TIMES the "add_ten" func
def add_ten(number):
    return number + 10


print(add_ten(3))