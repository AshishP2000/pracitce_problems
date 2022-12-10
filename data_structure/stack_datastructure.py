stack = []
def push(value):
    stack.append(value)
    print("pushed")

def pop():
    stack.pop()
    print("popped")

def display():
    print(stack)


if __name__ == '__main__':
    while True:
        choice = int(input("Enter choice 1.push 2.pop 3.display stack 4.quit: "))
        if choice == 1:
            num = int(input("Enter number you want to push: "))
            push(value=num)
        elif choice == 2:
            pop()
        elif choice == 3:
            display()
        elif choice == 4:
            break
        else:
            print("Enter the current operation")