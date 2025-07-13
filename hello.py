#python // 
#Loops
#Sum of the Odd Numbers

def add_odd_to_n(n):
    num = 0
    for i in range(1, n + 1, 2):
        num += i
    return num

print(add_odd_to_n(5))