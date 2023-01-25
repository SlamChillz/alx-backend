#!/usr/bin/python3
"""Basic Cache implementation Class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache implementaion class

    Attributes:
        MAX_ITEMS: number of items that can be store in the cache
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
