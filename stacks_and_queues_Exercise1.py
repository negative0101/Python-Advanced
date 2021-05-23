# Write a program that reads from the console a string with N integers, separated by a single space, and reverses them using a stack.  #
# Print the reversed integers on one line, separated by a single space. #
stack = [ ]
nums = input().split()
for i in range(len(nums)):
    popped_num = nums.pop()
    stack.append(int(popped_num))
print(*stack)