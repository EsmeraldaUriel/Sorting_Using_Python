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


