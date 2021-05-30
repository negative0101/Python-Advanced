n = int(input())

matrix = []
is_in_matrix = False
for i in range(n):
    ascii_chars = input()
    current_list = []
    for x in ascii_chars:
        current_list.append(x)
    matrix.append(current_list)
symbol_to_find = input()

for j in range(n):
    for k in range(n):
        if matrix[j][k] == symbol_to_find:
            print(f'({j}, {k})')
            is_in_matrix = True
            break
    if is_in_matrix:
        break
if not is_in_matrix:
    print(f'{symbol_to_find} does not occur in the matrix')
