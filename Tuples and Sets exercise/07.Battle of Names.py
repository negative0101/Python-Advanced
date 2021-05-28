n = int(input())

odd_numbers, even_numbers = set(), set()
for i in range(n):
    name = input()

    ascii_sum = 0
    for letter in name:
        ascii_sum += ord(letter)
    ascii_sum = ascii_sum // (i + 1)

    if ascii_sum % 2 == 0:
        even_numbers.add(ascii_sum)
    else:
        odd_numbers.add((ascii_sum))
even_sum =sum(even_numbers)
odd_sum = sum(odd_numbers)


if even_sum == odd_sum:
    result = odd_numbers.union(even_numbers)
elif even_sum > odd_sum:
    result = odd_numbers.symmetric_difference(even_numbers)
elif odd_sum > even_sum:
    result = odd_numbers.difference(even_numbers)

print(', '.join([str(x) for x in result]))
