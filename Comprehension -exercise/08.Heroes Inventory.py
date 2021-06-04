heroes = input().split(', ')

command = input()
inventory = {hero:{} for hero in heroes}
while not command == 'End':
    name, item, gold = command.split('-')
    if item not in inventory[name]:
            inventory[name][item]= int(gold)

    command = input()

for hero in heroes:
    cost = sum(inventory[hero].values())
    item_count= len(inventory[hero])
    print(f'{hero} -> Items: {item_count}, Cost: {cost}')