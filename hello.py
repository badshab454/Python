#python // 
#Language fundamentals
#Harvard CS50
#Hitting the jackpot

def test_jackpot(result):
    for i in range(len(result) - 1):
        if result[i] != result[i + 1]:
            return False
    return True


print(test_jackpot(["SS", "SS", "SS", "SS"])) # True

print(test_jackpot(["&&", "&", "&&&", "&&&&"])) # False