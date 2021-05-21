from collections import deque

text = input()
queue = deque()
while not text == 'End':
    if text == 'Paid':
        while queue:
            name = queue.popleft()
            print(name)
    else:
        queue.append(text)
    text = input()

else:
    print(f'{len(queue)} people remaining.')
dd