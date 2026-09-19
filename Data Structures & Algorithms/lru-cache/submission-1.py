class Node:
    def __init__(self, value: int, key: int) -> None:
        self.value = value
        self.key = key
        self.next = self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def delete(self, node: Node) -> None:
        # remove from right side
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node: Node) -> None:
        head = self.left.next
        node.prev, node.next = self.left, head
        self.left.next = node
        head.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # update list
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.value
        return - 1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            del self.cache[key] # deleted the key
            self.delete(node)
        new_node = Node(value=value, key=key)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            del self.cache[self.right.prev.key]
            self.delete(self.right.prev)

        
        
    



        
