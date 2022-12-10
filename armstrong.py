def armstrong(arm):
    s = 0
    num = arm
    while arm > 0:
        add = arm % 10
        s += add ** 3
        arm = int(arm/10)
    if s == num:
        print(number,"is Armstrong number")
    else:
        print(number,"is not Armstrong number")


if __name__ == '__main__':
    number = int(input("Enter number to check armstrong number: "))
    armstrong(arm=number)