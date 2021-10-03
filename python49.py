#python program to check if a string is a palindrome or not
def palindrome_string(s):
    if len(s) <= 1:
        print(s)
    else:
        new_string = ""
        for i in s:
            new_string = i + new_string
        print(new_string)
        
        if new_string == s:
            print("palindrome")
        else:
            print("not palindrome")
    
string = input()
palindrome_string(string)