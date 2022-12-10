# from collections import OrderedDict
# d = {'3': 3, '1': 1, '2': 2}
# print(sorted(d))
#
# names = {'zinc':32,'app':21}
# print(OrderedDict(sorted(names.items())))

B = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in B:
    for j in i:
        print(j,end=" ")
    print()

# A =[]
# row = int(input("Enter row: "))
# col = int(input("Enter column: "))
#
# for i in range(row):
#     c=[]
#     for j in range(col):
#         j = int(input("Enter value: "))
#         c.append(j)
#     B.append(c)

# for i in B:
#     for j in i:
#         print(j,end=" ")
#     print()

print("first diagonal")
for i in range(len(B)):
    for j in range(len(B[i])):
        if i==j:
            print(B[i][j],end=" ")
    print()

k=0
m=len(B)-1
print("second diagonal")
for i in range(len(B)):
    for j in range(len(B[i])):
        if i==k and j==m:
            print(B[i][j],end=" ")
            k += 1
            m -= 1
    print()

k=0
m=len(B)-1
print("second diagonal")
for i in range(len(B)):
    for j in range(len(B[i])):
        if i==k and j==m:
            print(B[i][j],end=" ")
            k += 1
    print()