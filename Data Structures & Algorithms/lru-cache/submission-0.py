class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev

            prev, nxt = self.right.prev, self.right
            prev.next = nxt.prev = node
            node.next, node.prev = nxt, prev

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev
        self.cache[key] = Node(key, value)

        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = self.cache[key]
        self.cache[key].next, self.cache[key].prev = nxt, prev
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            prev, nxt = lru.prev, lru.next
            prev.next, nxt.prev = nxt, prev
            del self.cache[lru.key]
            # At capacity, remove LRU
        
