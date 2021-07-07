
arr = [77,5,5,22,13,55,97,4,746,1,0,9]


for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    
print(arr)



