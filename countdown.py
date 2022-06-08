
countlist = []
def countdown(x):
    while x >= 0:
        countlist.append(x)
        x = x-1
    print(countlist)
    
countdown(10)
