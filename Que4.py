"""
num = int(input("Enter the number : "))
def DecimaltoBinary(num):
    if num >= 1:
        DecimaltoBinary(num // 2)
    print(num % 2, end = " ")
    
print(DecimaltoBinary(num))
"""

num = int(input("Enter the Number : "))
binary = format(num, 'b')

print("Interger to binary is : ", binary)

position = int(input("Enter the position of number : "))
count = int(input("Enter the Count : "))

mask = ~(~0 << count) << position
print("Inverted Number is : ",num ^ mask)


