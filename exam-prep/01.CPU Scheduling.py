from collections import deque

que = deque(map(int, input().split(', ')))
priority = que[int(input())]
total = 0
is_found = False
while not is_found:
    current_i = 0
    lowest_num = 1000000000000
    for i in range(len(que)):
        if que[i] < lowest_num:
            lowest_num = que[i]
            current_i = i
    if lowest_num == priority:
        if que.count(lowest_num) > 1:
            total+= lowest_num
            que.remove(lowest_num)
            continue
        else:
            is_found = True
            total += lowest_num
            que.remove(lowest_num)
            break
    total += lowest_num
    que.remove(lowest_num)

print(total)