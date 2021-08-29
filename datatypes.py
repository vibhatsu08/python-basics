#python data types
#python numbers
a = 10
print(type(a))

#list in python
listType = ["peter", "spiderman", 19, "superhero"]
print(listType[2])
listType[2] = "ironman"
print(listType)

#tuples in python
tupleType = (1, "program", "hello world", "awesome")
#tuples unlike lists are immutable
print(tupleType)

#strings in python
stringType = "this is a single line string!"
print(stringType)
multiLineStringType = """This is a multi
line string"""
print(multiLineStringType)
#strings also are immutable

#sets in python
#sets eliminate duplicate elements when used
setType = {1,2,2,2,3,4,5,5,6}
print(setType); #prints the set as {1,2,3,4,5,6}

#python dictionary, a collection or ordered key value pairs
dictionaryType = {2: "value", "hello": 1}
print("dictionaryType[2]: ", dictionaryType[2])
print("dictionaryType[2]: ", dictionaryType['hello'])
