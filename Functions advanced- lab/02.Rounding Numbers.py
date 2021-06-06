def round_numbers(nums):
    nums= [round(float(n)) for n in nums ]
    return nums

list_ = input().split()
print(round_numbers(list_))