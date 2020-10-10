def max_min(array, x, y):
    if x >= y:
        return max(array[x], array[y]), min(array[x], array[y])
    else:
        max_1, min_1 = max_min(array, x, (x+y)//2)
        max_2, min_2 = max_min(array, (x+y)//2 + 1, y)
    return max(max_1, max_2), min(min_1, min_2)

def main():
    array = list([9,1,8,2,7,3,6,4,5])
    print(max_min(array, 0, len(array)-1))

main()