print("This calculator works only for 2 num")
print("for add type 1")
print("for sub type 2")
print("for multiply type 3")
print("for devide type 4")
x=int(input("enter your choice: "))
a=int(input("enter first number: "))
b=int(input("enter Second number: "))


if x==1:
    c=a+b
    print("your answer is ",c)
elif x==2:
    c=a-b
    print("your answer is ",c )
elif x==3:
    c=a*b
    print("your answer is ",c)
elif x==4:
    c=a/b
    print("your answer is ",c)
else:
    print("input is out of range")