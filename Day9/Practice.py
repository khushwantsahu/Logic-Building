def prime(num):
    for i in range(2,num):
        if num%i ==  0:
            return False
    return True

#1.   Check Whether a Number is Prime or Not
n = int(input("Enter a number : "))
if prime(num=n):
    print(f"{n} is an prime Number")
else:
    print(f"{n} is not an prime number")


#2   Print Prime Numbers Within a Range
n1 = int(input("\nEnter number : "))
n2 = int(input("Enter number : "))
print(f"prime number between {n1} and {n2} : ",end="")
for i in range(n1,n2+1):
    if prime(num=i):
        print(f"{i}",end=" ")


#3   Print Factorial Series:
def factorial(num):
    temp = 1
    for i in range(1 , num+1):
        temp *= i
        print(f"{i}! : {temp}")

n3 = int(input("\n\nEnter a number : "))
factorial(num = n3)