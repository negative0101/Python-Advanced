n =int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

left_side = [matrix[i][i] for i in range(n)]
right_side = [matrix[i][n-1 -i] for i in range(n)]
print(f'First diagonal: {", ".join((str(left_side[i]) for i in range(len(left_side))))}. Sum: {sum(left_side)}')
print(f'Second diagonal: {", ".join((str(right_side[i]) for i in range(len(right_side))))}. Sum: {sum(right_side)}')