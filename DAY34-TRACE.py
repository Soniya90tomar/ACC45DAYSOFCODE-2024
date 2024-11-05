# cook your dish here
T=int(input())
for __ in range(T):
    n=int(input())
    arr=[]
    for __ in range(n):
        lst= list(map(int,input().split()))
        arr.append(lst)
    ans= -float('INF')
    for i in range(n):
        x=i
        y=0
        s1=0
        s2=0
        while x<n and y<n:
            s1 = s1+arr[x][y]
            s2 = s2+arr[y][x]
            x+=1
            y+=1
        ans = max(ans,s1,s2)
    print(ans)