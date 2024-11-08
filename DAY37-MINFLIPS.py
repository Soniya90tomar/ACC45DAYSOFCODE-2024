# cook your dish here
for __ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    if N%2!=0:
        print(-1)
    else:
        X=A.count(1)
        Y=A.count(-1)
        print(abs(X-Y)//2)