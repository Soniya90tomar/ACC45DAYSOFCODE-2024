# cook your dish here
T = int(input())
for __ in range(T):
    X = int(input())

    if X<=100:
        print(X)
    elif 100<X<=1000:
        print(X-25)
    elif 1000<X<=5000:
        print(X-100)
    else:
        print(X-500)