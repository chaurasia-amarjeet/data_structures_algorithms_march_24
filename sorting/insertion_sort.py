def insertion_sort(array):
    n = len(array)

    if n <= 1:
        return

    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    print("Before:", arr)
    insertion_sort(arr)
    print("After:", arr)
