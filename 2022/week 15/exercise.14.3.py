import string
import random



'''
14.3: Implement a Python dictionary using a Hashtable. Your hashtable should have a
get(), add(), and hash() methods. Showcase those methods working. You may either
create your own hash function, or use the Python built in hash function.
'''



class Hashtable:
    class Node:
        def __init__(self, key, val, next=None):
            self.key = key
            self.val = val
            self.next = next
            
    def __init__(self, n_buckets=1000):
        self.buckets = [None] * n_buckets
        
    def add(self, key, val):
        bidx = hash(key) % len(self.buckets)
        n = self.buckets[bidx]
        # WHILE THERES AN ITEM IN THE INDEX OF OUR TABLE
        while n:
            if key == n.key:
                n.val = val
                return
            n = n.next

        else:
            self.buckets[bidx] = Hashtable.Node(key, val, next=self.buckets[bidx])
            # print(self.buckets[bidx].next)
    
    def get(self, key):
        bidx = hash(key) % len(self.buckets)
        n = self.buckets[bidx]
        while n:
            if key == n.key:
                return n.val
            n = n.next
        else:
            raise KeyError(str(key))
    
    def contains(self, key):
        try:
            _ = self[key]
            return True
        except:
            return False





if __name__ == "__main__":
    # INIT HASH-TABLE
    table = Hashtable(24)


    # MOCK DATA
    alphabet_indicies = random.sample(range(0, len(string.ascii_lowercase)), len(table.buckets))


    # ADDING PAIRS TO TABLE
    keys_titles = []
    for x in range(0 , len(table.buckets) , 1):
        key = string.ascii_lowercase[alphabet_indicies[x]] * random.randint(1,6)
        table.add(key, alphabet_indicies[x])
        print(key, alphabet_indicies[x], "ADDED ON INDEX",end=" ")
        print(hash(key) % len(table.buckets))
        keys_titles.append(key)


    print()


    # GETTING VALUES FROM TABLE
    for x in range(0 , len(keys_titles) , 1):
        value = table.get(keys_titles[x])
        print(f"GETTING {keys_titles[x]}: {value}")