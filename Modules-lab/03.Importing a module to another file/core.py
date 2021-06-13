def print_first_part(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(' '.join(str(j)), end=' ')
        print()


def print_second_part(n):
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(' '.join(str(j)), end=' ')
        print()


def print_triangle(n):
    print_first_part(n)
    print_second_part(n)
