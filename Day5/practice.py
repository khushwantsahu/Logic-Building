#1. Calculate the Sum of Digits of a Given Number
class Calculate: 
    def sum_of_digit(self,num):
        n = num
        sum = 0
        while (n>0):
            rem = int(n%10)
            sum += rem
            n /= 10
        
        print(f"sum of digits {num} : {sum}")

    #2. Write a Program to Check Whether a Character is a Vowel or Consonant:    
    def  vowel_consonent(self,char):
        if char.lower() in ['a','e','i','o','u']:
            print(f"{char} is an Vowel")
        else:
            print(f"{char} is an Consonant")


    #3  Write a Program to Find the ASCII Value of a Character
    def ascii_val(self,char):
        print(f"ASCII Value of {char} : {ord(char)}")


    

def main():
    calculate = Calculate()
    
    num = int(input("Enter a value : "))
    calculate.sum_of_digit(num= num)

    ch = input("\nEnter a character : ")
    calculate.vowel_consonent(char = ch)

    calculate.ascii_val(ch)
    
    

main()