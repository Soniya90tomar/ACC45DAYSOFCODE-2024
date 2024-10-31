# cook your dish here
for __ in range(int(input())):
    P,Q= map(int,input().split())
    B=(P+Q)//2
    if B%2==0:
        print("Alice")
    
    else:
        print("Bob")