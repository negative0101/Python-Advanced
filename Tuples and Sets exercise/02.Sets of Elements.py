x,y = input().split()
set_x = set()
set_y = set()
for i in range(int(x)+int(y)):
    element = input()
    if i < int(x) :
        set_x.add(int(element))
    else:
        set_y.add(int(element))
intersection = set_x.intersection(set_y)
for j in intersection:
    print(j)