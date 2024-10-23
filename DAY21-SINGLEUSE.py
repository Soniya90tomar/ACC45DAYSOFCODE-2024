# cook your dish here
for __ in range(int(input())):
    H,X,Y = map(int,input().split())
    count=0
    if(X<Y):
        count+=1
        remaining_health=H-Y
        if remaining_health >0:
            count += ((H-Y+X-1)//X)
        print(count)