#1. Program to Check Whether the Number is Divisible by 10:
num = int(input("Enter a number : "))
if num % 10 == 0:
    print(f"{num} is divisible by 10")
else:
    print(f"{num} is not divisible by 10")

#2. Program to Check Whether the Number is a Multiple of 15

num = int(input("Enter a number "))
is_true = False
for i in range(num):
    if 15*i == num:
        is_true = True
        break
    else:
        is_true = False

if is_true:
    print(f"{num} is multiple of 15")
else:
    print(f"{num} is not multiple of 15")