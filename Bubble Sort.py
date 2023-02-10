def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)


elements = [42, 82, 72, 65, 57, 60, 63, 80, 5, 1]
bubbleSort(elements)

print("Sorted Array:")
print(elements)

