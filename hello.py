#python // 
#Loops
#Num to dashes

def num_to_dashes(num):
    result = ""
    for i in range(num):
        result += "-"
    return result


print(num_to_dashes(5))