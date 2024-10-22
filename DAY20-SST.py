# cook your dish here
for __ in range(int(input())):
    A,B= map(int,input().split())
    if(A*100/10==B*100/20):
            print("ANY")
    elif(A*100/10>B*100/20):
            print("FIRST")
    else:
            print("SECOND")