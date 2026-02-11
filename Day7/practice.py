'''
Pattern :  half_butterfly
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
'''
def  half_butterfly(n):
    for i in range(1,5):
        for j in range(1,i+1):
            print(f"{j} ",end="")
        for j in range(2,(n-i)*2):
            print("  ",end="")
        for k in range(i,0,-1):
            print(f"{k} ",end="")
        print()

'''
Pattern : left Triagle in character
A
A B
A B C
A B C D
A B C D E
'''
def char_pattern(n):
    ch = 65
    for i in range(1,n+1):
        for j in range(0,i):
            print(f"{chr(ch+j)} ",end="")
        print()

'''
Pattern : inverted left triangle in character
A B C D E
A B C D
A B C
A B
A
'''
def inverted_char_pattern(n):
    print()
    ch = 65
    for i in range(0,n):
        for j in range(0,n-i):
            print(f"{chr(ch+j)} ",end="")
        print()

'''
Pattern 
A
B B
C C C
D D D D
E E E E E
''' 
def char_left_triangle(n):
    print()
    ch = 65
    for i in range(n):
        print(f"{chr(ch+i)} "*(i+1))


'''
Pattern 
      A
    A B A
  A B C B A
A B C D C B A
'''

def char_pyramid(n):
    ch = 65
    for i in range(0,n):
        for j in range(n-i):
            print("  ",end="")
        for j in range(i):
            print(f"{chr(ch+j)} ",end="")
        for j in range(i,-1,-1):
            print(f"{chr(ch+j)} ",end="")
        print()

'''
Program to Perform Swapping of Two Numbers:
'''
def swap():
    num1 = int(input("\nEnter a value : "))
    num2 = int(input("Enter a value : "))
    
    num1 = num1+num2  
    num2 = num1-num2
    num1 = num1-num2
    
    print(f"\nValue a : {num1}")
    print(f"Value b : {num2}")

n = 5
half_butterfly(n)
char_pattern(n)
inverted_char_pattern(n)
char_left_triangle(n)
char_pyramid(n)
swap()