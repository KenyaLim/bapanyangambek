class BukuTelpon:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _gethash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def probing(self, key):
        for index in range(self.size):
            probeHash = self.linearProbing(key, index)
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash
        return None  
    
    def linearProbing(self, key, index):
        return (self._gethash(key) + index) % self.size
    
    def add(self, key, value):
        key_hash = self._gethash(key)
        if self.map[key_hash] is not None:
            key_hash = self.probing(key)
            if key_hash is None:
                print("Buku Telepon penuh")
                return False
        self.map[key_hash] = (key, value)
        return True 

    def delete(self, key):
        key_hash = self._gethash(key)
        if self.map[key_hash] is None:
            print("Key tidak ditemukan")
            return False
        
        for i in range(self.size):
            probe_hash = (key_hash + i) % self.size
            if self.map[probe_hash] is None:
                print("Key tidak ditemukan")
                return False
            if self.map[probe_hash][0] == key:
                self.map[probe_hash] = 'deleted'
                return True
        print("Key tidak ditemukan")
        return False
    
    def print(self):
        print('---Buku Telepon----')
        for item in self.map:
            if item is not None and item != 'deleted':
                print(f"{item[0]}: {item[1]}")

h = BukuTelpon()
h.add('Dendy', '567-8888')
h.add('Yuan', '293-6753')
h.add('Anton', '333-8233')
h.add('Adi', '293-8625')
h.add('Dida', '293-8625')
h.print()
h.delete('Dida')
h.print()