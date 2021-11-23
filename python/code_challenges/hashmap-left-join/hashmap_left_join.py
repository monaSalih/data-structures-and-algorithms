class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False



class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
        index = self.__hash(key)
        if self.__buckets[index]:
            linked_list = self.__buckets[index]
            current = linked_list.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def contains(self,key):
        idx=self.__hash(key)
        if self.__buckets[idx]:
            return self.__buckets[idx].includes(key)
        else:
            return False

def hash_left_join(hash_one,hash_two):
    arr = []
    for hash in hash_one.__buckets:
        if hash != None:
            current = hash.head
            while current.head:
                arr += [[current.vlaue[0],current.value[1]]]
                current = current.next

    for elem in arr:
        if hash_two.contains(elem[0]):
            res=hash_two.get(elem[0])
            arr += [res]
        else:
            arr += [None]
    return arr



