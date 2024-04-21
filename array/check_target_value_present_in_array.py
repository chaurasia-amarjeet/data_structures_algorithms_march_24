def search(arr, target):
    length = len(arr)
    for i in range(0, length):
        if arr[i] == target:
            return True
    return False


if __name__ == '__main__':
    arr = [3, 5, 2, 4, 10, 0]
    print(search(arr, 5))
    print(search(arr, 8))