class HashTable:
    def __init__(self):
        self.__elems = {}
        self.len = 0

    def add(self, elem):
        pos = self.hash(elem)
        if self.search(elem) == -1:
            self.__elems.update({self.hash(elem): elem})
            self.len += 1
        return pos

    def resize(self, new_size):
        pass

    def search(self, elem):
        pos = self.hash(elem)
        if self.__elems.get(pos) == elem:
            return pos
        return -1

    def hash(self, elem):
        ascii_sum = 0
        for letter in elem:
            ascii_sum += ord(letter)
        return ascii_sum
