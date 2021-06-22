from collections import deque

total_pizza = 0
orders = deque([int(pizza) for pizza in input().split(', ')])
employees = [int(worker) for worker in input().split(', ')]

orders = deque([i for i in orders if i > 0 if i <= 10])
completed = True
while orders and employees:
    first_pizza = orders[0]
    last_baker = employees[-1]
    if first_pizza <= last_baker:
        first_pizza = orders.popleft()
        last_baker = employees.pop()
        total_pizza += first_pizza
    else:
        try:
            orders[0] = first_pizza - last_baker
            total_pizza += last_baker
            employees.pop()
            while True:
                if orders[0] <= employees[-1]:
                    employees[-1] = employees[-1] - orders[0]
                    first_pizza = orders.popleft()
                    last_baker = employees.pop()
                    total_pizza += first_pizza
                    break
                else:
                    orders[0] -= employees[-1]
                    employees.pop()
                    if orders[0] > 0:
                        continue
                    break
        except IndexError:
            completed = False

if completed:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza}')
    print(f"Employees: {', '.join([str(i) for i in employees])}")

else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(i) for i in orders])}')
