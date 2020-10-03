class PatternKMP(object):

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

    def __create_pi_table(self):

        m = len(self.pattern)
        self.pi_array = [0 for i in range(m)]
        length = 0
        i = 1

        while i < m:
            if self.pattern[i]== self.pattern[length]:
                length += 1
                self.pi_array[i] = length
                i += 1
            else:
                if length != 0:
                    length = self.pi_array[length-1]
                else:
                    self.pi_array[i] = 0
                    i += 1

    def check(self, string=""):
        m = len(self.pattern)
        n = len(string)

        if m > n:
            return -1

        i, j = 0, 0
        answers = []
        while i < n:
            if self.pattern[j] == string[i]:
                i += 1
                j += 1

            if j == m:
                answers.append(i-j+1)
                j = self.pi_array[j-1]
            elif i < n and self.pattern[j] != string[i]:
                if j != 0:
                    j = self.pi_array[j-1]
                else:
                    i += 1

        return answers

'''
AABAACAADAABAABA
AABA
'''
