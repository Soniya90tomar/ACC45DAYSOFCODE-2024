# cook your dish here
for __ in range(int(input())):
    n,x,p=map(int,input().split())
    a=(n-x)*-1
    b=x*3
    c=a+b
    if c>=p:
        print("PASS")
    else:
        print("FAIL")