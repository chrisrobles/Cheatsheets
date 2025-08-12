class hashTable:
    def __init__(self):
        #Create empty Hash Table with Chaining in mind
        self.table = [[] for _ in range(10)]
    
    def hashing(self, val):
        return val % 10
    
    def insert(self, val):
        self.table[self.hashing(val)].append(val)

    def search(self, val):
        index = self.hashing(val)
        for v in self.table[index]:
            if(v == val):
                return index
        return -1
myHash = hashTable()
myHash.insert(10)
myHash.insert(15)
myHash.insert(25)
print(myHash.table)
print(myHash.search(15))
print(myHash.search(23))
