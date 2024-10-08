# cook your dish here
T = int(input())
for __ in range(T):
    n,x = map(int,input().split())
    
    print(min(x,n-x))