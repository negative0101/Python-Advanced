n = int(input())

matrix = []
first_sum = 0
second_sum = 0
counter = 0

for i in range(n):
    row = [(int(el)) for el in input().split()]
    matrix.append(row)
for j in range(n):
    first_sum += matrix[j][j]
for k in range(n,0,-1):
    second_sum += matrix[counter][k -1]
    counter+=1
print(abs(first_sum-second_sum))
