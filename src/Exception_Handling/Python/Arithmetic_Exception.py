def main():
    i = 10
    j=0
    k = int(input())

    try:
        j = i // k
    except Exception as ex:
        print("EX : ",ex)
    print("OP : ",j)

main()