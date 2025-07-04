#python // 
#Language fundamentals
#Harvard CS50
#Factorize a Number

def factorize(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

print(factorize(12))