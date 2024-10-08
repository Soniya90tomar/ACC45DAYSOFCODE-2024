# cook your dish here
T = int(input())
for __ in range(T):
    x,y = map(int,input().split())
    if x>y:
        t=x-y
    elif x==y:
        t=0
    else:
        t=y-x
    print(t)