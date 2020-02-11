def sort(nums):
    for i in range(7):
        minpos = i
        for j in range(i, 8):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp


nums = [5, 2, 3, 1, 4, 6, 8, 7]

sort(nums)
