# cook your dish here
import math
for __ in range(int(input())):
    x,y,r=map(int,input().split())
    
    b=math.ceil((x+(r/30))/y)
    print(b)