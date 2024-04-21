# finding min in array
# what's max size of array
# what would be value of each element- 0 < 100
# min = 100
def min(arr):
    min = 10000
    length = len(arr)

    for i in range(0, length):
        if min > arr[i]:
            min = arr[i]

    return min

if __name__ == '__main__':
    arr = [3, 5, 2, 4, 10, 0]
    print("Minimum:", min(arr))
