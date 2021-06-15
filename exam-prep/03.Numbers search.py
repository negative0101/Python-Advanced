def numbers_searching(*nums):
    lowest = 100000000000000000000
    highest = 0
    duplicates = []
    missing_number = []
    for i in range(len(nums)):
        if nums.count(nums[i]) >1 and (nums[i] not in duplicates):
            duplicates.append(nums[i])
        if nums[i] < lowest:
            lowest = nums[i]
        if nums[i] > highest:
            highest = nums[i]
    for j in range(lowest,highest):
        if j not in nums:
            missing_number.append(j)
            break
    missing_number.append(sorted(duplicates))
    return missing_number
