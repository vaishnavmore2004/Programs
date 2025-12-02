
arr=[3,1,5,4,3,6,3]
n=len(arr)
count=0
for i in range(n-2):
          if((arr[i]+arr[i+2])==arr[i+1]):
            count=count+1
print(count)        


