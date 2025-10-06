mylist = [1,2,3,4,5,6,7,8,9,10]

for jelly in mylist:
    print("hello")
print()
for num in mylist:
    if num%2==0:
        print(num)
    else:
        print(f"Odd Number >> {num}")

print()
list_sum = 0
for num in mylist:
    list_sum += num
print("List Sum >> {}".format(list_sum))

print()
for _ in "Hello World":
    print('hello')

print()
tup=(1,2,3)

for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8),(9,10)]
print(len(mylist))
print()
for a,b in mylist:
    print(b)
print()
mylist = [(1,2,3),(5,6,7),(8,9,10)]
for (a,b,c) in mylist:
    print(b)
print()
myDict = {"k1":1,"k2":2,"k3":3}
for value in myDict.values():
    print(value)