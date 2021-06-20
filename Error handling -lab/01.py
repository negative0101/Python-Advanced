text = input()

number = input()
try:
    number = int(number)

except ValueError:
    print('Variable times must be an integer')
print(text * number)