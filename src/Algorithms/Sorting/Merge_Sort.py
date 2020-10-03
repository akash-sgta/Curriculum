class MergeSort(object):

    def __init__(self, array_, size_):
        self.array = array_
        self.size = size_

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

    def sort(self):
        self.__merge_sort(self.array)
        return self.array
'''
m = MergeSort([9,1,8,2,7,3,6,4,5], 9)
print(m.sort())'''