def simple_intrest(p, r, t):
    r = r/100
    return p*(1+(r*t))

def compound_intrest(p, r, t):
    #r = r/100
    return p*(1+(r/100))**t


if __name__ == '__main__':
    number1 = float(input("Enter Initial principle balance: "))
    number2 = float(input("Enter annual interest rate: "))
    number3 = float(input("Enter number of time in years: "))

    print(simple_intrest(p=number1, r=number2, t=number3))
    print(compound_intrest(p=number1, r=number2, t=number3))
