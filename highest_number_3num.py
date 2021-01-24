x=int(input("enter the 1st number: "))
y=int(input("enter the 2nd number: "))
z=int(input("enter the 3rd number: "))

if x>y and x>z:
    print("highest num is ",x)
elif y>x and y>z:
    print("highest num is ",y)
elif z>y and z>y:
    print("highest num is ",z)