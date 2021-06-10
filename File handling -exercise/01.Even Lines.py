import re

with open('01.input.txt') as file:
    lines = file.readlines()
    for idx, line in enumerate(lines):
        if idx % 2 != 0:
            continue
        line = re.sub(r'[-,.!?]', '@', line)
        line = ' '.join(reversed(line.split()))

        print(line.strip())

