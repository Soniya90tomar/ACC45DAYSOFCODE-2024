# cook your dish here
for __ in range(int(input())):
    n,a,b=map(int,input().split())
    count=0
    co=0
    for i in range(1,n+1):
        if i%2!=0:
            count+=1
        else:
            co+=1
    print(count*b+co*a)
        