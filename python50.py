#python program to replace punctuations in the string
def remove_puncs(new_string):
    punctuations = "!@#$%^&*(){[],}.<>/:'/?|\;:'"
    
    for i in new_string:
        if i in punctuations:
            new_string = new_string.replace(i, "")
    print(new_string)

string = input()
remove_puncs(string)

