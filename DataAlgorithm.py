class Entry:
    def __init__(self, item, priority):
        self.priority = priority
        self.item = item

class PriorityQueue:
    def __init__(self):
        self.entries = []

    def insert(self, item, priority):
        tempElement = Entry(item, priority)
        contain = False

        for i in range(0, len(self.entries)):
            if self.entries[i].priority <= tempElement.priority:
                self.entries.insert(i, tempElement)
                contain = True
                break
        if contain == False:
            self.entries.append(tempElement)
    

    def findMin(self):
        return min(self.entries).item
    
    def removeMin(self):
        entry = min(self.entries)
        self.entries.remove(entry)
        return entry.item
