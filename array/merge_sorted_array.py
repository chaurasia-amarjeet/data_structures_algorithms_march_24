# merged array should be sorted
# array 1 - [1, 2, 3, 5, 7, 9] i
# array 2 - [4, 6, 8, 10] j
# final array - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] k

# array 1 - [12]
# array 2 - [1 3 6 7 8 9 10]
# final array - [1 3 6 7 8 9 10 12]

def merge_sorted_array(arr1, arr2):
    length1 = len(arr1)
    length2 = len(arr2)

    merged_arr = [None] * (length1 + length2)
    print(merged_arr)

    i = 0
    j = 0
    k = 0

    while i < length1 and j < length2:

        if arr1[i] < arr2[j]:  # 2 < 1
            merged_arr[k] = arr1[i]
            i = i + 1
        else:
            merged_arr[k] = arr2[j]
            j = j + 1
        k = k + 1

    while i < length1:
        merged_arr[k] = arr1[i]
        i = i + 1
        k = k + 1

    while j < length2:
        merged_arr[k] = arr2[j]
        j = j + 1
        k = k + 1

    return merged_arr


if __name__ == '__main__':
    arr1 = [1, 3, 5, 17, 19]
    arr2 = [2, 4, 6, 8, 10]
    merged_arr = merge_sorted_array(arr1, arr2)
    print(merged_arr)
