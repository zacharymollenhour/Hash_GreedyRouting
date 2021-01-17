
# Zachary Mollenhour #001462017
# Class that holds the hash table and uses the chaining method for collisions
class ChainHashTable(object):
    """
    Constructor for Chaining Hash Table
    Paramters of option capacity
    Assigns all of the buckets an empty list instance
    """
    def __init__(self, capacity = 10):
        self.hashTable = []
        #Loop through the hashtable and initialize with empty values
        for i in range(capacity):
            self.hashTable.append([])
    """
    Function responsible for Finding packages in the hash table
    """
    def find(self, key):
        tempBucket = hash(key) % len(self.hashTable)
        tempBucketList = self.hashTable[tempBucket]

        if key in tempBucketList:
            index = tempBucketList.index(key)
            return tempBucketList[index]

        else:
            return None
    """
    Function responsible for inserting new packages into the hash table
    """
    def insert(self, package):
        tempBucket = hash(package) % len(self.hashTable)
        tempBucketList = self.hashTable[tempBucket]

        # insert the item to the end of the bucket list.
        tempBucketList.append(package)
    """
    Function responsible for deleting a package from the hash table
    """
    def delete(self, key):
        tempBucket = hash(key) % len(self.hashTable)
        tempBucketList = self.hashTable[tempBucket]

        for key in tempBucketList:
            tempBucketList.remove(key)
        
