def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        print("left: ", left, "right: ", right)
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
        print(myList)


myList = [42, 82, 72, 65, 57, 60, 63, 80, 5, 1]
mergeSort(myList)
