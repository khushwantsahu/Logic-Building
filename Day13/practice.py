
'''Pattern 1:
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''
def pattern1(num):

    for i in range(1,num+1):
        for j in range(1,i+1):
            
            if (i+j) %2 == 0:
                print('1 ',end="")
            else :
                print('0 ',end="")
        print()
pattern1(5)
"""
Pattern 2:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 4 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
"""
print()
def pattern2(num):
    for i in range(num,0,-1):
        for j in range(num,i,-1):
            print(j,end= " ")
        for j in range(1,i*2):
            print(i,end=" ")
        for j in range(i+1,num+1):
            print(j,end=" ")
        print()
    for i in range(1,num):
        for j in range(num,i,-1):
            print(j,end=" ")
        for j in range(1,i*2):
            print(i+1,end=" ")
        for j in range(i+1,num+1):
            print(j,end=" ")
        print()
            
pattern2(4)
"""
Pattern 3:
E
D E
C D E
B C D E
A B C D E
"""
def pattern3(num):
    ch = 65+num;
    for i in range(0,num+1):
        char = ch
        for j in range(0,i):
            print(chr(char),end=" ")
            char = char+1
        print()
        ch = ch-1
pattern3(5)