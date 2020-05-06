class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.tail = None

    def push(self, key, value):
        if self.key == key:
            self.value = value
            return
        
        while self.next:
            if self.next.key == key:
                self.next.value = value
                return
            self.next = self.next.next

        if not self.next:
            self.next = HashTableEntry(key, value)
            self.tail = self.next
        else:
            self.tail.next = HashTableEntry(key, value)
            self.tail = self.tail.next
    
    def search(self, key):
        if self.key == key:
            return self.value
        else:
            while self.next:
                if self.next.key == key:
                    return self.next.value
                self.next = self.next.next
        return None

    def remove(self, key):
        if self.key == key:
            if self.next:
                 self.key = self.next.key
                 self.value = self.next.value
                 self.next= self.next.next
            else:
                self.key = None
                self.value = None
            return
        else:
            while self.next:
                if self.next.key == key:
                    if self.next.next:
                        self.next.key = self.next.next.key
                        self.next.value = self.next.next.value
                        self.next = self.next.next
                    else:
                        self.next = None
                    return 
                self.next = self.next.next
        print(f"warning: {key} not found")
   


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity= capacity
        self.storage = [None] * capacity    

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hash = FNV_offset_basis

        encodedKey = key.encode()
        for c in encodedKey:
            hash *= FNV_prime
            hash ^= c

        return hash


    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381

        encodedKey = key.encode()
        for c in encodedKey:
            hash = ((hash << 5) + hash) + c

        return hash
 
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.auto_resize()
        index = self.hash_index(key)
        if not self.storage[index]:
            self.storage[index] = HashTableEntry(key, value)
        else:
            self.storage[index].push(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if not self.storage[index]:
                print(f"{key} not found")
        else:
                self.storage[index].remove(key)
        self.auto_resize()

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if not self.storage[index]:
            return None
        else:
            return self.storage[index].search(key)   

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.capacity *= 2
        ht = HashTable(self.capacity)
        for i in self.storage:
          if i:  
            ht.put(i.key, i.value)
            while i.next:
                ht.put(i.next.key, i.next.value)
                i.next = i.next.next
        self.storage = ht.storage
    
    def down_size(self):
         """
         Doubles the capacity of the hash table and
         rehash all key/value pairs.
         Implement this.
         """
         self.capacity *= .5
         ht = HashTable(self.capacity)
         for i in self.storage:
           if i:  
             ht.put(i.key, i.value)
             while i.next:
                 ht.put(i.next.key, i.next.value)
                 i.next = i.next.next
         self.storage = ht.storage
    
    def auto_resize(self):
        load_factor_up=0.7
        load_factor_down=0.2
        minimum_slot = 128
    
        count=0
        factor = count / self.capacity
        for i in self.storage:
            if i:
                count += 1
        if factor > load_factor_up:
            self.resize()
        elif factor < load_factor_down and count > minimum_slot:
            self.down_size()



if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
