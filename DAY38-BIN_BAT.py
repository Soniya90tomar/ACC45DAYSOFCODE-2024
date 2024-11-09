# cook your dish here
for __ in range(int(input())):
    N,A,B= map(int,input().split())
    k = N.bit_length()-1
    t=k*A+B*(k-1)
    print(t)