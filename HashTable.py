import HashTable
import csv

"""
    HashMap Class that handles creation of hashtable
 """
class HashMap:

    #Initialize hashmap Object
    def __init__(self, capacity = 10):
        self.bucket = []
        for i in range(capacity):
            self.bucket.append([])

    # Create hash key -> O(1)
    def create_hash_key(self, key):
        return int(key) % len(self.bucket)

    # Insert package into hash table -> O(n)
    def insert(self, key, value):
        key_hash = self.create_hash_key(key)
        key_value = [key, value]

        if self.bucket[key_hash] == None:
            self.bucket[key_hash] = list([key_value])
            return True
        else:
            for pair in self.bucket[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.bucket[key_hash].append(key_value)
            return True

    # Update package in hash table -> O(n)
    def update(self, key, value):
        key_hash = self.create_hash_key(key)
        if self.bucket[key_hash] != None:
            for pair in self.bucket[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('There was an error with updating on key: ' + key)

    # Get a value from hash table -> O(n)
    def get_value(self, key):
        key_hash = self.create_hash_key(key)
        if self.bucket[key_hash] != None:
            for pair in self.bucket[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Delete a value from hash table -> O(n)
    def delete(self, key):
        key_hash = self.create_hash_key(key)

        if self.bucket[key_hash] == None:
            return False
        for i in range(0, len(self.bucket[key_hash])):
            if self.bucket[key_hash][i][0] == key:
                self.bucket[key_hash].pop(i)
                return True
        return False