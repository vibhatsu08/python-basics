# Reverse words in a given string
# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

def reverseWords (S) :
    strArr = S.split(".")
    newStr = []
    for i in range (len(strArr), 0, -1) :
        newStr.append(strArr[i-1])
    return ".".join(newStr)
        
    
print(reverseWords(S="i.like.this.program.very.much"))