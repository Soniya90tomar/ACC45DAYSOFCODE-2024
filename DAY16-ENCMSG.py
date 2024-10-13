# cook your dish here
T = int(input())
for __ in range(T):
    N = int(input())
    S = input()
    temp1 = list(S)
    for i in range(0,N-1,2):
        temp1[i],temp1[i+1] = temp1[i+1],temp1[i]
    temp2=''
    for i in range(N):
        temp2 += chr(219-ord(temp1[i]))
    print(temp2)
    