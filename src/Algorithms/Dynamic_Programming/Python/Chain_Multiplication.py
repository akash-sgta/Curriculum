def main():
    n = int(input)
    dims = list()
    for _ in range(n):
        dims.append(tuple(map(int, input().split())))
    
main()