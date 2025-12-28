a=int(input("enter first number="))
b=int(input("enter second number="))
sym=input("choose operation from (+,-,*,/):")
if (sym=='+'):
    res=a+b
    print("result is",res)
elif(sym=='-'):
    res=a-b
    print("result is",res)
elif(sym=='*'):
    res=a*b
    print("result is",res)
elif(sym=='/'):
    if(b==0):
        print("division by zero is invalid")
    else:
        res=a/b
        print("result is",res)
else:
    print("invalid operator")
