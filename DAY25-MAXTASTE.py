# cook your dish here
T = int(input())
for __ in range(T):
    a,b,c,d = map(int,input().split())
    print(max(a,b)+max(c,d))