n = int(input())
stack = []
for i in range(n):
    command = input()
    if command.startswith('1'):
        num_in_command = int(((command.split()[-1])))
        stack.append(num_in_command)
    elif command == '2':
        if stack:
            stack.pop()
    elif command == '3':
        if stack:
            print(max(stack))
    elif command == '4':
        if stack:
            print(min(stack))
reversed_stack = []
for j in range (len(stack)):
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))