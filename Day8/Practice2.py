
#4.  Program to Print Integers in Words
def int_to_word(string):
    dict = {"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","0":"Zero"}
    for digit in string:
        print(f"{dict[digit]}",end=" ")


string_num = input("\n\nEnter a number : ")
int_to_word(string_num)


#5.  Print Numbers in Words in Reverse Order Using a Switch Case:
def int_to_word_in_rev(string):
    dict = {"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","0":"Zero"}
    n = len(string)
    for i in range(1,n+1):
        digit = string[-i]
        print(f"{dict[digit]}",end=" ")


str_num = input("\n\nEnter a number : ")
int_to_word_in_rev(str_num)


#6.  Write a Program to Display All Factors of a Number
def factor(num):
    factor =  0
    print(f"Factorial of {num} : ",end="")
    for i in range(1,num+1):
        if num % i == 0:
            print(f"{i}",end=" ")
        


factor_num = int(input("\n\nEnter a number : "))
factor(factor_num)


#7.  Amstrong Number or Not
def armstrong(num):
    digit = len(num)
    sum = 0
    n ,num= int(num),int(num)
    while(n>0):
        rem = n % 10
        sum += rem ** digit
        n = n//10
            
    if num == sum:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is Not an Armstrong number")


num = input("\n\nEnter a num : ")
armstrong(num)