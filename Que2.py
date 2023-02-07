# find one's count

n = int(input("Enter the number : "))
x = n & (n-1)
count = 1
while(x!=0):
    count = count + 1
    x = x & (x-1)
print("Number of 1's is : ", count)
    
    

















"""
#include<stdio.h>
int main()
{
    int n;
    printf("Enter the Number : ");
    scanf("%d", &n);

    int x = n & (n-1);
    int count = 1;

    while(x!=0)
    {
        count ++;
        x = x & (x-1);
    }

    printf("Number of 1'S is %d", count);

}
"""