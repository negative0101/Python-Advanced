def absolute_value(nums):
    return [abs(el) for el in nums]

list_of_nums = [float(el) for el in input().split()]
print(absolute_value(list_of_nums))