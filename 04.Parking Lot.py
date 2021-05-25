n = int(input())

parking_lot = set()
for _ in range(n):
    command, car_number = input().split(', ')
    if command == 'IN':
        parking_lot.add(car_number)
    else:
        if car_number in parking_lot:
            parking_lot.remove(car_number)
if parking_lot:
    [print(car) for car in parking_lot]
else:
    print(f'Parking Lot is Empty')