# cook your dish here
for __ in range(int(input())):
    N=int(input())
    if N<=1:
        print("no")
    else:
        
        for i in range(2,N):
          if N%i==0:
            print("no")
            break
        else:
            print("yes")