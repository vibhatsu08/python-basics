# Remove vowels from string
# Given a string, remove the vowels from the string.

def removeVowels (S) :
    newString = ""
    for i in range (len(S)) :
        if (S[i] != 'a' and S[i] != 'e' and S[i] != 'i' and S[i] != 'o' and S[i] != 'u') :
            newString += S[i]
    return newString
print(removeVowels(S="what is your name ?"))
