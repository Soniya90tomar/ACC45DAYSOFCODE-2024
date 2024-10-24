# cook your dish here
for __ in range(int(input())):
    N=int(input())
    I=list(map(int,input().split()))
    c= -1
    for i in range(N):
        if I[i]!=0:
            c=i
    print(c)