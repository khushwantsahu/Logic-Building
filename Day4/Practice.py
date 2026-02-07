#1. Print the Multiplication Table of a Given Number
class Table:
    def __init__(self,num):
        self.num = num
    
    def multiply(self):
        for i in range(1,11,1):
            print(f"{self.num} x {i} : {(self.num*i)}")

#Write a Program to Make a Simple Calculator
class Calculator:
    def __init__(self,numA,numB,op):
        self.numA = numA
        self.numB = numB 
        self.op = op
        
    def select(self):
        match self.op:
            case '+':
                print(f"{self.numA} + {self.numB} : {(self.numA+self.numB)}")
            case '-':
                print(f"{self.numA} - {self.numB} : {(self.numA-self.numB)}")
            case '*':
                print(f"{self.numA} * {self.numB} : {(self.numA*self.numB)}")
            case '/':
                if self.numB > 0:
                    print(f"{self.numA} / {self.numB} : {(self.numA/self.numB)}")
            case '%':
                print(f"{self.numA} % {self.numB} : {(self.numA%self.numB)}")
            case _:
                print(f"----Enter valid Operator----")
    


#3. Print a Number in Reverse Order
class Reverse:
    def __init__(self,num):
        self.num = num 

    def reverse(self):
        sum = 0
        n = self.num
        while(n>0):
            rem = int(n%10)
            sum = int(10*sum + rem)
            n = n//10
        print(f"reverse of {self.num} : {sum}")

def main():
    num = float(input("\nEnter number : "))
    table = Table(num=num)
    table.multiply()


    while True:
        num1 = float(input("\n\nEnter number : "))
        num2 = float(input("Enter number : "))
        op = input("Enter Operator : ")
        calculator  = Calculator(numA= num1,op=op,numB=num2)
        calculator.select()

        option = input("Want to continue(Y/N) : ")
        if option.lower() == 'n':
            break
    
    num = int(input("\nEnter number to reverse : "))
    reverse = Reverse(num=num)
    reverse.reverse()

main()