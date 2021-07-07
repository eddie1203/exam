arr = [0,1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
a=0
b=0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        a+=arr[i]
        even.append(arr[i])
  
    else:
        if arr[i] % 2 != 0:  
           b+=arr[i] 
           odd.append(arr[i])
print (b-a)
print (odd)
print (even)
