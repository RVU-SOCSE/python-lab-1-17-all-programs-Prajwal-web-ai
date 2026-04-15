choice=input("convert to (C)elsius or (F)ahrenhe? ").lower()
temp=float(input("enter the temperture value:"))
if choice=='c':
    celsius=(temp-32)*5/9
    print("temperture in celsius:",celsius)
elif choice =='f':
    fahrenheit=(temp*9/5)+32
    print("temperture in fahrenheit:",fahrenheit)
else:
        print("invalid choice")
