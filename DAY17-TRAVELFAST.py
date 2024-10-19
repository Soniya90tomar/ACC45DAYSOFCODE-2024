# cook your dish here
T = int(input())
for __ in range(T):
    
    x,y = map(int, input().split())
    if(x<y):
        print("BIKE")
    elif(x>y):
        print("CAR")
    else:
        print("SAME")
