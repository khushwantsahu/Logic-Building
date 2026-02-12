def factorial(n):
    fact =  1
    for i in range(1,n+1):
        fact *= i
    
    print(f"Factorial of {n} : {fact}")

def fibonacci(n):
    sum = 0
    a = 0
    b = 1
    print(f"Fibonacci series : {a} {b}",end=" ")
    for i in range(2,n):
        sum = a + b
        a , b = b , sum
        print(f"{sum}",end=" ")

def GCD(n1,n2):
    gcd = 0
    n = min(n1,n2)
    for i in range(1,n+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

def LCM(n1,n2):
    lcm = 0
    lcm = (n1*n2) // GCD(n1,n2)
    print(f"LCM of {n1} and {n2} is {lcm}")




#1. Factorial of a Number Using a For Loop
fact_num = int(input("Enter a number : "))
factorial(n = fact_num)

#2.  Print Fibonacci Series
terms = int(input("\nEnter the number of term : "))
fibonacci(terms)

#3.  Write a Program to Find the GCD or HCD and LCM of Two Numbers:
num1 = int(input("\nEnter Two numbers : "))
num2 = int(input("Enter a number : "))
gcd = GCD(n1=num1,n2=num2)
print(f"GCD of {num1} and {num2} is {gcd}")
LCM(n1=num1,n2=num2)


