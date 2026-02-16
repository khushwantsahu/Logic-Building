#   Write a Program to Check Whether a Number is a Palindrome
def pelindrome(num):
    n = num
    rev = 0
    while n>0:
        rem = int(n%10)
        rev = (rev*10) + rem
        n //=10
    
    if rev == num:
        print(num," is a pelindrome number")
    else:
        print(num," is not a pelindrome number ")


pelin_num = int(input("Enter a number to check pelindrome or not : "))
pelindrome(num = pelin_num)

#   Check if an Integer Can Be Expressed as the Sum of Two Prime Numbers
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_of_two_prims(num):
    for i in range(2,num//2+1):
            if isPrime(i) and isPrime(num-i):
                print(f"{num} : {i} + {num-i}")


num = int(input("Enter a number to check if its an Expressed as the Sum of Two Prime Numbers : "))
sum_of_two_prims(num)


#   Print All Digits and Alphabets Using a For Loop
def print_alpha_digit():
    print("digit : ",end="")
    for i in range(10):
        print(i,end=" ")

    print()

    print("Alphabate : ",end="")
    for ch in range(65,91):
        print(chr(ch),end=" " )

    for ch in range(97,123):
        print(chr(ch),end=" " )


print_alpha_digit()
