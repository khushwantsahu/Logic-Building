#Write a Program to Convert Binary Numbers to Decimal and Vice Versa Manually
def decimal_to_binary(num):
    binary = ""
    while num>0:
        rem = num%2
        binary = str(rem) + binary
        num //= 2
    return binary

def binary_to_decimal(bin):
    decimal = 0
    j = 0
    for i in bin[::-1]:
        decimal += int(i)*(2**j)
        j = j+1 
    return decimal


num = int(input("Enter a decimal number : "))
binary = decimal_to_binary(num)
print(f"Binary of {num} : {binary}")

num1 = input("Enter a binary number : ")
decimal = binary_to_decimal(num1)
print(f"decimal of {binary} : {decimal}")



"""
Pattern - 1

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
def pattern1(n):
    for i in range(1,n+1):
        print("* "*i)
    for i in range(n-1,0,-1):
        print("* "*i)

pattern1(5)


'''
Pattern - 2

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

def pattern2(n):
    for i in range(1,n+1):
        for j in range(i,n):
            print("  ",end="")
        for j in range(1,i*2):
            print("* ",end= "")
        print()
    for i in range(2,n+1):
        for j in range(1,i):
            print("  ",end="")
        for j in range(i*2,n*2+1):
            print("* ",end="")
        print()


pattern2(5)
