#python // 
#Language fundamentals
#Xs and Os

#example // 


def XO(txt):
    txt = txt.lower()
    x = 0
    o = 0
    for i in txt:
        if i == "x":
            x += 1
        elif i == "o":
            o += 1
            
    return x == o
  

print(XO("dffdd")) #true