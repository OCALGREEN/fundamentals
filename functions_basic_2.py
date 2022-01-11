# Countdown
def countdown(num):
    new_list = []
    for x in range(num, -1, -1):
        new_list.append(x)
    return new_list

print("Countdown")
print(countdown(5))


# Print and Return
def print_and_return(arg):
    print(arg[0])
    return arg[1]

print("Print and Return")
another_list = [1, 2]
print(print_and_return(another_list))


# First Plus Length
def first_plus_length(simple):
    return simple[0] + len(simple)

print("First Plus Length")
and_list = [1, 2, 3, 4, 5]
print(first_plus_length(and_list))

# Values Greater than Second
def values_greater_than_second(example4b):
    example4c = []
    if len(example4b) < 2:
        return False
    else: 
        for x in range(len(example4b)):
            if x > example4b[1]:
                example4c.append(x)
        print(len(example4c))
        return example4c

print("Values Greater than Second")
example4a = [5, 2, 3, 2, 1, 4]
print(values_greater_than_second(example4a))

# This Length, Than Value
def this_length_that_value(size, value):
    a = []
    for x in range(size):
        a.append(value)
    return a

print("This Length That Value")
print(this_length_that_value(6, 2))
