# cook your dish here
T = int(input())
for __ in range(T):
    x,y = map(int,input().split())
    if (y%x==0):
        print(y//x-1)
    else:
        print(y//x)