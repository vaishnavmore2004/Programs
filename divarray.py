
arr=[8,9,5,1,2,3]
n=len(arr)
half=n//2
fh=sh=0
for i in range(n):
    if(i<half):
        fh+=arr[i]
    else:
        sh+=arr[i]   
if fh < sh:
    arr.reverse()
print(arr)    
