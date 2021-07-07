#消除相同元素
def eve(arr, n):
    new_arr = []
    for i in range(n):
        if arr[i] not in new_arr:
            new_arr.append(arr[i])
                

    return new_arr

#交集
def inter(arr_a, arr_b):

    arr_c = []
    size_a = len(arr_a)
    size_b = len(arr_b)

    for i in range(size_a):
        for j in range(size_b):
            if arr_a[i] == arr_b[j]:
                arr_c.append(arr_a[i])

    arr_c = eve(arr_c, len(arr_c))
     
    return arr_c

#差集
def dif(arr_a, arr_b):
    
    arr_d = []
    size_a = len(arr_a)
    size_b = len(arr_b)
    
    for i in range(size_a):
        if arr_a[i] not in arr_b:
            arr_d.append(arr_a[i])

    return arr_d

#聯集
def Uni(arr_a, arr_b):
    
    arr_e = []
    size_a = len(arr_a)
    size_b = len(arr_b)
    
    for i in range(size_a):
        arr_e.append(arr_a[i])
    
    for j in range(size_b):
        arr_e.append(arr_b[j])
    
    arr_e = eve(arr_e, len(arr_e))
    return arr_e
    

arr_a = [77, 5, 5, 22, 13, 55, 97, 4, 796, 1, 0, 9]
arr_b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


arr_c = inter(arr_a, arr_b)
arr_d = dif(arr_a, arr_b)
arr_e = Uni(arr_a, arr_b)
print('交集：', arr_c)
print('差集：', arr_d)
print('聯集：', arr_e)
