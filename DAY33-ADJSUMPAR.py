# cook your dish here
for __ in range(int(input())):
    N=int(input())
    B=list(map(int,input().split()))
    a=[1]
    for i in range(N-1):
        if B[i]==0:
            a.append(a[i])
        else:
            a.append(a[i]+1)
    if(a[0]+a[N-1])%2==B[N-1]:
        print("YES")
    else:
        print("No")