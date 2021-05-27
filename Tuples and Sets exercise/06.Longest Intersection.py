n = int(input())

max_so_far = None

for _ in range(n):
    first_line,second_line = input().split('-')
    first_line = first_line.split(',')
    second_line = second_line.split(',')

    first_line = (int(first_line[0]),int(first_line[1]))
    second_line = (int(second_line[0]),int(second_line[1]))

    near_point = max(first_line[0],second_line[0])
    far_point = min(first_line[1],second_line[1])

    current_span = far_point - near_point +1

    if max_so_far is None or current_span > len(max_so_far):
        max_so_far = list(range(near_point,far_point +1))

print(f'Longest intersection is {max_so_far} with length {len(max_so_far)}')