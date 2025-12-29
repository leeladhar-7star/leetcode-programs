def missingnum(arr):
    n=len(arr)
    n=n+1
    total_sum=(n*(n+1))//2
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    return total_sum-sum
arr=1,2,4,3,5,7,6,10,9
print(missingnum(arr))