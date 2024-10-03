# cook your dish here
T = int(input())
for __ in range(T):
    A,B = map(int,input().split())
    x1= 500 - A*2
    y1 = 1000 - (A+B)*4
    x2= 1000 - B*4
    y2=500-(A+B)*2
    if x1+y1>x2+y2:
        print (x1+y1)
    else:
        print(x2+y2)