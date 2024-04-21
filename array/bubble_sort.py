def bubble_sort(arr):
    length = len(arr)
    for i in range(0, length - 1):
        for j in range(0, length - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                # (arr[i], arr[j]) = (arr[j], arr[i])
    return arr


if __name__ == '__main__':
    arr = [5, 3, 8, 6, 7, 2]

    print("Before: ", arr)
    print("After: ", bubble_sort(arr))
