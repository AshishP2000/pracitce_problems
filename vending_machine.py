# vending machine
def vending_machine():
    my_list = [1000, 500, 100, 50, 10, 5, 2, 1]
    numbers = []
    cash = 10000
    count = 0
    cash1 = 0
    while cash1 != cash:
        for i in range(len(my_list)):
            cash1 += my_list[i]
            count += 1
            numbers.append(my_list[i])
            if cash1 > cash:
                cash1 -= my_list[i]
                count -= 1
                numbers.remove(my_list[i])

    print("cash needs to withdraw:", cash1)
    print("Note Count:", count)
    for i in my_list:
        print("Rs.{0}= {1}".format(i,numbers.count(i)))


if __name__ == '__main__':
    vending_machine()