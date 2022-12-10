def search(num):
    arr = [1, 2, 35, 34, 56, 119, 76, 890]
    for i in range(len(arr)):
        if num == arr[i]:
            print(num, "is present at:", i + 1)
            return i+1
    print(num,"is not present")
    return -1


if __name__ == '__main__':
    num = int(input("Enter number you want to search: "))
    search(num=num)
