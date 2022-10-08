def addition(a,b):
    return (a+b)
def subtraction(a,b):
    return (a-b)
def multiplication(a,b):
    return (a*b)
def division(a,b):
    return (a/b)
def menu():
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")
    ch=int(input("ENTER YOUR CHOICE:\n"))
    return ch
def calculation():
    a = int(input("enter the value of a:\n"))
    b = int(input("enter the value of b\n"))
    ch=menu()
    if ch == 1:
        result = addition(a,b)
    elif ch == 2:
        result = subtraction(a,b)
    elif ch == 3:
        result = multiplication(a,b)
    elif ch == 4:
        if b==0:
            print("DIVISION WITH 0 IS INVALID!")
        result = division(a,b)
    print("YOUR FINAL RESULT IS:\n",result)
calculation()


