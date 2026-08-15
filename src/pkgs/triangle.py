class Triangle:
    def __init__(self, va: float, vb: float, vc: float):
        self.a = va
        self.b = vb
        self.c = vc

    def equilateral(self):
        if self.a == self.b == self.c:
            print("Triangle is equilateral")
        else:
            print("Triangle is not equilateral")

    def isosceles(self):
        if self.a == self.b or self.b == self.c or self.a == self.c:
            print("Triangle is iscosceles")
        else:
            print("Triangle is not iscosceles")

    def scalene(self):
        if self.a != self.b and self.b != self.c and self.a != self.c:
            print("Triangle is scalene")
        else:
            print("Triangle is not scalene")


if __name__ == "__main__":
    t = Triangle(
        float(input("side 1: ")), float(input("side 2: ")), float(input("side 3: "))
    )
    t.equilateral()
    t.isosceles()
    t.scalene()
