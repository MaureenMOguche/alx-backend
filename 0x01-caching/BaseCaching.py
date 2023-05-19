#!/usr/bin/python3
""" BaseCaching module"""


class BaseCaching():

    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliazion method """
        self.cache_data = {}

    def print_cache(self):
        """ Print cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add item in the cache"""
        raise NotImplementedError(
            "put should be implemented")

    def get(self, key):
        """ Get item using key """
        raise NotImplementedError(
            "get should be implemented")
