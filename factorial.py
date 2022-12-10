def factorial(input_number):
    try:
        fact = 1
        for i in range(1,input_number+1):
            fact *= i
        print(fact)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    number = int(input("Enter number to find the factorial: "))
    factorial(input_number=number)