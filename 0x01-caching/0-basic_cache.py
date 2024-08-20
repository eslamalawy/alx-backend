#!/usr/bin/python3
"""Create BasicCache class that inherits from BaseCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Define BasicCache """

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value associated with the given key """
        return self.cache_data.get(key)
