#python // 
#Loops
#is palindrom string

def is_palindrome(txt):
    reversed_str = txt[::-1]
    return reversed_str == txt

print(is_palindrome("mos"))

