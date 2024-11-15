# cook your dish here
for __ in range(int(input())):
    n=int(input())
    swipes=list(map(int,input().split()))
    current_in=set()
    max_count=0
    for swipe in swipes:
        if swipe in current_in:
            current_in.remove(swipe)
        else:
            current_in.add(swipe)
        max_count=max(max_count,len(current_in))
    print(max_count)