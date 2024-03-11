#to create a simple calculator
p=int(input("Enter first number: "))
q=int(input("Enter second number: "))
opr=input("Enter the type of operation(+,-,%,*,/): ")
result=0
if opr=="+":
    result=p+q
elif opr=="-":
    if p>q:
        result=p-q
    else:
        result=q-p
elif opr=="%":
        result=p%q
elif opr=="/":
        result=p//q
elif opr=="*":
        result=p*q
else:
        print("Invalid input")
print("Your answer is: ",result)
