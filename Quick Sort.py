def quickSort(array, left, right):
    if left < right:
        pi = partition(array, left, right)

        quickSort(array, left, pi - 1)
        quickSort(array, pi + 1, right)






