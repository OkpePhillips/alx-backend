#!/usr/bin/python3
"""
MRUCache Module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching.
    """
    def __init__(self):
        """Initialize MRUCache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Function discard the most recently used item (MRU algorithm)
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item
            self.order.insert(0, key)

    def get(self, key):
        """
        Moves the accessed key to the beginning of the order list
        """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.insert(0, key)
            return self.cache_data[key]
        return None
