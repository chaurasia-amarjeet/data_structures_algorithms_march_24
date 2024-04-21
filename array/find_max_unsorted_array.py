# finding mix in array

def max(arr):
    max = -10000
    length = len(arr)

    for i in range(0, length):
        if max < arr[i]:
            max = arr[i]

    return max

if __name__ == '__main__':
    arr = [3, 5, 2, 4, 10, 0]
    print("Maximum:", max(arr))
