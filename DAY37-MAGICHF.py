# cook your dish here
for __ in range(int(input())):
    N,X,S = map(int,input().split())
    main = X
    for i in range(S):
        A,B = map(int,input().split())
        if main ==A:
            main = B 
        elif main ==B:
            main = A
    print(main)