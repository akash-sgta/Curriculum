import sys

INTMAX = sys.maxsize
max_ = -INTMAX
min_ = INTMAX

def max_min(array, x, y):
    global max_
    global min_

    mid = (x+y)//2
    if y-x > 2:
        max_min(array, x, mid)
        max_min(array, mid, y)
    else:
        array = array[x:y]
        if y-x == 1:
            array.append(array[0])
        max_ = max(max_, max(array[0], array[1]))
        min_ = min(min_, min(array[0], array[1]))
    
    return True

def main():

    array = list([9,1,8,2,7,3,6,4,5])
    print(max_min(array, 0, len(array)))
    print(f"max : {max_}")
    print(f"min : {min_}")

main()