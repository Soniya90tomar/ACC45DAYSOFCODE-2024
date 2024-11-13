# cook your dish here
for __ in range(int(input())):
    n=int(input())
    N=list(map(int,input().split()))
    k=int(input())
    s=N[k-1]
    b=sorted(N)
    for i in range(n):
        if b[i]==s:
            print(i+1)
            break