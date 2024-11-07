# cook your dish here
for __ in range(int(input())):
    L,K = map(int,input().split())
    if L%K ==0:
        print(0)
    else:
        print(1)