# cook your dish here
t=int(input())
for _ in range(t):
    A,B = map(int,input().split())
    i=1
    Limak=0
    Bob=0
    while A>0 and B>0:
        if i%2!=0:
            if(Limak+i)<=A:
                Limak=Limak+i
            else:
                break
        else:
            if(Bob+i)<=B:
                Bob=Bob+i
            else:
                break
        #print(Limak,Bob,i)
        i=i+1
    #print(i)
    if i%2==0:
        print('Limak')
    else:
        print('Bob')