def type_check(value_type):
    def decorator(func):
        def wrapper(*args):
            for el in args:
                if not isinstance(el, value_type):
                    return "Bad Type"   # if return "Bad type" == break
            return func(*args)      # if no break -> all elements are of the CORRECT type
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))