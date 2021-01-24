x=int(input("enter the num of rows you want: "))

for i in range(x,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()