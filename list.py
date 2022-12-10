a=[1,2,4,5,6,9,12]
max_number = max(a)
for i in range(1,max_number+1):
    if i not in a:
        print(i)

b = list("Hello")

print("".join(b))

print(bin(25))


# def add(*args):
#     for i,j in enumerate(args):
#         print(i+j)
#
# add(1,2,3,4)
# for i in enumerate(a):
#     print(i)

# my_str = "Hello"
# my_str1 = "World"
#
# my_list =[my_str,my_str1]
# my_str2 = " ".join(my_list)
# print(type(my_str2))

my_list = [[1],[2],[3],[4,5]]
flat_list = []
for i in my_list:
    for j in i:
        print(j)

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()




