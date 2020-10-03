class PatternNaive(object):

    def __init__(self, pattern=None):
        if pattern == None:
            self.pattern = ""
        else:
            self.pattern = pattern

    def set_pattern(self, pattern=None):
        if pattern == None:
            return False
        else:
            self.pattern = pattern
            return True

    def check(self, string=""):

        m = len(self.pattern)
        n = len(string)

        if m > n:
            return -1
        answers = []
        pos = -2
        i,j = 0,0
        while i < n-m+1:
            s_pos, j = i, 0
            while j < m:
                #print(f"s : {string[s_pos]}\tp : {self.pattern[j]}")
                if string[s_pos] == self.pattern[j]:
                    j, s_pos = j+1, s_pos+1
                else:
                    break
            if j == m:
                pos = i
                answers.append(pos+1)
            i += 1

        return answers

    def __str__(self):
        return self.pattern
