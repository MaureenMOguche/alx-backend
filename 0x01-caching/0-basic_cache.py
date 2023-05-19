#!/usr/bin/env python3
""" 0-basic_cache.py """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache class """

    def put(self, key, item):
        """ Add item in cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get item from cache """
        return self.cache_data.get(key)
