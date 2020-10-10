class Hash(object):

    def __init__(self, size):
        self._size = size
        self._hash_table_chaining = dict()
    
    def __hash_util(self, val):
        ans = val % self._size
        return ans
    
    def find(self, val):
        key = self.__hash_util(val)
        if key not in self._hash_table_chaining.keys():
            return False
        else:
            for i in self._hash_table_chaining[key]:
                if i == val:
                    return True
        return False
    
    def add_element(self, val):

        if val == None or self.find(val):
            return False
        else:
            if 'int' not in str(type(val)):
                return False
            else:
                key = self.__hash_util(val)
                if key not in self._hash_table_chaining.keys():
                    self._hash_table_chaining[key] = list()
                self._hash_table_chaining[key].append(val)

        return True
    
    def delete_element(self, val):

        if val == None or not self.find(val):
            return False
        else:
            if 'int' not in str(type(val)):
                return False
            else:
                key = self.__hash_util(val)
                if key not in self._hash_table_chaining.keys():
                    pass
                else:
                    self._hash_table_chaining[key].remove(val)

        return True

def main():
    import random
    size = 100
    array = [(int(random.random() * 1000) + 1) for _ in range(size)]
    h = random.choice([size//2, size//3, size//4, size//5])
    if h < 3:
        h = 3

    hash = Hash(h)
    for i in array:
        hash.add_element(i)
    
    for i in range(10):
        print(hash.find(array[random.randrange(1,100)]))
    print(hash.find(69))

    for i in range(10):
        print(hash.delete_element(array[random.randrange(1,100)]))

main()

# O(1) - O(n)