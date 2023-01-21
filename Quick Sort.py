def quickSort(array, left, right):
    if left < right:
        pi = partition(array, left, right)

        quickSort(array, left, pi - 1)
        quickSort(array, pi + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    print("Pivot: ", pivot)





