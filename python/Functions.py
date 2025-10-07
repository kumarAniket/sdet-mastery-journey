from random import shuffle


def say_hello():
    print("Hello")
    print("How")
    print("Are")
    print("You")


say_hello()

print()


# Function with input parameter
def print_my_name(name):
    """Method to take a name and print it in console as Hello {name}!!"""
    print(f"Hello {name}!!")


print_my_name("Golu")


def add_num(num1, num2):
    return num1 + num2


result = add_num(1, 2)
print("Returned Value >> {}".format(result))
print()


# Logic with functions
def check_even(num):
    return num % 2 == 0


print(check_even(20))
print(check_even(21))


def check_even_list(my_list):
    even_number_list = []
    for num in my_list:
        if num % 2 == 0:
            even_number_list.append(num)
        else:
            pass
    return sorted(even_number_list)


print(check_even_list([1, 3, 5, 7, 4, 8, 11, 2]))

# Tuple Unpacking
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for ticker, price in stock_prices:
    print(price + (price * 0.1))
print()
work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for name, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = name
        else:
            pass
    return current_max, employee_of_month


hours, name = employee_check(work_hours)
print(f"Employee Name >> {name}, Hours >> {hours}")
print()

# Interactions b/w functions challenge
# game_list = ['o',' ',' ']
#
# def shuffle_my_list(my_list):
#     shuffle(my_list)
#
#     return my_list
#
# def user_guess():
#     guess=''
#     while guess not in ['0','1','2']:
#         guess = input("Guess a number from 0 to 2 or 'q' to quit: ")
#     return int(guess)
#
# def player_game(final_list,guess_final):
#     shuffle_my_list(final_list)
#
#     if final_list[guess_final] == 'o':
#         print("Correct Guess!!!")
#         print(final_list)
#     else:
#         print("Incorrect Guess!!!")
#         print(final_list)
#
# player_game(game_list,user_guess())


# Functions Coding Challenge : Functions#1: print Hello World
print()
print("------ Functions#1: print Hello World ------")


def myfunc():
    print("Hello World")


myfunc()

print()
print("------ Functions#2: print Hello Name ------")


def myfunc(name):
    print(f"Hello {name}")


myfunc("Aniket")

print()
print("------ Functions#3: simple Boolean ------")


def myfunc(boolean_check):
    if boolean_check:
        return "Hello"
    else:
        return "Goodbye"


print(myfunc(True))
print(myfunc(False))

print()
print("------ Functions#4: using Booleans ------")


def myfunc(x, y, z):
    return x if z else y


print(myfunc('a', 'b', True))

print()
print("------ Functions#5: simple math ------")


def myfunc(num1, num2):
    return num1 + num2


print(myfunc(12, 24))

print()
print("------ Functions#6: is even ------")


def is_even(check_even_num):
    return check_even_num % 2 == 0


print(is_even(5))

print()
print("------ Functions#7: is greater ------")


def is_greater(num1, num2):
    return True if num1 > num2 else False


print(is_greater(12, 5))
print(is_greater(11, 11))
print(is_greater(7, 24))

print()


# *args and **kwargs Keywords

# *args keyword is used to take arbitrary no. of parameters
def myfunc(*args):
    return (sum(args)) * 0.05


print("*args output >> {}".format(myfunc(40, 20, 100, 90, 80.50, 200.13)))
print()


def myfunc_iterator(*args):
    for item in args:
        print("Tuple Item >> {}".format(item))


myfunc_iterator(40, 60, 1.34, 5000, 20, 20.625, 2.314514)
print()


# **kwargs keyword is used to take arbitrary no. of keyworded parameters
def myfunc_keyargs(**kwargs):
    if 'fruit' in kwargs:
        print("My fruit choice is {}".format(kwargs['fruit']))
    else:
        print("Fruit not found")


myfunc_keyargs(fruit="Apple", veggie='Lettuce')


def myfunc(*args, **kwargs):
    print("I would like {} hot{}s".format(args[0], kwargs['animal']))


myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')

print()
print("------ Functions#8: *args ------")


def myfunc_sum(*args):
    total_sum = 0
    for item in args:
        total_sum += item
    return total_sum


print("Total Sum >> {}".format(myfunc_sum(10, 70.5, 800.8764)))

print()
print("------ Functions#9: pick evens ------")


def myfunc_is_even(*args):
    even_list = [item for item in args if item % 2 == 0]
    return even_list


print("Even List >> {}".format(myfunc_is_even(5, 6, 7, 8)))

print()
print("------ Functions#10: skyline ------")


def myfunc_skyline(skyline_string):
    new_string=''
    for index in range(0, len(skyline_string)):
        if index%2==0:
            new_string+=skyline_string[index].upper()
        else:
            new_string += skyline_string[index].lower()

    return new_string


print(myfunc_skyline('Anthropomorphism'))
