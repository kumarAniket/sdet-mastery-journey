my_dict = {"key1":"value1","key2":"value2"}
print(my_dict['key2'])

prices_lookup={'apple':2.99,'oranges':1.99,'milk':5.80}
print(prices_lookup['milk'])

d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}
print(d['k2'])
print(d['k3']['insideKey'])
print(d['k2'][2])
print()
d = {'key1':['a','b','c']}
print(d['key1'][2].upper())

d['key1'][2] = d['key1'][2].upper()
print(d)

d = {'k1':100, 'k2':200}
d['k3']=300
print(d)

d['k1']=500
print(d)

# Grab Dictionary Keys, Values & Mappings
print(d.keys())
print()
print(d.values())
print()
print(d.items())


# Coding Challenge 7: Create a dictionary where all the keys are strings and all values are integers
print()
print("------ Dictionaries Coding Challenge ------")
myDict = {'k1':22, 'k2':2, 'k3':1998}
print(myDict)