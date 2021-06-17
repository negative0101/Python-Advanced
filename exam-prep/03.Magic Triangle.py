def get_magic_triangle(n):
    matrix = []
    for i in range(1, n + 1):
        matrix.append([1] * i)
    for j in range(2, len(matrix)):
        for k in range(1, len(matrix[j]) - 1):
            matrix[j][k] = matrix[j - 1][k - 1] + matrix[j - 1][k]
    return matrix


print(get_magic_triangle(5))

x = [
    [1],
    [1, 1],
    [1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1, 1],

]
