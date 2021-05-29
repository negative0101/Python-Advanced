n = int(input())

matrix = []
sum = 0
for i in range(n):
    numbers = input().split()
    matrix.append(numbers)

for j in range(n):
    sum += int(matrix[j][j])
print(sum)
