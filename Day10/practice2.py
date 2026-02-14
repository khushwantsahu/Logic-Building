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