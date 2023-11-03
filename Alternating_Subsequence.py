for _ in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split()))
    i=0
    k=0
    seq=[nums[0]]
    for j in range(1,n):
        if nums[j]^nums[j-1]<0:
            seq.append(nums[j])
            k+=1
            i=j
        elif nums[j]>nums[i]:
            seq[k]=nums[j]
            i=j
    print(sum(seq))
    
