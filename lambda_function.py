x = lambda a: a * 2
print(x(2))

def fun(n):
    return lambda a: a * n

a = fun(2)
print(a(2))