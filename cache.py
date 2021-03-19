from collections import OrderedDict


class LRUCache:

    # initializing capacity
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: str) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: str, value: dict) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > int(self.capacity):
            self.cache.popitem(last=False)
