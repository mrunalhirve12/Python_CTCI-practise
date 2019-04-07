"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
"""
# WITH SETS: O(1) average case
class RandomizedSet(object):

    def __init__(self):
       
        #Initialize your data structure here.
       
        self.dataSet = set()

    def insert(self, val):
        
        #Inserts a value to the set. Returns true if the set did not already contain the specified element.
        #:type val: int
        #:rtype: bool
       
        if val in self.dataSet:
            return False
        else:
            self.dataSet.add(val)
            return True

    def remove(self, val):
        
        # Removes a value from the set. Returns true if the set contained the specified element.
        #:type val: int
        #:rtype: bool
        
        if val in self.dataSet:
            self.dataSet.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        
        # Get a random element from the set.
        # :rtype: int
        
        import random
        return random.choice(tuple(self.dataSet))
        #return random.sample(self.dataSet, 1) -- gives list
"""
# A list holding the elements and a hashmap mapping each element to its index:
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = {}
        self.arr = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        """
        1) Check if x is already present by doing a hash map lookup.
        2) If not present, then insert it at the end of the array.
        3) Add in hash table also, x is added as key and last array index as index.
        """
        if val in self.s:
            return False
        else:
            self.arr.append(val)
            self.length += 1
            self.s[val] = self.length - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val in self.s:
            """
            1) Check if x is present by doing a hash map lookup.
            2) If present, then find its index and remove it from hash map.
            3) Swap the last element with this element in array and remove the last element.
            Swapping is done because the last element can be removed in O(1) time.
            4) Update index of last element in hash map.
            """
            idx = self.s[val]
            last = self.arr[self.length - 1]
            self.arr[idx] = last
            self.s[last] = idx
            del self.s[val]
            self.arr.pop()
            self.length -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        """
        1) Generate a random number from 0 to last index.
        2) Return the array element at the randomly generated index.
        """
        import random
        idx = random.randint(0,self.length-1)
        return self.arr[idx]

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_1 = obj.insert(3)
param_1 = obj.insert(4)
param_2 = obj.remove(4)
param_2 = obj.remove(1)
param_3 = obj.getRandom()