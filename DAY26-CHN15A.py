# cook your dish here
for __ in range(int(input())):
    N,K = map(int,input().split())
    n= map(int,input().split())
    count=0
    for i in n:
      if (i + K)%7 ==0:
        count+=1
    print(count)