[1, 100000000, 1]

O(n) - max

[0, 1, 1, 2, 1, 2, 0, 1] - O(n)

O(maxElement)



def partition(arr, p, r):
    # [5, 1, 8, 6, 7, 2, 3]
    pivot = arr[r]  # 3
    i = p - 1  #-1

    for j in range(p, r):
        if arr[j] <= pivot:
            i = i + 1 #0
            (arr[i], arr[j]) = (arr[j], arr[i])  # [1, 5, 8, 6, 7, 2, 3]
    (arr[i + 1], arr[r]) = (arr[r], arr[i + 1])  # [1, 2, 3, 6, 7, 5, 8]
    return i + 1  # 1


def quick_sort(arr, p, r):
    if p < r:
        pivot = partition(arr, p, r)
        quick_sort(arr, p, pivot - 1)
        quick_sort(arr, pivot + 1, r)


if __name__ == '__main__':
    arr = [5, 1, 8, 6, 7, 2]
    print("Before: ", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("After: ", arr)
