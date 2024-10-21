# cook your dish here
for __ in range(int(input())):
    N,X,Y = map(int,input().split())
    if Y%X ==0:
        print("YES")
    else:
        print("NO")