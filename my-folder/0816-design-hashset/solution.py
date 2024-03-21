class MyHashSet(object):

    def __init__(self):
        self.set=[] 

    def add(self, key):
       if key not in self.set:
        self.set.append(key)

    def remove(self, key):
         if key in self.set:
            self.set.remove(key)

    def contains(self, key):
        return True if key in self.set else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
