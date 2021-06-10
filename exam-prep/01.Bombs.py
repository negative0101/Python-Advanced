from collections import deque


bomb_pouch = {40: 'datura bombs', 60: 'cherry bombs', 120: 'smoke decoy bombs'}
each_of_3_found = False

datura = 0
cherry = 0
smoke = 0
values = [40, 60, 120]
que = deque([int(i) for i in input().split(', ')])
stack = [int(i) for i in input().split(', ')]
first_bomb_effect = que[0]
last_bomb_casing = stack[-1]

while not each_of_3_found and (len(que) > 0 and len(stack) > 0):
    if datura >= 3 and cherry >= 3 and smoke >= 3:
        each_of_3_found = True
        break
    if (first_bomb_effect + last_bomb_casing) in values:
        if (first_bomb_effect + last_bomb_casing) == 40:
            datura += 1
        elif (first_bomb_effect + last_bomb_casing) == 60:
            cherry += 1
        elif (first_bomb_effect + last_bomb_casing) == 120:
            smoke += 1
        que.popleft()
        stack.pop()
        if stack and que:
            first_bomb_effect = que[0]
            last_bomb_casing = stack[-1]
    else:
        last_bomb_casing -= 5

if each_of_3_found:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")
if que:
    print(f'Bomb Effects: {", ".join([str(i)for i in que])}')
else:
    print(f'Bomb Effects: empty')
if stack:

    print(f'Bomb Casings: {", ".join([str(i)for i in stack])}')
else:
    print(f'Bomb Casings: empty')

print(f'Cherry Bombs: {cherry}')
print(f'Datura Bombs: {datura}')
print(f'Smoke Decoy Bombs: {smoke}')
