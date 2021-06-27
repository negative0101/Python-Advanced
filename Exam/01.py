from collections import deque

chocolates = deque([el for el in input().split(", ")])
cup_of_milk = deque([el for el in input().split(", ")])

milkshades = 0
is_Ready = False

while chocolates and cup_of_milk:
    current_chocolate = chocolates.pop()
    current_cup_milk = cup_of_milk.popleft()
    current_chocolate = int(current_chocolate)
    current_cup_milk = int(current_cup_milk)
    if current_chocolate <= 0 and current_cup_milk <= 0:
        continue
    if current_chocolate <= 0:
        cup_of_milk.appendleft(str(current_cup_milk))
        continue
    elif current_cup_milk <= 0:
        chocolates.append(str(current_chocolate))
        continue
    elif current_chocolate == current_cup_milk:
        milkshades += 1
    elif current_chocolate != current_cup_milk:
        cup_of_milk.append(str(current_cup_milk))
        current_chocolate -= 5
        chocolates.append(str(current_chocolate))

    if milkshades >= 5:
        is_Ready = True
        break

if is_Ready:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(chocolates)}")
else:
    print("Chocolate: empty")
if cup_of_milk:
    print(f"Milk: {', '.join(cup_of_milk)}")
else:
    print("Milk: empty")
