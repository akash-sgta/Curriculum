from my_list import List

def heapify(self, n, i):

    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and self[i] < self[l]:
        largest = l
    if r < n and self[largest] < self[r]:
        largest = r

    if largest != i:
        self[i], self[largest] = self[largest], self[i]
        self.util(n, largest)

def heap_sort(self):
    size = len(self)
    # build heap
    for i in range(size//2 - 1, -1, -1):
        self.util(size, i)
        
    # extract one by one from top
    for i in range(size-1, 0, -1):
        # swap root with last
        self[i], self[0] = self[0], self[i]
        # heapify the reduced heap
        self.util(i, 0)
        
    return True

def main():
    List.sort = heap_sort
    List.util = heapify

    array = List(9,1,8,2,7,3,6,4,5)
    print(array.sort())
    print(array)
    array = List(1,2,3,4,5,6,7,8,9)
    print(array.sort())
    print(array)

main()

# O(nlogn) - O(nlogn) - O(nlogn)