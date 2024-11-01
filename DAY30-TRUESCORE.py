# cook your dish here
for __ in range(int(input())):
    A,B=map(int,input().split())
    C,D=map(int,input().split())
    if C>=A and D>=B:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")