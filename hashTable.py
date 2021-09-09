import math

# This class implements the hash table data structure. Used https://www.youtube.com/watch?v=9HFbhPscPU0 as reference.
class HashTable:
    def __init__(self):
        self.tableLength = 64
        self.initialize = self.tableLength * [None]

    # Creates hash value using multiplication method as hash function.
    def _create_hash_value(self, key):
        hash = 0
        for i in str(key):
            hash += ord(i)

        constA = (5 ** 0.5 + 1)/2
        hashValue = math.floor(self.tableLength*(hash*constA - math.floor(hash*constA)))
        return hashValue

    # Insert method for adding entries to the hash table.
    def insert(self, key, value):
        keyHash = self._create_hash_value(key)
        keyValue = [key, value]

        if self.initialize[keyHash] is None:
            self.initialize[keyHash] = list([keyValue])
            return True
        else:
            for entry in self.initialize[keyHash]:
                if entry[0] == key:
                    entry[1] = value
                    return True
            self.initialize[keyHash].append(keyValue)
            return True

    # Look-up function for returning values given a specific key.
    def retrieve(self, key):
        keyHash = self._create_hash_value(key)

        if self.initialize[keyHash] is not None:
            for entry in self.initialize[keyHash]:
                if entry[0] == key:
                    return entry[1]
        return None

    # Delete method for removing entries from the hash table.
    def remove(self, key):
        keyHash = self._create_hash_value(key)

        if self.initialize[keyHash] is None:
            return False
        for i in range(0,len(self.initialize[keyHash])):
            if self.initialize[keyHash][i][0] == key:
                self.initialize[keyHash].pop(i)
                return True

    # Print method for displaying the current entries in the hash table.
    def print(self):
        print('Hash Table')
        for entry in self.initialize:
            if entry is not None:
                print(entry)