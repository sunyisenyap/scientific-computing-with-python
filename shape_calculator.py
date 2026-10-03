class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        # Membuat gambar dengan mengulang string "*" sebanyak width, 
        # lalu menambahkan \n, dan mengulang keseluruhan sebanyak height
        return (("*" * self.width) + "\n") * self.height

    def get_amount_inside(self, shape):
        # Menghitung berapa kali shape bisa muat di dalam self (tanpa rotasi)
        # Menggunakan integer division (//) agar hasilnya bulat ke bawah
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        # Memanggil __init__ dari class induk (Rectangle) dengan width dan height yang sama
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    # Override metode set_width dari Rectangle agar mengubah width DAN height sekaligus
    def set_width(self, width):
        self.set_side(width)

    # Override metode set_height dari Rectangle agar mengubah width DAN height sekaligus
    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"