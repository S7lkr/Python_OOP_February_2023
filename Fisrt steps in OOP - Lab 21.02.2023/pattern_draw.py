def choose_pattern():
    allowed = ("square", "triangle", "rhombus")

    def pattern_input():
        patt = input("Enter type of pattern:\n- square\n- triangle\n- rhombus\nPattern choice: ")
        return patt

    pattern = pattern_input()
    while pattern not in allowed:
        print("\nPlease type a valid pattern!")
        pattern = pattern_input()
        continue
    else:
        pattern_size = int(input("Enter pattern size: "))
        return pattern, pattern_size


def spaces_and_stars(size, i):
    spaces, stars = size - i, i
    return stars, spaces     # REMEMBER: returns a TUPLE -> (spaces, size)


def print_pattern(info):      # prints each ROW of the pattern (func called on EVERY iteration below)
    st, sp = info
    print(" " * sp + "* " * st)   # this func is called on every PATTERN ITERATION


def get_patten_data(data):  # NOTE: data -> one TUPLE: (spaces, size); *data -> ((spaces, size),) !!
    pattern, size = data

    if pattern.lower() == "square":
        for i in range(1, size + 1):
            print_pattern(spaces_and_stars(i, size))    # to print curr row, we call "print_pattern" func to do that

    if pattern.lower() == "triangle":
        for i in range(1, size + 1):
            print_pattern(spaces_and_stars(size, i))

    if pattern.lower() == "rhombus":
        for i in range(1, size + 1):
            print_pattern(spaces_and_stars(size, i))

        for i in range(size - 1, -1, -1):
            print_pattern(spaces_and_stars(size, i))


get_patten_data(choose_pattern())