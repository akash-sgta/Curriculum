class InsertionSort(object):

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

    def __insertion_sort(self):

        for i in range(1, self.size):
            key = self.array[i]
            j = i - 1
            while j>=0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
        
        return True

    def sort(self):
        self.__insertion_sort()
        return self.array

def main():
    array = [9,1,8,2,7,3,6,4,5]
    m = InsertionSort(array)
    print(m.sort())
    array = [1,2,3,4,5,6,7,8,9]
    m = InsertionSort(array)
    print(m.sort())

main()

# O(n^2) - O(n^2) - O(n^2)