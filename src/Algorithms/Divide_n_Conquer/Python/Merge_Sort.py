class List(list):
    def __init__(self, *args):
        super().__init__(args)
    def sort(self):
        raise Exception("override on implementation")
    def util(self):
        raise Exception("override on implementation")

def merge(self, l, mid, h):

    left_array = self[l:mid+1]
    n = len(left_array)
    right_array = self[mid+1:h+1]
    m = len(right_array)

    i=j=0
    k=l

    while i < n and j < m:
        if left_array[i] < right_array[j]:
            self[k] = left_array[i]
            i += 1
        else:
            self[k] = right_array[j]
            j += 1
        k += 1
            
    while i < n:
        self[k] = left_array[i]
        k += 1
        i += 1
            
    while j < m:
        self[k] = right_array[j]
        k += 1
        j += 1

def merge_sort(self, l, h):

    if l < h:
        middle = l + (h-l)//2
        
        self.sort(l, middle)
        self.sort(middle+1, h)

        self.util(l, middle, h)


def main():
    List.sort = merge_sort
    List.util = merge

    array = List(9,1,8,2,7,3,6,4,5)
    n = len(array)
    print(array.sort(0, n-1))
    print(array)
    array = List(1,2,3,4,5,6,7,8,9)
    n = len(array)
    print(array.sort(0, n-1))
    print(array)

main()

# O(nlogn) - O(nlogn) - O(nlogn)