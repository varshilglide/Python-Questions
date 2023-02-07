
"""
StringList = []
a = str(input("Enter the Expression : "))
l = len(a)

if a[0] != chr(45):
    for i in range(l):
        if a[i] == chr(45):
            start = a[i-1]
            end = a[i+1]
            print(start)
            print(end)
            
            for j in range(str(start), str(end)):
                print("String is :  {j} ")
else:
    for i in range(l):
        if a[i] == chr(45):
            start = a[i-1]
            end = a[i+1]
            
            for j in range(str(start), str(end)):
                print("String is : {j}")
                
                
StringList = []
a = input("Enter the Expression : ")
l = len(a)

if str(a[0]) != '-':
    for i in range(l):
        if a[i] == '-':
            start = a[i-1]
            end = a[i+1]
            for j in range(start, end):
                print(j)
else:
    for i in range(l):
        if a[i] == '-':
            start = a[i-1]
            end = a[i+1]
            for j in range(start, end):
                print(j)
    
    
    
"""
StringList = []
a = input("Enter the Expression : ")
l = len(a)

if str(a[0]) != '-':
    for i in range(l):
        if a[i] == '-':
            start = a[i-1]
            end = a[i+1]
            for j in range(int(start), int(end)):
                print(j)
else:
    for i in range(l):
        if a[i] == '-':
            start = a[i-1]
            end = a[i+1]
            for j in range(int(start), int(end)):
                print(j)
                
