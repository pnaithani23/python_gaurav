x=int(input("enter the size of list: "))
l=[]
for i in range (0,x):
    y=eval(input("enter the value: "))
    l.append(y)
    print("index: ",i)
print("userlist : ",l)

even=[]
odd=[]

for i in l:
    if i%2==0:
        even.append(i)

    else:
        odd.append(i)

print("even number list: ",even)
print("odd number list: ",odd)

