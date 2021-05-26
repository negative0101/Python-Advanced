phone_book = {}
user_number = input()

while not user_number.isdigit():
    user_number=user_number .split('-')
    user,number = user_number
    if user not in phone_book:
        phone_book[user] = 0
    phone_book[user] = number
    user_number = input()

else:
    for i in range(int(user_number)):
        user_calling = input()
        if user_calling in phone_book:
            print(f'{user_calling} -> {phone_book[user_calling]}')
        else:
            print(f'Contact {user_calling} does not exist.')
