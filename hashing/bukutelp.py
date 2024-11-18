class BukuTelpon:
    def _init_(self):
        self.size = 6
        self.map = [None] * self.size

    def _gethash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def add(self, key, value):
        key_hash = self._gethash(key)
        key_value = (key, value)
        
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            print("Key hash ", key_hash, " sudah terisi")
            return False
        
    def delete(self, key):
            key_hash = self._getHash(key)
            if self.map[key_hash] is None:
                return False
            for i in range(0, len(self.map[key_hash])):
                if self.map[key_hash][i][0] == key:
                    self.map[key_hash] = None
                    return True
            print("Key ",key, " tidak ditemukan")
            return False
    
    def print(self):
            print('---Buku Telepon----')
            for item in self.map:
                if item is not None:
                    print(str(item))

myTelpBook = BukuTelpon()
myTelpBook.add('Dendy', '08123456789')
myTelpBook.add('Yuan', '21746')
myTelpBook.add('Keni', '890314')

myTelpBook.print()