n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=0
j=0
while j<m:
    if i>=n:
        print(n,end=' ')
        j+=1
        continue
    if a[i]>=b[j]:
        print(i,end=' ')
        j+=1
    else:
        i+=1
