queue = []
def enqueue(value):
    queue.append(value)
    print("element added")

def dequeue():
    queue.pop(0)
    print("element removed")

def display():
    print(queue)


if __name__ == '__main__':
    while True:
        choice = int(input("Enter choice 1.enqueue 2.dequeue 3.display queue 4.quit: "))
        if choice == 1:
            num = int(input("Enter number you want to push: "))
            enqueue(value=num)
        elif choice == 2:
            dequeue()
        elif choice == 3:
            display()
        elif choice == 4:
            break
        else:
            print("Enter the current operation")