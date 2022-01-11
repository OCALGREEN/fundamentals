# 1. Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# students[0]['last_name'] = 'Bryant'
# sports_directory['soccer'][0] = 'Andres'
# z[0]['y'] = 30










# 2. Iterate Through a List of Dictionaries
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(some_list):
#     key_list = []
#     value_list = []
#     count = 0

#     for k in some_list:
#         key_list += some_list[count]
#         value_list += some_list[count].values()
#         count += 1

#     jump = 0
#     for x in key_list:
#         print(key_list[jump], "-", value_list[jump])
#         jump += 1

# print(iterateDictionary(students))










# 3. Get Values from a List of Dictionaries
# def iterateDictionary2(key_name, some_list):
#     count = 0

#     for x in range(len(some_list)):
#         print(some_list[count][key_name])
#         count += 1

# print(iterateDictionary2("first_name", students))
# print(iterateDictionary2("last_name", students))










# 4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):

    list_of_keys = []
    for x in some_dict:
        list_of_keys.append(x)

    size_of = []
    for m in some_dict:
        size_of.append(len(some_dict[m]))

    count = 0
    for k in some_dict:
        jump = 0
        print(len(some_dict[list_of_keys[count]]), " ", list_of_keys[count].upper())
        for j in range(size_of[count]):
            print(some_dict[list_of_keys[count]][jump])
            jump+=1
        count+=1

printInfo(dojo)
