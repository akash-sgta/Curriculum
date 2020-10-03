class PatternZ(object):

    def __init__(self, pattern=None):
        if pattern != None:
            self.pattern = pattern
            self.__create_pi_table()
        else:
            self.pi_table = None

    def set_pattern(self, pattern=None):
        if pattern == None:
            return False
        else:
            self.pattern = pattern
            self.__create_pi_table()
            return True
    #def check(self, string):

    def __str__(self):
        s = []
        m = len(self.pattern)
        for i in range(m):
            s.append([self.pattern[i], self.pi_array[i]])
        return str(s)
