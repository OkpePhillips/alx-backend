#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """ Assigns item value to key in self.cache_data
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
