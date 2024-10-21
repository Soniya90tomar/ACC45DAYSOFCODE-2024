# cook your dish here
for __ in range(int(input())):
    N= int(input())
    P = list(map(int,input().split()))
    count={}
    for size in P:
        if size in count:
            count[size]+=1
        else:
            count[size]=1
            
        possible = True
        for size,num_people in count.items():
            if num_people % size!=0:
                possible= False
                break
        
         
    if possible:
        print("YES")
    else:
        print("NO")