# cook your dish here
for __ in range(int(input())):
    N=int(input())
    A = sorted(list(map(int,input().split())))
    operations = 0
    possible = True
    
    for i in range(N):
        if A[i] >i+1:
            possible= False
            break
        operations +=(i+1)-A[i]
    if possible:
        print(operations)
    else:
        print(-1)
    