
'''
Pattern 1: Sqaure
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
def sqauare(n):
    for i in range(1,n):
        print("* "*5)

'''
Pattern 2: Right-angled trinagle
*
* *
* * *
* * * *
* * * * *
'''
def right_angled_trinagle(n):
    for i in range(n+1):
        print("* "*i)


'''
Pattern 3: Hallow Rectangle
* * * * *
*       *
*       *
*       *
* * * * *
'''

def hallow_rectangle(n):
    for i in range(n):
        for j in range(n):
            if ((i == 0) or (j==0) or (i == n-1) or (j==n-1)) :
                print("* ",end="")
            else:
                print("  ",end="")
        print()


'''
Pattern 1: Inverted Right-angled triangle
* * * * *
* * * *
* * *
* *
*
'''

def inverted_right_angle_triangle(n):
    for i in range(n,0,-1):
        print("* "*i)


'''
Pattern 2: traingle
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

def trianlgle(n):
    for i in range(1,n+1):
        for j in range(n,i,-1):
            print("  ",end = "")
        for k in range(1,i*2,1):
            print("* ",end = "") 
        print()


'''
Pattern 3: Inverted traingle
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''


def inverted_triangle(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print("  ",end="")
        for j in range(i*2,n*2+1):
            print("* ",end="")
        print()

'''
Pattern 7:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

def pattern7(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(f"{j} ",end="")
        print()

'''
Pattern 8

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
def pattern8(n):
    for i in range(1,n+1):
        print(f"{i} "*i)

'''
Pattern 9

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

'''
def pattern9(n):
    for i in range(0,n+1):
        for j in range(1,(n+1)-i):
            print(f"{j} ",end="")
        print()


n=5
sqauare(n)
print()
right_angled_trinagle(n)
print()
hallow_rectangle(n)
print()
inverted_right_angle_triangle(n)
print()
trianlgle(n)
print()
inverted_triangle(n)
print()
pattern7(n)
print()
pattern8(n)
print()
pattern9(n)
