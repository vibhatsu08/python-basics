# Python program to encrypt and decrypt a string, based on a pattern.
# This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during the Gallic Wars. The idea is rather simple – every letter of the message is replaced by its nearest consequent (A becomes B, B becomes C, and so on). The only exception is Z, which becomes A.

def cipher (str) :
    newStr = ""
    for ch in str :
        if not ch.isalpha() :
            continue
        ch = ch.upper()
        code = ord(ch)+1
        if code > ord('Z') :
            code = ord('A')
        newStr += chr(code)
    return newStr
print(cipher(str="hello world my name is Ultron!"))

def reverseCipher (str) :
    newStr = ""
    for ch in str :
        if not ch.isalpha() :
            continue
        code = ord(ch)-1
        if code < ord('A') :
            code = ord('Z')
        newStr += chr(code)
    return newStr
print(reverseCipher(str="IFMMPXPSMENZOBNFJTVMUSPO"))
    