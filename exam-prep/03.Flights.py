def flights(*args):
    dictionary = {}
    args = list(args)
    cities = []
    nums = []
    for i in range(len(args)):
        if str(args[i]).isalpha():
            cities.append(args[i])
        elif str(args[i]).isnumeric():
            nums.append((args[i]))
        else:
            cities.append(args[i])

    for i in range(len(cities)):
        if cities[i] == 'Finish':
            break
        if cities[i] not in dictionary:
            dictionary[cities[i]] = 0
        dictionary[cities[i]] += nums[i]

    return dictionary


print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))