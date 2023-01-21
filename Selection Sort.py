def sort(nums):

    for i in range(8):
        minpos = i
        for j in range (i,10):
            if nums[j] < nums[minpos]:
                minpos = j
