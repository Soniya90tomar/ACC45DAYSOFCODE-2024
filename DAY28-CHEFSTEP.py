# cook your dish here
for __ in range(int(input())):
    N,K=map(int,input().split())
    a=list(map(int,input().split()))
    s=" "
    
    for i in a:
        
        if i%K==0:
            s=s+'1'
        else:
            s=s+'0'
    print(s)