# Prefix match with other strings
# Given an array of strings arr[] of size n and given s a string str and an integer k. The task is to find the count of strings in arr[] whose prefix of length k matches with the k length prefix of str.

def klengthpref (arr, n, k, s) :
    count = 0
    for word in range (len(arr)) :
        wordd = arr[word]
        if wordd[0:k] == s[0:k] :
            count += 1
    return count
        
print(klengthpref(arr=["geeks", "geeksforgeeks", "forgeeks"], n=3, k=2, s="geeks"))