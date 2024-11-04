#Program to build a simple calculator
def calculate(a,b,opr):
    if (opr=='+'):
       res=a+b
    elif (opr=='-'):
        res=a-b
    elif (opr=='*'):
        res=a*b
    elif (opr=='/'):
        res=a/b
    else:
         Error=('Invalid Operator')
    return res
num1=float(input("Enter the first number:"))
opr=input("Enter an operator(+,-,*,/):")
num2=float(input("Enter the second number:"))
print(num1,opr,num2)
res=calculate(num1,num2,opr)
print("=",res)
