# cook your dish here
for __ in range(int(input())):
    s,x,y,z=map(int,input().split())
    n=s-x-y
    if n>=z:
       print(0)
    elif(s-min(x,y)>=z):
        print(1)
    else:
        print(2)
       