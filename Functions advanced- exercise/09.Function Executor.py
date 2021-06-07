def sum_numbers(*nums):
    return sum(nums)

def multiply_numbers(num1,num2):
    return num1 * num2

def func_executor(*funcs_with_args):
    res = []
    for func,fargs in funcs_with_args:
        func_result = func(*fargs)
        res.append(func_result)

    return res

