a = [2,3,5,6,8,10,15,1,7]

for i in range(len(a)-1):
    temp = a[i]
    for j in range(i,len(a)):
        if(a[j]<temp):
            temp = a[j]
    a[i],temp = temp,a[i]
    print(a)
