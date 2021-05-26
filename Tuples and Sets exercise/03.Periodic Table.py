n = int(input())
set_ = set()
for i in range(n):
    element = input().split()
    for j in element:
        set_.add(j)
for k in set_ :
    print(k)