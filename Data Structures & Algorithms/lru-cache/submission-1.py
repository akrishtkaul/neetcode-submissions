class Node:
    
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = { }
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        
        if key not in self.hm:
            return -1
        node = self.hm[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])

        new_node = Node(key, value)
        self.insert(new_node)
        self.hm[key] = new_node
        
        if len(self.hm) > self.capacity:
            oldest_node = self.tail.prev
            self.remove(oldest_node)
            del self.hm[oldest_node.key]

        return

    def remove(self, node : Node) -> none:
        node.prev.next = node.next
        node.next.prev = node.prev

        return


    def insert(self, node : Node) -> none:
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

        

        return



        
        
        
