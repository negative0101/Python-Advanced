number_of_clothes = input().split()
capacity_of_rack = int(input())

num_racks = 1
current_rack = 0
for i in range(len(number_of_clothes)):
    popped_cloth =int(number_of_clothes.pop())
    if popped_cloth + current_rack > capacity_of_rack:
        num_racks += 1
        current_rack= 0
    current_rack += int(popped_cloth)

print(num_racks)