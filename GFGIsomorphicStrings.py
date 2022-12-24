# Isomorphic Strings
# Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
# Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.
# Note: All occurrences of every character in str1 should map to the same character in str2

def areIsomorphic (str1, str2) :
    if len(str1) != len(str2) :
        return 0
    
    mapping = {}
    
    for i in range (len(str1)) :
        if str1[i] not in mapping :
            if str2[i] in mapping.values() :
                return 0
            mapping[str1[i]] = str2[i]
        else :
            if mapping[str1[i]] != str2[i] :
                return 0
    return 1
    
print(areIsomorphic(str1="aab", str2="xxy")) 