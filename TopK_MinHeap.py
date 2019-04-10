# -*- coding: utf-8 -*-
def min_heapify(data, heap_size, i):
    """
    :param data:输入列表
    :param i:节点序号
    :return:返回最小堆,找topk用最小堆
    """
    left = 2*i + 1
    right = 2*i + 2
    if left <= heap_size - 1 and data[left] < data[i]:
        smallest = left
    else:
        smallest = i
    if right <= heap_size - 1 and data[right] < data[smallest]:
        smallest = right
    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        min_heapify(data, heap_size, smallest)


def build_min_heap(data):
    """
    :param data: 输入数据
    :return:返回最小堆数据结构
    """
    lens = len(data)
    node = (lens - 1)//2
    for k in range(node, -1, -1):
        min_heapify(data, lens, k)


def heapsort(data):
    """
    :param data:
    :return:
    """
    # 建堆
    build_min_heap(data)
    for i in range(len(data)):
        data[0], data[len(data) - i - 1] = data[len(data) - i - 1], data[0]
        min_heapify(data, len(data) - i - 1, 0)


if __name__ == "__main__":
    N = 1024
    data_sort = list(range(N))
    data_heap = data_sort[0:10]
    data_heap = data_heap[::-1]
    build_min_heap(data_heap)
    for i in range(10, N):
        if i > data_heap[0]:
            data_heap[0] = i
            build_min_heap(data_heap)
    heapsort(data_heap)
    print(data_heap)
