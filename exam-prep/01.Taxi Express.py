from collections import deque

all_customers = deque([int(_) for _ in input().split(', ')])
all_taxi = [int(_) for _ in input().split(', ')]

total_time = 0
while len(all_taxi) != 0 or len(all_customers) != 0:
    if all_taxi:
        if all_customers[0] <= all_taxi[-1]:
            popped_customer = all_customers.popleft()
            popped_taxi = all_taxi.pop()
            total_time+=popped_customer
        else:
            if all_taxi:
                all_taxi.pop()
            else:
                break
    else:
        break
if not all_customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(customer) for customer in all_customers])}')