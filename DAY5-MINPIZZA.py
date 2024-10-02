# cook your dish here
T = int(input())
for __ in range(T):
    N,X = map(int, input().split())
    x = int((N*X+3)//4)
    print(x)