#A set is collection which is unordered, unchangable and unindexed
#duplicates are not allowed in set

numbers = {2,3,1,5,6,2,0} #created set
print(numbers)

numbers.add(12) #added elements
numbers.add("b")
numbers.add("a")
numbers.add(10)
print(numbers)

#we can use remove method but
# key error can generate if element is not present
numbers.remove(10)
print(numbers)

#we can use remove method but
# key error will not generate if element is not present
numbers.discard(10)
print(numbers)

#remove any random element
numbers.pop()
print(numbers)

#use update add more than one element
numbers.update([20,30])
print(numbers)

#clear the set
numbers.clear()
print(numbers)


A = {1,2,3,4,5}
B = {5,6,7,8,9}

#Union of set
C = A | B
print("Union:",C)

#Intersection of set
C = A & B
print("Intersection:",C)

#Difference of set
C = A - B
print("Difference:",C)

#Symmetric difference
C = A ^ B
print("Symmetric difference:",C)