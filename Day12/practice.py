"""
Pattern - 1

*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
"""

def butterfly(num):
    for i in range(1,num+1):
        for j in range(i):
            print("* ",end="")
        for j in range(i,num*2-i):
            print("  ",end="")
        for j in range(i):
            print("* ",end="")
        print()
    for i in range(1,num):
        for j in range(i, num):
            print("* ",end="")
        for j in range(0,i*2):
            print("  ",end="")
        for j in range(i,num):
            print("* ",end="")
        print()
butterfly(5)
print()


"""             
Pattern - 2

* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
"""
def hollow_diamond(num):
    for i in range(1,num+1):
        for j in range(i,num+1):
            print("* ",end="")
        for j in range(1,i*2 - 1):
            print("  ",end="")
        for j in range(i,num+1):
            print("* ",end="")
        print()
    for i in range(1,num+1):
        for j in range(0,i):
            print("* ",end="")
        for j in range(i,num*2 - i):
            print("  ",end= "")
        for j in range(0,i):
            print("* ",end= "")
        print()
hollow_diamond(5)

"""
Pattern - 3

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""

def print_num(num):
    k=1
    for i in range(1,num+1):
        for j in range(0,i):
            print(f"{k} ",end="")
            k = k+1
        print()
print()
print_num(5)