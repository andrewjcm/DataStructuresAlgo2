from model.package import Package


class HashTable:
    def __init__(self, max_len: int = 40) -> None:
        """
        Instantiates a hash table.

        Space-Time: O(n)

        :param max_len: max number if unique keys, default is 40
        """
        self.MAX = max_len
        self.table = [[] for _ in range(max_len)]

    def hash_key(self, key: int) -> int:
        """
        Creates a hashed key.

        Space-Time: O(1)

        :param key: any object
        :return: hashed key
        """
        return hash(key) % self.MAX

    def insert(self, key: int, value: Package) -> bool:
        """
        Inserts an object into the hash table.

        Space-Time: O(1)

        :param key: any object as key
        :param value: any object to store
        :return: True if successfully inserted
        """
        loc = self.table[self.hash_key(key)]
        for i in loc:
            if i[0] == key:
                i[1] = value
                return True
        loc.append([key, value])
        return True

    def get(self, key: int, full_list: bool = False) -> Package:
        """
        Gets an object stored in the hash table. If full list is True
        get method will return entire chained list at the hash.

        Space-Time: O(1) -> O(n)

        :param key: hash key
        :param full_list: default is False
        :return: value stored in hash table or full list of chained objects
        """
        loc = self.table[self.hash_key(key)]
        for i in loc:
            if full_list:
                return i
            else:
                if i[0] == key:
                    return i[1]

    def remove(self, key: int, full_list: bool = False) -> None:
        """
        Removes a key-value object from the hash table. If full_list is
        True, remove method will remove entire chained list of key-value
        objects.

        Space-Time: O(1) -> O(n)

        :param key: hash key
        :param full_list: default is False
        :return: None
        """
        loc = self.table[self.hash_key(key)]
        if full_list:
            loc = []
        else:
            for i in loc:
                if i[0] == key:
                    loc.remove([i[0], i[1]])
