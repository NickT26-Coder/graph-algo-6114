import random
'''
left child: 2i+1
right child: 2i+2
parent: i - 1 // 2
'''

# Insert one at a time to create min heap
def insert_to_heap(heap: list[tuple], value: tuple):
    # insert tuple into heap list
    heap.append(value)
    index_of_value = len(heap) - 1
    index_of_parent = (index_of_value-1)//2
    # heapify, compare by distance
    while heap[index_of_value][1] < heap[index_of_parent][1]:
        heap[index_of_value], heap[index_of_parent] = heap[index_of_parent], heap[index_of_value]
        index_of_value = index_of_parent
        index_of_parent = max(0, (index_of_value-1)//2)
    
def remove_min(heap):
    minimum_vertex, minimum_vertex_dist = heap[0]
    # Only swap if the root is less than the last element
    if minimum_vertex_dist < heap[len(heap)-1][1]:
        # swap the last node with the root (the smallest value)
        heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    i = 0
    heap.pop()
    # terminate when heap[i] is a leaf node or when the children are greater than heap[i]
    while 2*i+2 <= len(heap)-1 and (heap[i][1] > heap[2*i+1][1] or heap[i][1] > heap[2*i+2][1]):
        if heap[2*i+1][1] > heap[2*i+2][1]:
            heap[i], heap[2*i+2] = heap[2*i+2], heap[i]
            i = 2*i+2
        else:
            heap[i], heap[2*i+1] = heap[2*i+1], heap[i]
            i = 2*i+1
    return minimum_vertex

# if __name__ == "__main__":
#     lst = []
#     n = 10000
#     for i in range(n):
#         lst.append(random.randint(0,n))
    
#     sorted_list = heap_sort(lst)
#     if sorted(lst) == sorted_list:
#         print("Sorted!")
