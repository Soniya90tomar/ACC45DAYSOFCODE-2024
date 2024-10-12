# cook your dish here
from collections import Counter
T = int(input())
for __ in range(T):
    n = int(input())
    N = list(map(int,input().split()))
    counts = Counter(N)
    possible= all(count%2 ==0 for count in counts.values())
    if possible:
        print("YES")
    else:
        print("NO")