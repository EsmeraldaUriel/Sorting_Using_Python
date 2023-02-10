def sort(nums):

    for i in range(9):
        minpos = i
        for j in range (i,10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)


nums = [42, 82, 72, 65, 57, 60, 63, 80, 5, 1]
sort(nums)

print(nums)