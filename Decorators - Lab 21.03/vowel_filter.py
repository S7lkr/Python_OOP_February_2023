def vowel_filter(function):
    def wrapper():
        func_res = function()     # func has no parameters, so STORE its RESULT: func_res = ["a", "b", "c", "d", "e"]
        filtered = [ch for ch in func_res if ch.lower() in "aiouey"]    # iterate through "func_res" to get all vowels
        return filtered           # wrapper returns ["a", "e"]
    return wrapper           # the whole "vowel_filter" DECORATOR returns wrapper's result -> ["a", "e"]


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())