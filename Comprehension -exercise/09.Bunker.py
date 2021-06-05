categories = input().split(', ')

n = int(input())

bunker = {category: [] for category in categories}
for _ in range(n):
    category, item_name, quantity_quality = input().split(' - ')
    quantity, quality = quantity_quality.split(';')
    quantity, quality = quantity.split(':')[1], quality.split(':')[1]
    quantity, quality = int(quantity), int(quality)

    bunker[category].append({
        'name': item_name,
        'quality': quality,
        'quantity': quantity
    })
total_items = sum([item['quantity']for items in bunker.values() for item in items])
average_quality = sum([item['quality']for items in bunker.values() for item in items])
average_quality /= len(categories)

print(f'Count of items: {total_items}')
print(f'Average quality: {average_quality:.2f}')

print('\n'.join(
    f'{category} -> {", ".join(item["name"]for item in bunker[category])}'
    for category in categories
))