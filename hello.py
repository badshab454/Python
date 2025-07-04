#python // 
#Language fundamentals
#odd up, even down

def transform(lst):
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(i - 1)
        else:
            result.append(i + 1)

    return result


print(transform([1, 2, 3, 4, 1]))