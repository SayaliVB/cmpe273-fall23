import hashlib
import math

class BloomFilter:
    def __init__(self, size, num_hashes, salt=None):
        self.size = size
        self.num_hashes = num_hashes
        self.salt = salt or ''
        self.bit_array = [0] * size

    def add(self, element):
        for i in range(self.num_hashes):
            digest = hashlib.sha1((self.salt + str(element) + str(i)).encode('utf-8')).hexdigest()
            index = int(digest, 16) % self.size
            self.bit_array[index] = 1
    
    def lookup(self, element):
        for i in range(self.num_hashes):
            digest = hashlib.sha1((self.salt + str(element) + str(i)).encode('utf-8')).hexdigest()
            index = int(digest, 16) % self.size
            if self.bit_array[index] != 1:
                return False
        return True
