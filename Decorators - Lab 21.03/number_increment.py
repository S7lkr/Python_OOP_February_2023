def increment_decorator(func):
    def wrapper(numbers):
        numbers = [num + 1 for num in numbers]
        return func(numbers)
    return wrapper


@increment_decorator
def number_increment(numbers):
    return numbers


# def number_increment(numbers):
#     def increase():
#         inc_list = [num + 1 for num in numbers]
#         return inc_list
#     return increase()


print(number_increment([1, 2, 3]))