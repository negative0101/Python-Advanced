def math_operations(*args, **kwargs):
    list_args = list(args)
    while list_args:

        kwargs['a'] += list_args.pop(0)
        if not list_args:
            break
        kwargs['s'] -= list_args.pop(0)
        if not list_args:
            break
        try:
            kwargs['d'] /= list_args.pop(0)
            if not list_args:
                break
        except ZeroDivisionError:
            pass
        kwargs['m'] *= list_args.pop(0)
        if not list_args:
            break


    return kwargs

print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))