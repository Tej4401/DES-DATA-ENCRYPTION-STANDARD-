P=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
D=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
spec=[0,1,8,15]
def parity_drop(key_64):
    a=[]
    for i in range(56):
        b=P[i]-1
        c=key_64[b]
        a.append(c)
    return a
def divide_28(key_56):
    a=[[],[]]
    for i in range(28):
        b=key_56[i]
        a[0].append(b)
    for i in range(28,56):
        b=key_56[i]
        a[1].append(b)
    return a
def ls1(list1):
    a=list1[0]
    for i in range(27):
        list1[i]=list1[i+1]
    list1[27]=a
    return list1
def ls2(list1):
    a=list1[0]
    for i in range(27):
        list1[i]=list1[i+1]
    list1[27]=a
    a=list1[0]
    for i in range(27):
        list1[i]=list1[i+1]
    list1[27]=a
    return list1
def concatenate(list1,list2):
    a=[]
    for i in range(28):
        b=list1[i]
        a.append(b)
    for i in range(28):
        b=list2[i]
        a.append(b)
    return a
def compression_D(list1):
    a=[]
    for i in range(48):
        b=D[i]-1
        c=list1[b]
        a.append(c)
    return a
key_64=list(input())
p_d_key_56=parity_drop(key_64)
div=divide_28(p_d_key_56)
a=div[0]
b=div[1]
key=[]
for i in range(16):
    if i in spec:
        a=ls1(a)
        b=ls1(b)
        ab=concatenate(a,b)
        k=compression_D(ab)
        key.append(k)
    else:
        a=ls2(a)
        b=ls2(b)
        ab=concatenate(a,b)
        k=compression_D(ab)
        key.append(k)
for i in range(16):
    a=''.join(key[i])
    print("key " + str(i) + " >> " + a)
