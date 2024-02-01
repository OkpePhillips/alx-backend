#!/usr/bin/python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initializes the FIFOCache instance
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Assigns item value to key in self.cache_data (FIFO)
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
