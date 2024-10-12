# cook your dish here
import math
T = int(input())
for __ in range(T):
    n,k,m =  map(int,input().split())
    s = (n/(k*m))
    s=math.ceil(s)
    print(s)
    