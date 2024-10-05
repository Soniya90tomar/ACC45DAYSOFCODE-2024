# cook your dish here
T = int(input())
for __ in range(T):
    P,Q,R,S = map(int,input().split())

    if S> P+Q+R or R>P+Q+S or Q>P+R+S or  P> Q+S+R:
       print("yes")
    else:
       print("NO")