def merge(arr, p, q, r):
    # p=0, q=2, r=4
    n1 = q - p + 1
    n2 = r - q

    # create temp arrays
    L = [None] * (n1)
    R = [None] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[p + i]

    for j in range(0, n2):
        R[j] = arr[q + 1 + j]

    #Initialize indexes
    i = 0
    j = 0
    k = p

    # Merge the 2 sorted arrays
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[]
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[]
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, p, r):
    if p < r:
        q = p + (r - p) // 2

        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    print("Before:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("After:", arr)
