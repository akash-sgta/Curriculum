class List(list):

    def __init__(self, *args):
        super().__init__(args)
    
    def sort(self):
        raise Exception("override on implementation")

    def util(self):
        raise Exception("override on implementation")