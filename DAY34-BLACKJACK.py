# cook your dish here
for __ in range(int(input())):
    A,B = map(int,input().split())
    X= 21-(A+B)
    if X>=0 and X<=10:
        print(X)
    else:
        print("-1")