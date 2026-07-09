# ============================================================
# 05 - TUPLE VA SET
# ============================================================

# ==================== TUPLE ====================
t = (1, 2, 3, 4, 5)

print(t[0])             # 1
print(t[-1])            # 5
print(t[1:3])           # (2, 3)
print(len(t))           # 5
print(t.count(1))       # 1
print(t.index(3))       # 2
print(3 in t)           # True

# --- Unpack ---
x, y, z = (1, 2, 3)
a, *b = (1, 2, 3, 4, 5)
print(a, b)             # 1 [2, 3, 4, 5]

# --- Named tuple ---
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x)              # 10
print(p.y)              # 20
print(p)                # Point(x=10, y=20)

Person = namedtuple("Person", ["ism", "yosh", "shahar"])
ali = Person("Ali", 25, "Toshkent")
print(ali.ism)

# --- Tuple o'zgarmas ---
# t[0] = 99   # TypeError: tuple does not support item assignment

# ==================== SET ====================
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

# --- Qo'shish / O'chirish ---
s1.add(6)
s1.remove(1)            # yo'q bo'lsa xato
s1.discard(99)          # yo'q bo'lsa xato yo'q
popped = s1.pop()       # tasodifiy

# --- Amallar ---
print(s1 | s2)          # birlashma
print(s1.union(s2))
print(s1 & s2)          # kesishma
print(s1.intersection(s2))
print(s1 - s2)          # ayirma
print(s1.difference(s2))
print(s1 ^ s2)          # simmetrik ayirma
print(s1.symmetric_difference(s2))

# --- Tekshirish ---
s3 = {1, 2}
s4 = {1, 2, 3, 4}
print(s3.issubset(s4))      # True
print(s4.issuperset(s3))    # True
print(s3.isdisjoint({5, 6})) # True

# --- Set Comprehension ---
kvadratlar = {x**2 for x in range(10)}
print(kvadratlar)

# --- frozenset ---
fs = frozenset([1, 2, 3])
# fs.add(4)   # AttributeError
print(fs)

# --- Dublikatlarni olib tashlash ---
lst = [1, 1, 2, 2, 3, 3, 4]
unique = list(set(lst))
print(unique)
