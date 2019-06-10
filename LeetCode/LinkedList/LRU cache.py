"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
import collections


#Doubly linked lists to store the (key, val) pair, and dictionary mapping key to the corresponding node.
#Time complexity for both get and put : O(1). Space complexity: O(capacity)

# CREATING LISTNODE
class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
    
        #type capacity: int
        
        # initialize ListNode
        self.head = ListNode(-1, -1)
        # initialize tail to head
        self.tail = self.head
        # create a dict
        self.key2node = {}
        # size of the queue
        self.capacity = capacity
        # initialize size of queue
        self.length = 0

    def get(self, key):

        #type key: int
        #rtype: int

        # if val not present return -1
        if key not in self.key2node:
            return -1
        # get not and val
        node = self.key2node[key]
        val = node.val
        # if node has next(you have to make it latest)
        if node.next:
            # store nodes prev as nodes next and vice versa
            node.prev.next = node.next
            node.next.prev = node.prev
            # add tails next as node(making it new node)
            self.tail.next = node
            # add nodes prev as tail and next to none and self.tails as node return val
            node.prev = self.tail
            node.next = None
            self.tail = node
        return val

    def put(self, key, value):
    
        #type key: int
        #type value: int
        #rtype: None

        if key in self.key2node:
            # add get val and node
            node = self.key2node[key]
            node.val = value
            #if node has next, repeat same as i get to get node in front(tail)
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
        # if not in LL
        else:
            # create a node with key and val, add in dict.
            node = ListNode(key, value)
            self.key2node[key] = node
            # putting the element to last
            self.tail.next = node
            # setting prev element to tail
            node.prev = self.tail
            # add node in tail, increase the length
            self.tail = node
            self.length += 1
            # chk if length greater than 1
            if self.length > self.capacity:
                # store heads next
                remove = self.head.next
                # store head.next.next in head(as head has old nodes)
                self.head.next = self.head.next.next
                # add prev as head to node
                self.head.next.prev = self.head
                # delete node & decrease length
                del self.key2node[remove.key]
                self.length -= 1


#=======================================================================================================================
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        #set capacity of cache and dict
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #if key is not present, return -1
        if key not in self.dic:
            return -1
        #get val if present
        val = self.dic[key]
        #move to end(front)
        self.dic.move_to_end(key)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        #add in dict and add at top
        self.dic[key] = value
        self.dic.move_to_end(key)
        #if greater than capacity, pop items
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
obj.put(2, 2)
obj.get(1)
obj.put(3, 3);
obj.get(2);
obj.put(4, 4);
obj.get(1);
obj.get(3);
obj.get(4);
