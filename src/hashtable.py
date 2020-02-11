import hashlib

# Linked List hash table key/value pair
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return '{key: '+self.key+', value: '+str(self.value)+' }'

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)
    
    
    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
    def insert(self, key, value):
        # hash the key
        index = self._hash_mod(key)
        self.storage += 1
        node = self.storage[index]
        # if index already exists print warning
        if node is not None:
            print(f"Warning: Collision has occured at {index}")
            self.storage[index] = LinkedPair(key, value)
            # collision handling / iterate to end of SLL at index
            # node = self.storage[index]
            prev = node
            while node is not None:
                prev = node
                node = node.next
            # add new node to the end of list at key/value pair
            prev.next = LinkedPair(key, value)
        # else add index to storage
        else: 
            self.storage[index] = (key, value)
                       
        
    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hash key into index in hashtable / find hased index
        index = self._hash_mod(key)


        if self.storage[index] is not None:
            # if the hashed key is found in index 0
            if self.storage[index][0] == key:
                self.storage[index] = None      
            else: 
                print(f"Warning: Collision has occured at index {index}")
        else:
            print(f"WARNING: key {key} not found!")

        return 


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                return self.storage[index][1]
            else: 
                print(f"WARNING: Collision has occurred at index {index}")
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for item in old_storage:
            self.insert(item[0], item[1])



if __name__ == "__main__":
    # My Own Tests
    my_ht = HashTable(2)

    my_ht.insert("bobby", "liberti")
    my_ht.insert("iris", "liberti")
    my_ht.insert("milo", "liberti")
    # my_ht.remove("bobby")

    print(my_ht.storage)
    
    # Lambda Tests
    # ht = HashTable(2)
    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
