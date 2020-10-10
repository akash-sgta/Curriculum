from my_list import List

def merge(self, l, mid, h):

    print("in")
    left_array = self[l:mid]
    n = len(left_array)
    right_array = self[mid:h]
    m = len(right_array)

    print(left_array, right_array)
    input()

    i=j=k=0

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
        print(l, h)
        input()
        self.sort(l, middle)
        self.sort(middle, h)

        self.util(l, middle, h)

    return True

def main():
    List.sort = merge_sort
    List.util = merge

    array = List(9,1,8,2,7,3,6,4,5)
    print(array.sort(0, len(array)))
    print(array)
    array = List(1,2,3,4,5,6,7,8,9)
    print(array.sort(0, len(array)))
    print(array)

main()

# O(nlogn) - O(nlogn) - O(nlogn)