class HeapSort(object):

    def __init__(self, array):
        self._array = array
        self._size = len(array)
    
    @property
    def array(self):
        return self._array
    @array.setter
    def array(self, val):
        self._array = val

    @property
    def size(self):
        return self._size

    def __heapify(self, array, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2

        if l < n and array[i] < array[l]:
            largest = l
        if r < n and array[largest] < array[r]:
            largest = r

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.__heapify(array, n, largest)

    def __heap_sort(self):


        for i in range(self.size//2 - 1, -1, -1):
            self.__heapify(self.array, self.size, i)
        
        for i in range(self.size-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.__heapify(self.array, i, 0)
        
        return True

    def sort(self):
        self.__heap_sort()
        return self.array

def main():
    array = [9,1,8,2,7,3,6,4,5]
    m = HeapSort(array)
    print(m.sort())
    array = [1,2,3,4,5,6,7,8,9]
    m = HeapSort(array)
    print(m.sort())

main()

# O(n^2) - O(n^2) - O(n^2)