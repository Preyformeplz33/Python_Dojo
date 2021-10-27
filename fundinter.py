x = [ [ 5,2,3], [10,8,9]]
students = [
    {'first_name': 'Micheal', 'last_name' : 'Jordan'},
    {' first_name' : 'John', 'last_name'  : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo','Rooney']
}
z = [ {'x': 10,'y': 20} ]

# # TODO: <not a function just to mark comments? Change the value 10 in x to 15. Once your done , x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# print(x)
# # TODO:Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]['last_name']='Bryant'
# print(students)
# #in a []<list the the zero index selets the first curly brack so the 1st index would be the second
# TODO In the sports_directory, change 'Messi to 'Andres'
# sports_directory['soccer'][0] = 'Andres'
# print ( sports_directory['soccer'])
# #in a dictonary we choose the key then the index?
#TODO change the value 20 in z to 30
#z a list we choose the first curly with an index 0 and call the key y and change it to 30?
# z[0]['y'] = 30
# print(z)

#! Iterate Through a List of Dictionaries
# # # TODO: Create a Function iterateDictionary(some_list) that ,given a list of dictionaries the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
# students = [
#         {'first_name': 'Micheal', 'last_name': 'Jordan'},{'first_name':'John','last_name': 'Rosales'},
#         {'first_name':'Mark','last_name':'Guillen'},
#         {'first_name':'KB','last_name': 'Tonel'},
# ]

# def iterate_dictionary(list):
#     for m in range(0,len(list)):   #<  this functinon loops thrugh the length of teh list
#         output = '' # what does this do?
#         for key , val in list [m].items():
#             #
#             output += f'{key} - {val},'
#         print(output)
# iterate_dictionary(students)

# Get values from a list of dictionaries
#TODO:Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# def iterate_Dictionary2(key_name,some_list):
#     for m in range(0, len(some_list)):
#         for key,val in some_list[m].items():
#             if key == key_name:
#                 print(val)
# iterate_Dictionary2('first_name',students)
# #TODO: and iteratedictionary2('last_name',students) should output:
# #JOrdan
# #rosales
# #Guillen
# #tonel
# iterate_Dictionary2('last_name',students)

# TODO:create a function printinfo(some_dict)given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
# dojo = {#<dictonary curly 
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def print_info(dict):
#     for key,val in dict.items():
#         print('')
#         print(f'{len(val)} {key.upper()}')
#         for i in range(0, len(val)):
#             print(val[i])
# print_info(dojo)