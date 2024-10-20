# cook your dish here
for __ in range(int(input())):
    N,A,B = map(int,input().split())
    k = N.bit_length()-1
    total_time = k*A+(k-1)*B 
    print(total_time)