class HashTable(object):
    """implements a simple HastTable"""

    def __init__(self, size=1024):
        self._list_size = size
        self._bucket_list = [[] for bucket in xrange(0, size)]

    def hash(self, key):
        if not isinstance(key, basestring):
            raise TypeError("key must take a string")
        sum_ord = 0
        for letter in key:
            sum_ord += ord(letter)
        return sum_ord % self._list_size

    def set(self, key, value):
        hash = self.hash(key)
        for item in self._bucket_list[hash]:
            if item[0] == key:
                item[1] = value
                return
        self._bucket_list[hash].append([key, value])

    def get(self, key):
        hash = self.hash(key)
        for item in self._bucket_list[hash]:
            if item[0] == key:
                return item[1]
        raise KeyError("key not found in hash table")
