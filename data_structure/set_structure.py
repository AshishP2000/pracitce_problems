set_structure = {1, 2, 3, 4, 5, 6}
print(set_structure)
set_structure.update([2, 8, 9])
print(set_structure)

set_structure.pop()
print(set_structure)

set_structure.pop()
print(set_structure)

# set operations
# set union method
A = {1, 2, 3, 4, 5}
B = {5, 6, 7, 8}
C = {10, 11, 5}
print(A | B | C)

# set intersection

print(A & B & C)

# set difference

print(A - B)
print(B - A)

# set symmetric difference

print(A ^ B)

# different set operations

for i in A:
    print(i)
