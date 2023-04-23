T= int(input())
for A in range(T):
    bottles=0
    N,X,K= map(int,input().split())
    if N*X<=K:
        print(N)
    else:
        for i in range(1,N+1):
            if X*i<=K:
                bottles= bottles+1
        print(bottles)
