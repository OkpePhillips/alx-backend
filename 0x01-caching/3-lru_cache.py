#!/usr/bin/python3
"""
LRUCache Module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Inheriting from Base Caching and implementing LRUCache"""
    def __init__(self):
        """
        Initialising the super cache class.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Method discard the least recently used item.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Move accessed key to the end of list as the most recently used.
        """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
