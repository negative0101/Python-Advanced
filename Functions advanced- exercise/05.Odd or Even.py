command = input()
n = [int(i) for i in input().split()]

if command == 'Odd':
    filtered = filter(lambda x: x % 2 != 0,n)
else:
    filtered = filter(lambda x: x % 2 == 0,n)

result = sum(filtered) * len(n)
print(result)