# cook your dish here
N = int(input())
y = list( map(int,input().split()))
even = 0
odd =0
for __ in range(N):
    for i in y:
        if i%2==0:
            even+= 1
        else:
            odd+= 1
if even>odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
    