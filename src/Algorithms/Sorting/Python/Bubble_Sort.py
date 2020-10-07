class BubbleSort(object):

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

    def __bubble_sort(self):

        for i in range(0, self.size - 1):
            for j in range(0, self.size - 1 - i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        
        return True

    def sort(self):
        self.__bubble_sort()
        return self.array

def main():
    array = [9,1,8,2,7,3,6,4,5]
    m = BubbleSort(array)
    print(m.sort())
    array = [1,2,3,4,5,6,7,8,9]
    m = BubbleSort(array)
    print(m.sort())

main()

# O(n^2) - O(n^2) - O(n^2)