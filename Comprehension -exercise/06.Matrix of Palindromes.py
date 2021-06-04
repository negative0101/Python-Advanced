def generate_element(row, col):
    base = ord('a')

    first_letter = chr(row + base)
    middle_letter = chr(row + base + col)
    return f'{first_letter}{middle_letter}{first_letter}'


n, m = input().split()
n, m = int(n), int(m)

matrix = [[generate_element(row, col) for col in range(m)] for row in range(n)]
print('\n'.join(' '.join([str(el) for el in row]) for row in matrix))


                                #_____ANOTHER WAY TO SOLVE_____#
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#matrix = []
#rows, columns = [int(i) for i in input().split(' ')]
#for i in range(rows):
#    matrix.append([])
#    for j in range(columns):
#        if i == 0:
#            matrix[-1].append(alphabet[i].lower() + alphabet[j].lower() + alphabet[i].lower())
#        else:
#            matrix[-1].append(alphabet[i].lower() + alphabet[j + i].lower() + alphabet[i].lower())
#print('\n'.join(' '.join([str(el) for el in x]) for x in matrix))