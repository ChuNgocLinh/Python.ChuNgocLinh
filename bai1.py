class Bai1:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def so_hoc(self):
        print("=== Phép toán số học ===")
        print("a + b =", self.a + self.b)
        print("a - b =", self.a - self.b)
        print("a * b =", self.a * self.b)
        print("a / b =", self.a / self.b)
        print("a ** b =", self.a ** self.b)

    def so_sanh(self):
        print("\n=== Toán tử so sánh ===")
        print("a > b:", self.a > self.b)
        print("a < b:", self.a < self.b)
        print("a == b:", self.a == self.b)
        print("a != b:", self.a != self.b) 

    def gan(self):
        print("\n=== Toán tử gán ===")
        x = self.a
        x += self.b
        print("x += b:", x)
        x -= self.c
        print("x -= c:", x)
        x *= self.b
        print("x *= b:", x)
        x /= self.c
        print("x /= c:", x)

    def logic(self):
        print("\n=== Toán tử logic ===")
        print("(a > b) and (b > c):", (self.a > self.b) and (self.b > self.c))
        print("(a > b) or (b < c):", (self.a > self.b) or (self.b < self.c))
        print("not(a > b):", not(self.a > self.b))

    def bit(self):
        print("\n=== Toán tử bit ===")
        print("a & b =", self.a & self.b)
        print("a | b =", self.a | self.b)
        print("a ^ b =", self.a ^ self.b)
        print("~a =", ~self.a)
        print("a << 3 =", self.a << 3)
        print("a >> 2 =", self.a >> 2)


# chạy chương trình
bai = Bai1(16, 3, 5)
bai.so_hoc()
bai.so_sanh()
bai.gan()
bai.logic()
bai.bit()