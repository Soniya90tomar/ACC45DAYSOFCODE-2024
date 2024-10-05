# cook your dish here
T = int(input())
for __ in range(T):
    n= int(input())
    arr = list(map(int,input().split()))
    for i in range(n-1):
        if (arr[i+1]<arr[i]):
            temp =  arr[i+1]
            arr[i+1]= arr[i]
            arr[i]=temp
            break
    if(arr==sorted(arr)):
        print("Yes")
    else:
        print("No")