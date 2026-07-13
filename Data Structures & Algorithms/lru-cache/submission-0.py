class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Map key to Node
        # Dummy nodes to represent boundaries
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node):
        # Insert at the right (most recently used position)
        prev = self.right.prev
        nxt = self.right
        
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove from the left (least recently used position)
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]