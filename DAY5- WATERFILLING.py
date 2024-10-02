# cook your dish here
T = int(input())
for __ in range(T):
    B1,B2,B3 = map(int,input().split())
    emptybottle = (B1==0) + (B2 ==0) + (B3==0)
    if emptybottle >=2:
        print("Water filling time")
    else:
        print("Not now")