def quickSort(array, left, right):
    if left < right:
        pi = partition(array, left, right)

        quickSort(array, left, pi - 1)
        quickSort(array, pi + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        print(arr)
    return i


data = [42, 82, 72, 65, 57, 60, 63, 80, 5, 1]
print(data)
quickSort(data, 0, len(data) - 1)
