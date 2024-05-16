def even_numbers(function):
    def wrapper(numbers):
        info = function(numbers)        # NOTE: first, STORE the result of "get_numbers" func
        result = list(filter(lambda ch: ch % 2 == 0, info))
        return result
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))