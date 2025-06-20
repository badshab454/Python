#python // 
#Language fundamentals
#Same parity

def parity_analysis(num):
    string_num = str(num) #converted num int to str
    sum = 0
    for i in string_num:
        sum += int(i)
    return sum % 2 == num % 2

print(parity_analysis(243))






