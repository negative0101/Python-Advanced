n = int(input())
names = {}
for _ in range(n):
    name, grade = input().split()
    if name not in names:
        names[name] = [float(grade)]
    else:
        names[name].append(float(grade))
for key, value in names.items():
    marks = ' '.join(map(lambda f: f"{f:.2f}", value))
    print(f"{key} -> {marks} (avg: {sum(value) / len(value):.2f})")