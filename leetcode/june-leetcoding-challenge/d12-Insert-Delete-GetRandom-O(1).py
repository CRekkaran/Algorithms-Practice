import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = 0
        self.ds = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if(val not in self.ds):
            self.ds[val] = 1
            self.lst.append(val)
            self.num += 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if(val in self.ds):
            del self.ds[val]
            self.num += 1
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # On average, the while loop will run for constant number of times only.
        # Thus, time complexity in average remains O(1)
        n = len(self.lst)
        temp = int(random.random()*n)
        while(self.lst[temp] not in self.ds):
            temp = int(random.random()*n)
        return self.lst[temp]
    
        # list(map.items()) would take O(n) time. Thus not opted.
        # return random.choice(list(self.ds.items()))[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
