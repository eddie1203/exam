def string(s):
    rstring = ""
    for i in s:
        u_code = ord(i)
        if  u_code == 58: 
            u_code += 65248
        rstring += chr(u_code)
    return rstring

x = string("人易科技:上 機 測 驗 - 演算法")
print(x)

x = '人易科技:上 機 測 驗 - 演算法'

new_b = x.replace(' ', '')
new_x = new_b.replace('-',' - ')
print (new_x)
print (x[5:12])
