#1. Print the Multiplication Table of a Given Number
num = int(input("Enter a number : "))
for i in range(1,11,1):
    print(f"{num} x {i} : {(num*i)}")

#Write a Program to Make a Simple Calculator
numA = float(input("\n\nEnter 1st number : "))
numB = float(input("Enter 2nd number : "))
operator = input("Enter Operator : ")
match operator:
    case '+':
        print(f"{numA} + {numB} : {(numA+numB)}")
    case '-':
        print(f"{numA} - {numB} : {(numA-numB)}")
    case '*':
        print(f"{numA} * {numB} : {(numA*numB)}")
    case '/':
        if numB > 0:
            print(f"{numA} / {numB} : {(numA/numB)}")
    case '%':
        print(f"{numA} % {numB} : {(numA%numB)}")
    case _:
        print(f"----Enter valid Operator----")
    


#3. Print a Number in Reverse Order
numC = int(input("\n\nEnter number : "))
sum = 0
n = numC
while(n>0):
    rem = int(n%10)
    sum = int(10*sum + rem)
    n = n//10

print(f"reverse of {numC} : {sum}")