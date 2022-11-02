class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__elems = {}

    def add(self, elem):
        pos = self.hash(elem)
        if self.search(elem, pos) == -1:
            self.__elems.update({self.hash(elem): elem})
        return pos

    def resize(self, new_size):
        pass

    def search(self, elem, pos):
        if self.__elems.get(pos) == elem:
            return pos
        return -1

    def hash(self, elem):
        ascii_sum = 0
        for letter in elem:
            ascii_sum += ord(letter)
        return ascii_sum
