num_names = int(input())
names = set()

for _ in range(num_names):
    names.add(input())
[print(j) for j in names]