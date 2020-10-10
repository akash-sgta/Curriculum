from my_list import List

def bubble_sort(self):
    size = len(self)
    for i in range(0, size - 1):
        for j in range(0, size - 1 - i):
            if self[j] > self[j+1]:
                self[j], self[j+1] = self[j+1], self[j]
        
    return True

def main():
    List.sort = bubble_sort

    array = List(9,1,8,2,7,3,6,4,5)
    print(array.sort())
    print(array)
    array = List(1,2,3,4,5,6,7,8,9)
    print(array.sort())
    print(array)

main()

# O(n^2) - O(n^2) - O(n^2)