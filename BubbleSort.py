def bubble_sort(arr):
    for i in range(len(arr)-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print(arr)

arr = [2,3,5,6,8,10,15,1,7]

bubble_sort(arr)