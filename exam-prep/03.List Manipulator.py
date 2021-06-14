def list_manipulator(list_of_nums, add_remove='', beginning_end='', *args):
    nums = [int(i) for i in list_of_nums]
    if add_remove:
        if add_remove == 'add' and beginning_end == 'beginning':
            temp_list = []
            for i in range(len(args)):
                temp_list.append(args[i])
            return temp_list + nums
        elif add_remove == 'add' and beginning_end == 'end':
            for i in range(len(args)):
                nums.append(args[i])
            return nums
        elif add_remove == 'remove' and beginning_end == 'beginning':
            if args:
                arg = int(*args)
                new_list = nums[arg:]
                return new_list
            else:
                new_list = nums[1:]
                return new_list
        elif add_remove == 'remove' and beginning_end == 'end':
            if args:
                arg = int(*args)
                for i in range(arg):
                    nums.pop()
                return nums
            else:
                nums.pop()
                return nums


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
