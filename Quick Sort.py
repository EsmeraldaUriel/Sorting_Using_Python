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

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
            print("i", i, "arr[i]", arr[i])
        while j > left and arr[j] >= pivot:
            j -= 1
            print("j", j, "arr[j]", arr[j])
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)



