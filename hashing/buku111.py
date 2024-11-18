class BukuTelepon:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _getHash(self, key):
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)  # getting ASCII value
        return hash_value % self.size

    def _probing(self, key):
        for index in range(self.size):
            probeHash = self._linearProbing(key, index)
            # valid if index is None or flagged as deleted
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash
        return None

    # Perform linear probing
    def _linearProbing(self, key, index):
        return (self._getHash(key) + index) % self.size

    # Add key to hash table
    def add(self, key, value):
        key_hash = self._getHash(key)
        key_value = (key, value)

        if self.map[key_hash] is None:
            self.map[key_hash] = key_value
            return True
        else:
            key_hash = self._probing(key)
            if key_hash is None:
                print("Buku telephone sudah penuh")
                return False

        self.map[key_hash] = key_value
        return True  # Successfully added

    def getPhoneNumber(self, key):
        key_hash = self._getHash(key)
        if (self.map[key_hash] is not None) and (self.map[key_hash] != 'deleted'):
            for index in range(self.size):
                # Searching with probing
                probe_hash = self._linearProbing(key, index)
                # Check if the key matches the data to return
                if self.map[probe_hash] is not None and self.map[probe_hash][0] == key:
                    return self.map[probe_hash][1]

        print("Key ", key, " tidak ditemukan")
        return None

    def delete(self, key):
        key_hash = self._getHash(key)
        if self.map[key_hash] is None:
            print("Key tidak ditemukan")
            return False

        for index in range(self.size):
            # Deleting with linear probing
            probe_hash = self._linearProbing(key, index)
            # Check if the key matches the data to delete
            if self.map[probe_hash] is not None and self.map[probe_hash][0] == key:
                print("Deleting ", key)
                self.map[probe_hash] = "deleted"
                return True

        print("Key ", key, " tidak ditemukan")
        return False

    def print(self):
        print('---Buku Telephone----')
        for item in self.map:
            if item is not None and item != 'deleted':
                print(f"{item[0]}: {item[1]}")

# Testing the implementation
h = BukuTelepon()
h.add('Dendy', '567-8888')
h.add('Yuan', '293-6753')
h.add('Anton', '333-8233')
h.add('Adi', '293-8625')
h.add('Dida', '293-8625')
h.print()
print(h.getPhoneNumber('Dendy'))  # Should return '567-8888'
h.delete('Dida')
h.print()