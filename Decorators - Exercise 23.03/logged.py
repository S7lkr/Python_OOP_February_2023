def logged(func):
    def wrapper(*args):
        str_args = ', '.join(str(d) for d in args)
        return f"you called {func.__name__}({str_args})\n" \
               f"it returned {func(*args)}"
    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))