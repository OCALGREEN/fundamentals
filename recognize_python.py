num1 = 42               # variable declaration Numbers
num2 = 2.3              # variable declaration Numbers
boolean = True          # variable declaration Boolean
string = 'Hello World'  # variable declaration Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']          # variable declaration List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # variable declaration Dictionary
fruit = ('blueberry', 'strawberry', 'banana')                                       # variable declaration Tuple
print(type(fruit))                      # type check
print(pizza_toppings[1])                # list access value
pizza_toppings.append('Mushrooms')      # list add value
print(person['name'])                   # dictionary access value
person['name'] = 'George'               # dictionary change value
person['eye_color'] = 'blue'            # dictionary add value
print(fruit[2])                         # tuple access value

if num1 > 45:                       # conditional if statement
    print("It's greater")
else:                               # conditional else statement
    print("It's lower")

if len(string) < 5:                 # length check
    print("It's a short word!")
elif len(string) > 15:              # length check
    print("It's a long word!")
else:                               # length check
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()        # list delete value
pizza_toppings.pop(1)       # list delete value

print(person)               # dictionary access value
person.pop('eye_color')     # dictionary delete value
print(person)               # dictionary access value

for topping in pizza_toppings:          # for loop start
    if topping == 'Pepperoni':          # conditional if
        continue
    print('After 1st if statement')     # debugging
    if topping == 'Olives':             # conditional if
        break                           # for loop end

def print_hello_ten_times():            # function
    for num in range(10):               # for loop start
        print('Hello')

print_hello_ten_times()                 # function call

def print_hello_x_times(x):             # function(parameter)
    for num in range(x):                # for loop start
        print('Hello')

print_hello_x_times(4)                  # function(argument)

def print_hello_x_or_ten_times(x = 10): # function(parameter = argument)
    for num in range(x):                # for loop start
        print('Hello')

print_hello_x_or_ten_times()            # function call
print_hello_x_or_ten_times(4)           # function(argument)


"""
Bonus section
"""

# print(num3)                       NameError: name <variable name> is not defined
# num3 = 72                         variable declaration
# fruit[0] = 'cranberry'            TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])    KeyError: 'favorite_team'
# print(pizza_toppings[7])          IndexError: list index out of range
#   print(boolean)                  IndentationError: unexpected indent
# fruit.append('raspberry')         AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                      AttributeError: 'tuple' object has no attribute 'pop'