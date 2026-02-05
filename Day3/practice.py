#1. Program to Calculate the Square and Cube of a Number:
def square(num):
    return num**2

def cube(num):
    return num**3




#2. Program to Calculate the Area of a Circle and Triangle:

def c_area(radius):
    return 3.14*radius**2

def t_area(base , height):
    return base*height


def leapyear():
    #Write a Python program to check if a year entered by the user is a Leap Year or NOT.
    while(True):
        leap_or_not = int(input("Enter year find leap or not: "))
    

        '''if (leap_or_not % 4 == 0):
            if(leap_or_not % 100 == 0):
                if(leap_or_not % 400 == 0):
                   print(f"{leap_or_not} is leap year")
                else:
                    print(f"{leap_or_not} is not leap year")
            else:
                print(f"{leap_or_not} is leap year")
        else:
            print(f"{leap_or_not} is not leap year")'''

        if (((leap_or_not % 4 == 0) and (leap_or_not % 100 != 0)) or (leap_or_not % 400 == 0)):
            print(f"{leap_or_not} is leap year\n")
        else:
            print(f"{leap_or_not} is not leap year\n")
        
        str = input("want to continue y/n : ")
        if str in ["n","N"]:
            break


def main():
    n = int(input("Enter number : = "))
    square_ = square(num= n)
    cube_= cube(num=n)
    print(f"Square of {n} : {square_}")
    print(f"Cube of {n} : {cube_}\n")


    r = float(input("Enter radious "))
    area = c_area(radius = r)
    print(f"Area of circle : {area}\n")
    
    h = float(input("Enter height "))
    b = float(input("Enter base "))
    tarea = t_area(base = b,height=h)
    print(f"area of triangle : {tarea}\n")

    leapyear()


main()
