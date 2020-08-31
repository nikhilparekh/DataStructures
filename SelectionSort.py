a = [2,3,5,6,8,10,15,1,7]

for i in range(len(a)-1):
    temp = i
    for j in range(i+1,len(a)):
        if(a[j]<a[temp]):
            temp = j
    a[i],a[temp] = a[temp],a[i]
    print(a)
