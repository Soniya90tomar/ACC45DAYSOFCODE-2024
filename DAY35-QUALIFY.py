# cook your dish here
for __ in range(int(input())):
    X,A,B= map(int,input().split())
    if X<= A*1+B*2:
        print("Qualify")
    else:
        print("NotQualify")