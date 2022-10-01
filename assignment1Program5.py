# Write a python program to create dictionary using elements of two lists.\
# list of keys
list_keys = ["apple", "banana", "oranges"]
# list of values
list_values = [2, 3, 4]

# empty dictionary
list_dict = {}

# first loop to iterate over the keys in the list_keys list
for key in list_keys :
    # second loop to iterate over the values in the list_values list
    for value in list_values :
        # adding the value to it's key
        list_dict[key] = value
        # removing the current value to enable the iteration to reach the other values
        list_values.remove(value)
        break

# printing the final list_dict dictionary
print(str(list_dict))