def multiply(*args):
    sum =1
    for i in args:
        sum*= i

    return sum

print(multiply(4, 5, 6, 1, 3))