# cook your dish here
for __ in range(int(input())):
    a,b,c=map(int,input().split())
    x=a+b
    y=b+c
    z=a+c
    k=  max(x,y,z)
    print(k)