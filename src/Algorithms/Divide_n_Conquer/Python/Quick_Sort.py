class List(list):
    def __init__(self, *args):
        super().__init__(args)
    def sort(self):
        raise Exception("override on implementation")
    def util(self):
        raise Exception("override on implementation")

def partition(self, l, h):

    i = l
    j = h-1
    pivot = self[l]
    # trying to replicate do_while
    while i < j:
        while self[i] <= pivot:
            i += 1
            if i >= h:
                i = h-1
                break
        while self[j] > pivot:
            j -= 1
            if j < l:
                j = l
                break

        if i < j:
            self[i],self[j] = self[j],self[i]
        
    self[j], self[l] = self[l], self[j]

    return j

def quick_sort(self, l, h):

    if l < h:
        p = self.util(l, h)
            
        self.sort(l, p)
        self.sort(p+1, h)
        
    return True

def main():
    List.sort = quick_sort
    List.util = partition

    array = List(9,1,8,2,7,3,6,4,5)
    print(array.sort(0, len(array)))
    print(array)
    array = List(1,2,3,4,5,6,7,8,9)
    print(array.sort(0, len(array)))
    print(array)

main()

# O(n^2) - O(nlogn) - O(nlogn)