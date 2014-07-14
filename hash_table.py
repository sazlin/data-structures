class HashTable(object):
    """implements a simple HastTable"""

    def __init__(self, size=1024):
        self._list_size = size
        self._bucket_list = [[] for bucket in xrange(0, size)]

    def _hash(self, key):
        if not isinstance(key, basestring):
            raise TypeError("key must take a string")
        sum_ord = 0
        for letter in key:
            sum_ord += ord(letter)
        return sum_ord % self._list_size
