x=int(input("enter the size of list: "))
l=[]
for i in range (0,x):
    y=str(input("enter the value: "))
    l.append(y)
    print("index: ",i)
print("userlist : ",l)

for i in range(x,-1,-1):
    print(l[i], end="")

