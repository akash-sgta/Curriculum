class SelectionSort(object):

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

    def __selection_sort(self):

        for i in range(0, self.size):
            pos = i
            for j in range(i + 1, self.size):
                if self.array[pos] > self.array[j]:
                    pos = j
            if pos != i:
                self.array[i], self.array[pos] = self.array[pos], self.array[i]
        
        return True

    def sort(self):
        self.__selection_sort()
        return self.array

def main():
    array = [9,1,8,2,7,3,6,4,5]
    m = SelectionSort(array)
    print(m.sort())
    array = [1,2,3,4,5,6,7,8,9]
    m = SelectionSort(array)
    print(m.sort())

main()

# O(n^2) - O(n^2) - O(n^2)