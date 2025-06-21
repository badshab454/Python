#python // 
#Language fundamentals
#The Reverser!

#example // 

def reverse(txt):
    reversed_txt = txt[::-1]

    result = reversed_txt.swapcase()

    return reversed_txt

print(reverse("Hello World"))