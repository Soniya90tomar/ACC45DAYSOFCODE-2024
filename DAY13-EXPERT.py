# cook your dish here
T = int(input())
for __ in range(T):
    x,y = map(int,input().split())
    if 2*y>=x :
        print("YES")
    else:
        print("NO")