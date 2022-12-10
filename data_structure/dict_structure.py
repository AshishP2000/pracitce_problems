dict_structure = {'1': 2, 3: 4}
print(dict_structure.items())
print(dict_structure['1'])
print(dict_structure[3])
print(dict_structure.get('1'))

dict_structure['1'] = 8
print(dict_structure)

dict_structure['5'] = 10
print(dict_structure)

dict_structure['5'] = 11
print(dict_structure)

dict_structure.pop('5')
print(dict_structure)

dict_structure.popitem()
print(dict_structure)

# dict comprehension

my_dict = {x: x*x for x in range(1,11)}
print(my_dict)

my_dict = all(dict_structure)
print(my_dict)

my_dict = any(dict_structure)
print(my_dict)
