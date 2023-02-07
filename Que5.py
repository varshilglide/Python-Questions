pos = -1
def search(list, key):
    i = 0
    while i < len(list):
        if list[i] == key:
            globals()  ['pos'] = i
            return True
        i = i + 1
    return False

list = []
n = int(input("Enter the Number of Element : "))
for i in range(n):
    list.append(int(input("Enter Element : ")))

key = int(input("Enter the element that you want to search"))


if search(list, key):
    print("Found at index", pos)
else:
    print("-1")
    
    
    """
    
    a = []
    n = int(input("Enter the Number of Element  : "))
    for i in range(n):
        a.append(int(input("Enter Element : ")))
    print("List : ")
    
    for element in a:
         print(a)
        
    
    
def linearsearch(linearlist[], size, element):
       for i in range(size):
           if linearlist[i] == element:
                  print(i)
                  
        return False
    
linearlist = []
n = int(input("Enter the Number of Elements: "))
for i in range(n):
       list.append(int(input("Enter the Elements: ")))
print("List...")
    

    
    
    
    
    
    """