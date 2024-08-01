def constructor(*args):
    stars, spaces = args
    spaces -= stars
    print(" " * spaces + "* " * stars)


def pattern(s):
    for i in range(1, size + 1):
        constructor(i, size)
    for i in range(size - 1, -1, -1):
        print(" " * (size - i) + "* " * i)


size = int(input())
pattern(size)