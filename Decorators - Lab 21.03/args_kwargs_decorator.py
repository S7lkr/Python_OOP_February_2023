def repeat(num):
    def decorator_repeat(func):         # this func "decorator_repeat" will take the other func (greet) AS PARAMETER !
        def wrapper(*args, **kwargs):       # args = "SoftUni", NO kwargs in this case
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat


@repeat(4)      # repeat func "greet()" 4 times
def greet(name="Maria"):
    print(f"Hello, {name}")


greet("SoftUni")    # if we call the func without argument "name", it will be "Maria" (by default)