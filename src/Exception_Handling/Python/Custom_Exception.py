class Custom(Exception):

    def __init__(self, message):
        super().__init__(message)

def main():

    try:
        raise Custom("Custom Exception")
    except Exception as ex:
        print("EX : ",ex)

main()