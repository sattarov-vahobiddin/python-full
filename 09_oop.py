# ============================================================
# 09 - OOP (OBYEKTGA YO'NALTIRILGAN DASTURLASH)
# ============================================================

# --- Oddiy Class ---
class Inson:
    tur = "Homo sapiens"    # class atribut

    def __init__(self, ism, yosh):
        self.ism = ism      # instance atribut
        self.yosh = yosh

    def salomlash(self):
        print(f"Salom, men {self.ism}!")

    def __str__(self):
        return f"Inson({self.ism}, {self.yosh})"

    def __repr__(self):
        return f"Inson('{self.ism}', {self.yosh})"

    def __eq__(self, other):
        return self.ism == other.ism

    @classmethod
    def yaratish(cls, matn):
        ism, yosh = matn.split(",")
        return cls(ism.strip(), int(yosh.strip()))

    @staticmethod
    def tavsiflash():
        print("Bu Inson klassi")

    @property
    def tolik_info(self):
        return f"{self.ism} ({self.yosh} yosh)"

    @tolik_info.setter
    def tolik_info(self, qiymat):
        ism, yosh = qiymat.split(",")
        self.ism = ism.strip()
        self.yosh = int(yosh.strip())


ali = Inson("Ali", 25)
ali.salomlash()
print(ali)
print(ali.tolik_info)
ali.tolik_info = "Vali, 30"
print(ali.tolik_info)

a1 = Inson.yaratish("Soli, 22")
print(a1)
Inson.tavsiflash()


# --- Meros (Inheritance) ---
class Talaba(Inson):
    def __init__(self, ism, yosh, guruh):
        super().__init__(ism, yosh)
        self.guruh = guruh

    def salomlash(self):    # Override
        print(f"Salom, men {self.ism}, {self.guruh} talabasi!")

    def __str__(self):
        return f"Talaba({self.ism}, {self.guruh})"


t = Talaba("Dilnoza", 20, "CS-101")
t.salomlash()
print(t)
print(isinstance(t, Inson))    # True
print(isinstance(t, Talaba))   # True


# --- Ko'p meros ---
class A:
    def salom(self):
        print("A dan salom")

class B(A):
    def salom(self):
        print("B dan salom")

class C(A):
    def salom(self):
        print("C dan salom")

class D(B, C):
    pass

d = D()
d.salom()               # B dan salom (MRO bo'yicha)
print(D.__mro__)        # Method Resolution Order


# --- Abstract Class ---
from abc import ABC, abstractmethod

class Shakl(ABC):
    @abstractmethod
    def yuza(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    def info(self):
        print(f"Yuza: {self.yuza()}, Perimetr: {self.perimetr()}")


class Doira(Shakl):
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return 3.14159 * self.radius ** 2

    def perimetr(self):
        return 2 * 3.14159 * self.radius


class To_rtburchak(Shakl):
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi

    def yuza(self):
        return self.eni * self.boyi

    def perimetr(self):
        return 2 * (self.eni + self.boyi)


doira = Doira(5)
doira.info()
to_rt = To_rtburchak(4, 6)
to_rt.info()


# --- Dataclass ---
from dataclasses import dataclass, field

@dataclass
class Mahsulot:
    nom: str
    narx: float
    miqdor: int = 1
    teglar: list = field(default_factory=list)

    def jami(self):
        return self.narx * self.miqdor


m = Mahsulot("Olma", 5000, 3, ["meva", "shirinlik"])
print(m)
print(m.jami())


# --- Magic Methods ---
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)      # Vector(4, 6)
print(v2 - v1)      # Vector(2, 2)
print(v1 * 3)       # Vector(3, 6)
print(len(v2))      # 5
