# cook your dish here
T = int(input())
for __ in range(T):
    w,x,y,z = map(int,input().split())
    if x==w or y==w or z==w or x+y==w or x+z==w or y+z==w or x+y+z==w:
        print("YES")
    else:
        print("NO")