#python // 
#Loops
#check factors

def check_factors(factors, num):
    for i in factors:
        if num % i != 0:
            return False
    return True


print(check_factors([2, 5, 4], 12))