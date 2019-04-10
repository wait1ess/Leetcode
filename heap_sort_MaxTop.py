
# 堆：
# 任意节点小于（或大于）它的所有后裔，最小元（或最大元）在堆的根上（堆序性）。
# 一棵完全树。即除了最底层，其他层的节点都被元素填满，且最底层尽可能地从左到右填入
# 大堆顶
def sink(arr, i, n):                                      # 小节点元素下沉
    '''input: arr 堆
              i  当前节点
              n  堆长度
    '''
    while i * 2 <= n:                                     # 该节点有左子节点
        j = i * 2                                         # 左子节点索引
        if j + 1 <= n and arr[j] < arr[j + 1]:            # 有右子节点且右子点大于左子点元素时
            j += 1
        if arr[i] < arr[j]:                               # 若当前节点小于子点最大点
            arr[i], arr[j] = arr[j], arr[i]               # 交换位置
        i=j
        i *= 2                                            # 递归
        
def heapsort(arr):
    n = len(arr) - 1    
    for i in range(n // 2, 0, -1):                        # 从最后拥有左子节点的元素开始倒序遍历
        sink(arr, i, n)                                   # 小节点元素下沉
                                                          # 建堆完成
    print("heap",arr)
    while n > 0:                                          
        arr[1], arr[n] = arr[n], arr[1]
        n -= 1
        sink(arr, 1, n)


if __name__=="__main__":
    arr=[0,5,5,2,6,1,1,3]
    heapsort(arr)
    print(arr)
