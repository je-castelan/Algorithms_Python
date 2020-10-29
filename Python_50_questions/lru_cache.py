"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. 

If the number of keys exceeds the capacity from this operation, evict the least recently used key.
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.freq = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.cache.get(key, -1)
        if value != -1:
            self.__change_priority(key)
        print("Update freqs to {}".format(self.freq))   
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.cache) == self.capacity and not self.cache.get(key):
            self.cache.pop(self.freq[0])
            self.freq.pop(0)
        self.cache[key] = value
        self.__change_priority(key)
        print("---Cache: {}---Freqs are {}".format(self.cache,self.freq))
    
    def  __change_priority(self, key):
        if key in self.freq:
            self.freq.remove(key)
        self.freq.append(key)

    

if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1) # cache is {1=1}
    lRUCache.put(2, 2) # cache is {1=1, 2=2}
    print("printing {}".format(lRUCache.get(1)))    # return 1
    lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print("printing {}".format(lRUCache.get(2)))    # returns -1 (not found)
    lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print("printing {}".format(lRUCache.get(1)))    # return -1 (not found)
    print("printing {}".format(lRUCache.get(3)))    # return 3
    print("printing {}".format(lRUCache.get(4)))    # return 4

    print("*"*100)
    lRUCache = LRUCache(2)
    print("printing {}".format(lRUCache.get(2)))    # return -1 (not found)
    lRUCache.put(2, 6) # cache is {2=6}
    print("printing {}".format(lRUCache.get(1)))    # return -1 (not found)
    lRUCache.put(1, 5) # cache is {1=5, 2=6}
    lRUCache.put(1, 2) # cache is {1=2, 2=6}
    print("printing {}".format(lRUCache.get(1)))    # return 2
    print("printing {}".format(lRUCache.get(2)))    # return 6

    print("*"*100)
    lRUCache = LRUCache(2)
    lRUCache.put(2, 1) # cache is {2=1}
    lRUCache.put(1, 1) # cache is {2=1, 1=1}
    lRUCache.put(2, 3) # cache is {2=3, 1=1}
    lRUCache.put(4, 1) # cache is {2=3, 4=1}
    print("printing {}".format(lRUCache.get(1)))    # return -1
    print("printing {}".format(lRUCache.get(2)))    # return  3
    
    print("*"*100)
    lRUCache = LRUCache(3)
    lRUCache.put(1, 1) # cache is {1=1}
    lRUCache.put(2, 2) # cache is {2=2,1=1}
    lRUCache.put(3, 3) # cache is {3=3,2=2,1=1}
    lRUCache.put(4, 4) # cache is {4=4,3=3,2=2}
    print("printing {}".format(lRUCache.get(4)))    # return 4
    print("printing {}".format(lRUCache.get(3)))    # return 3
    print("printing {}".format(lRUCache.get(2)))    # return 2
    print("printing {}".format(lRUCache.get(1)))    # return -1
    lRUCache.put(5, 5) # cache is {5=5,4=4,3=3}
    