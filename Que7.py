while True:
    
    str = input("Enter the String : ")
    
    if str == "exit":
        break
    
    count = 0
    for i in str:
        count = count + 1
    print("Length of String is : ", count)
