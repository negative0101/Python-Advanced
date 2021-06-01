#n = int(input())
#nums = []
#for _ in range(n):
#    nums.extend(int(i) for i in input().split(', '))
#print(nums)



n = int(input())

matrix = [[int(i) for i in input().split(', ')] for _ in range(n)]
flatt_nums =[num for sublist in matrix for num in sublist]
print(flatt_nums)