# cook your dish here
import math
for __ in range(int(input())):
    N,X = map(int,input().split())
    H= list(map(int,input().split()))
    s=sum(math.ceil(h/X) for h in H)
    m=max(H)
    result=min(s,m)
    print(result)