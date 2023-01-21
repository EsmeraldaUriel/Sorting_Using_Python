def InsertionSort(array):
    for a in range(1, len(array)):
        b = a
        while b > 0 and array[b] < array[b - 1]:
            array[b - 1], array[b] = array[b], array[b-1]
            b -= 1
            print(array)


array = [42, 82, 72, 65, 57, 60, 63, 80, 5, 1]
print(array)
InsertionSort(array)
