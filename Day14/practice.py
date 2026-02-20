"""
Pattern 1

   *
  * *
 *   *
*     *
 *   *
  * *
   *
"""
def pattern1(num):
    for i in range(0,num):
        for j in range(num,i+1,-1):
            print(" ",end=" ")
        print("* ",end="")
        for j in range(1,i*2):
            print(" ",end=" ")
        if i != 0:
            print("*",end=" ")
        print()
    for i in range(1,num):
        for j in range(i):
            print("  ",end="")
        print("* ",end="")
        for j in range(i,(num-i)*2,2):
            print("  ",end="")
        if i != num-1:
            print("*",end="")
        print()

pattern1(4)
"""
Pattern 2
    1
  1 2 1
1 2 3 2 1
"""
def pattern2(num):
    for i in range(1,num+1):
        for j in range(i,num):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(i-1,0,-1):
            print(j,end=" ")
        print()
    
pattern2(3)
"""
Pattern 3
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
"""

def pattern3(num):
    print()
    for i in range(1,num+1):
        for j in range(1,num+1):
                print((i+j)%2,end=" ")
        print()

pattern3(5)