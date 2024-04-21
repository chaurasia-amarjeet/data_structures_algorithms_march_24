def binary_search(arr, start, end, target):
    if start > end:
        return False

    mid = start + (end - start) // 2
    if arr[mid] == target:
        return True
    elif target > arr[mid]:
        return binary_search(arr, mid + 1, end, target)
    else:
        return binary_search(arr, start, mid - 1, target)

def binary_search_itr(arr, start, end, target):
    while(start <= end):
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return True
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return False


#recursive -> iterative

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(binary_search(arr, 0, 4, 1))
    print(binary_search(arr, 0, 4, 0))
