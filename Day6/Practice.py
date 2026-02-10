
'''
Pattern 1: Sqaure
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
n = 5
for i in range(5):
    print("* "*5)

'''
Pattern 2: Right-angled trinagle
*
* *
* * *
* * * *
* * * * *
'''
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
print()
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
print()
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
print()

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
print()
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
print()
for i in range(0,n+1):
    for j in range(1,(n+1)-i):
        print(f"{j} ",end="")
    print()