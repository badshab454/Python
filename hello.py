#python // 
#Loops
#get indices

def get_indices(lst, el):
    result = []
    for i in range(len(lst)):
        if el == lst[i]:
            result.append(i)
    return result
    

print(get_indices([1, 2, 1, 3, 1], 1))