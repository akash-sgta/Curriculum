class MergeSort(object):

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

    def __merge_sort(self, array):

        if len(array) > 1:
            middle = len(array) // 2
            left_array = array[:middle]
            right_array = array[middle:]

            self.__merge_sort(left_array)
            self.__merge_sort(right_array)

            i=j=k=0

            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    array[k] = left_array[i]
                    i += 1
                else:
                    array[k] = right_array[j]
                    j += 1
                k += 1
            
            while i < len(left_array):
                array[k] = left_array[i]
                k += 1
                i += 1
            
            while j < len(right_array):
                array[k] = right_array[j]
                k += 1
                j += 1
        
        return True

    def sort(self):
        self.__merge_sort(self.array)
        return self.array

def main():
    array = [9,1,8,2,7,3,6,4,5]
    m = MergeSort(array)
    print(m.sort())
    array = [1,2,3,4,5,6,7,8,9]
    m = MergeSort(array)
    print(m.sort())

main()

# O(nlogn) - O(nlogn) - O(nlogn)