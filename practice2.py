
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

"""map function"""
import functools
import operator

my_list = [1,2,3,4,5,6]
def add(num):
    return num*5

x = list(map(add,my_list))
print(x)

"""reduce function"""
print(functools.reduce(operator.add,my_list))

"""filter function"""

def filter_data(x):
    if x > 5:
        return x

result = filter(filter_data,my_list)
print(list(result))