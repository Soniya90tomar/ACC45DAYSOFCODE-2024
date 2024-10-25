# cook your dish here
# cook your dish here
t=int(input())
for tc in range(t):
    n=int(input())
    arr=list(input().split())
    count=0
    bount=0
    for i in arr:
       if i=="START38":
          count+=1
       elif i=="LTIME108":
          bount+=1
    print(count, bount)  
