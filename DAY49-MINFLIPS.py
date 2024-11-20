# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if n%2!=0:
        print(-1)
    else:
        one=arr.count(1)
        minus=arr.count(-1)
        print(abs(one-minus)//2)