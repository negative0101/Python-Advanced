parentheses = input()
balanced = True
stack = []
for i in parentheses:
    if i in '[{(':
        stack.append(i)
    elif i in ']})':
        if len(stack) == 0:
            balanced = False
            break
        opening_paren = stack.pop()

        if f'{opening_paren}{i}' not in ['[]','()','{}']:
            balanced = False
            break
if balanced and len(stack) == 0:
    print('YES')
else:
    print(f'NO')