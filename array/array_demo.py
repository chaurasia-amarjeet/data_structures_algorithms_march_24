def array_demo():
    arr = [3, 5, 2, 4, 1]
    print(arr)
    print(arr[0])
    print(arr[1])
    print(arr[2])
    print("Length:", len(arr))
    arr[1] = 9
    print(arr)

    length = len(arr)
    for i in range(0, length):
        print(arr[i])


if __name__ == '__main__':
    array_demo()
