my_new_list = ['apple',2,300.2]

print(len(my_new_list))

my_list = ['one','two','three']
print(my_list[0])
print(my_list[1:])

another_list = ['four', 'five']
updatedList = my_list + another_list
print(updatedList)
print()
my_list[0]='ONE ALL CAPS'
print(my_list)

updatedList.append('six')
print(updatedList)

updatedList.append('seven')
print(updatedList)

updatedList.pop()
print(updatedList)

popped_item = updatedList.pop(3)
print("Popped >> {}".format(popped_item))
print("Updated List >> {}".format(updatedList))

new_list = ['a','e','x','b','c']
num_list = [4,1,8,3,5]
print(new_list)
new_list.sort()
my_sorted_list = new_list
print(my_sorted_list)
print()
print(num_list)
num_list.sort()
print(num_list)
print()
print(num_list)
num_list.reverse()
print(num_list)

# Coding Challenge 6: Create a list containing at least one string, one integer and one float
print()
print("------ Lists Coding Challenge ------")
coding_list = [200,55,65]
print("Org. List >> {}".format(coding_list))
print(f"Length of list >> {len(coding_list)}")
print()
coding_list.sort()
coding_list_sorted = coding_list
print(f"Sorted Org. List >> {coding_list_sorted}")
coding_list.append(56)
coding_list.pop(2)
print(f"Modified Org. List (Append & Pop) >> {coding_list}")
coding_list.reverse()
print(f"Reversed List >> {coding_list}")