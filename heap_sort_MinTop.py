def sink(arr,i,n):                      # 小元素节点下沉 堆顶元素索引为1
    while 2*i+1<=n-1:
        j=2*i+1
        if j+1<=n-1 and arr[j]>arr[j+1]:
            j+=1
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
        i=j

def heap_MinTop(arr):
    n=len(arr)
    for i  in range(n//2,-1,-1):
        sink(arr,i,n)
a=[3,2,3,1,2]
heap_MinTop(a)
print(a)


'''
def heap_sort(arr):
    n=len(arr)-1
    heap_MinTop(arr)
    while n>0:
        arr[1],arr[n]=arr[n],arr[1]
        n-=1
        sink(arr,1,n)
heap_sort(a)
print(a)
'''
