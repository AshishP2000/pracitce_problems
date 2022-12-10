list_structure = [1, 2, 3.3]
# print(list_structure)
# print(list_structure[-4])
# print(list_structure[:])
# print(list_structure[2:])
# print(list_structure[:2])
# print(list_structure[2:4])
multi_dimantional = [[1,2,3],[4,5,6]]
for i in multi_dimantional:
    for j in i:
        print(j,end=" ")
    print()

# del list_structure[1]
# print(list_structure)
# list_structure.append(5)
# list_structure.extend([7,8,9])
# print(list_structure)
# list_structure.insert(1,78)
# print(list_structure)
# list_structure.reverse()
# print(list_structure)
# list_structure.remove('ed')
# print(list_structure)


l = [i for i in list_structure if 2 in list_structure]
print(l)
