
def checkfirst(l1):
    i = ord(l1[0])
    # print(i)
    if i != 45:
        finalList(l1)
    else:
        l1.remove(l1[0])
        checkfirst(l1)


def printing(newList):
    v = 0
    res = ""
    for v in range(len(newList) -1):
        x = ord(newList[v])
        y = ord(newList[v+1])
        j = 0 
        for j in range(x, y + 1):
            res = res + chr(j)
        
        v = v + 2
    print(res)
            
    

def finalList(l1):
    newList = []
    i = 0
    for i in range(len(l1)):
        if l1[i] == chr(45):
            i = i + 1
        else:
            newList.append(l1[i])
    printing(newList)
    
# driver code
string = input("Enter the string:")
l1 = []
# ll1 = []
l1[:0] = string
checkfirst(l1)
 
        



    


