'''for i in range(0, 123):
    print(chr(i))'''
l=[]
x=str(input("enter the value: "))
l.extend(x)
print(l)


count = 0
for i in range(97,123):
    print('the count of',chr(i), 'is {}'.format(l.count(chr(i))))


