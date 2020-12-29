def binary_search(key, array, l, h):

    if l <= h:
        mid = l + (h-l)//2
        if key == array[mid]: 
            return mid+1
        elif key < array[mid]:
            return binary_search(key, array, l, mid-1)
        else:
            return binary_search(key, array, mid+1, h)
    return None
###
## you can just do it like this though
## if __name__ == "__main__" :
##    bla bla
###
def main():

    array = list([9,1,8,2,7,3,4,6,5])
    array.sort()
    print(binary_search(2, array, 0, len(array)-1))
    print(binary_search(21, array, 0, len(array)-1))

main()