class HashTable:
    def __init__(self):
        # Inisialisasi collection sebagai dictionary kosong
        self.collection = {}

    def hash(self, key):
        # Menghitung nilai hash dengan menjumlahkan nilai Unicode (ASCII) dari setiap karakter
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hash_key = self.hash(key)
        
        # Jika hash_key belum ada di collection, buat dictionary kosong untuk menampungnya
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
            
        # Simpan key-value pair di dalam dictionary pada hash_key tersebut
        self.collection[hash_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)
        
        # Cek apakah hash_key ada, dan apakah key asli ada di dalamnya
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                # Hapus hanya key-value pair spesifik, bukan seluruh dictionary di index tersebut
                del self.collection[hash_key][key]

    def lookup(self, key):
        hash_key = self.hash(key)
        
        # Cek keberadaan key
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                return self.collection[hash_key][key]
                
        # Kembalikan None jika tidak ditemukan
        return None