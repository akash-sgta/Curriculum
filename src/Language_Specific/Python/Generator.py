def generate_squares_of_natural_numbers(num):

    for i in range(1, num+1):
        yield i*i


def main():

    n = 100
    ans = generate_squares_of_natural_numbers(n)

    while True:

        try:
            print(next(ans))
        except StopIteration:
            break
        else:
            print("Did some job on the value, now give next value")

main()