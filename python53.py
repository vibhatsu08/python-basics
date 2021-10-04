#python program to merge two dictionaries
#first method by using the | operator
dict1 = {1:"one", 2:"two"}
dict2 = {3:"three", 4:"four"}
new_dict = dict1 | dict2
print(new_dict)

#second method, by using the ** operator
new_dict = {**dict1, **dict2}
print(new_dict)



