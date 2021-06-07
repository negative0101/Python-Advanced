def even(n):
    return n % 2 == 0


def odd(n):
    return n % 2 != 0


def even_odd(*args):
    list_of_nums = args[:len(args) - 1]
    command = args[len(args) - 1]
    if command == 'even':
        return list(filter(even, list_of_nums))
    else:

        return list(filter(odd, list_of_nums))


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
