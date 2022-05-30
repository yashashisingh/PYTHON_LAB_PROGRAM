a={}
size=int(input("enter the size"))
for i in range(0,size):
    x=int(input("enter the key"))
    y=int(input("enter the values"))
    a[x]=y
key=int(input("enter the replacement key"))
a.pop(key)
key1=int(input("enter the key"))
value1=int(input("enter the values"))
a[key1]=value1
print(a)
