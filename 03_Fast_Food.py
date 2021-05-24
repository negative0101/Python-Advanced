from collections import deque

total_food__quantity = int(input())

order_queue = deque()
for order in input().split():
    order_queue.append(int(order))

max_order = max(order_queue)

for i in range(len(order_queue)):
    order = order_queue.popleft()
    if order <= total_food__quantity:
        total_food__quantity -= order
    else:
        order_queue.appendleft(order)
        break
print(max_order)
if len(order_queue) == 0:
    print(f'Orders complete')
else:
    print(f'Orders left:', ' '.join([str(order) for order in order_queue]))