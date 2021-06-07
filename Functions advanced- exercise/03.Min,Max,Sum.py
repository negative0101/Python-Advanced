def min_max_sum(n):
    print(f"The minimum number is {min(n)}")
    print(f"The maximum number is {max(n)}")
    print(f"The sum number is: {sum(n)}")


n = [int(i) for i in input().split()]
min_max_sum(n)