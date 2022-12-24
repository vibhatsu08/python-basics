# Palindrome String
# Given a string S, check if it is palindrome or not.

def isPalindrome (S) :
    reverseStr = ""
    for i in range(len(S), 0, -1) :
        reverseStr += S[i-1]
    if reverseStr == S :
        return 1
    else :
        return 0
print(isPalindrome(S="abba"))