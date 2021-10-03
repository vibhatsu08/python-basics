#python program to reverse a string
def reverse_string(s):
    if len(s) == 1:
        return s
    else:
        string_new = ""
        for i in s:
            string_new = i + string_new
        return string_new
string = input()
print(reverse_string(string))