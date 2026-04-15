a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
caal=int(input("""enter which operation u want
               1 addition
               2 subtraction
               3 multiplication
               4 division"""))
match caal:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _ :
        print("invalid option")
