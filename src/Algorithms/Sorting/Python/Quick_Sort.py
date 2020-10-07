class QuickSort(object):

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

    def __quick_sort(self, array, l, h):

        if l < h:
            # partition
            i = l
            j = h-1
            pivot = array[l]
            # trying to replicate do_while
            while i < j:
                while array[i] <= pivot:
                    i += 1
                    if i >= h:
                        i = h-1
                        break
                while array[j] > pivot:
                    j -= 1
                    if j < l:
                        j = l
                        break

                if i < j:
                    array[i],array[j] = array[j],array[i]
        
            array[j], array[l] = array[l], array[j]
            p = j
            # ----------
            self.__quick_sort(array, l, p)
            self.__quick_sort(array, p+1, h)
        
        return True

    def sort(self):
        self.__quick_sort(self.array, 0, self.size)
        return self.array

def main():
    array = [9,1,8,2,7,3,6,4,5]
    m = QuickSort(array)
    print(m.sort())
    array = [1,2,3,4,5,6,7,8,9]
    m = QuickSort(array)
    print(m.sort())

main()

# O(n^2) - O(nlogn) - O(nlogn)