# ============================================================
# 01 - O'ZGARUVCHILAR VA MA'LUMOT TURLARI
# ============================================================

# --- Asosiy turlar ---
x = 10              # int
y = 3.14            # float
ism = "Ali"         # str
aktiv = True        # bool
nothing = None      # NoneType

# --- Tur aniqlash ---
print(type(x))              # <class 'int'>
print(isinstance(x, int))   # True
print(isinstance(y, float)) # True

# --- Tur o'zgartirish ---
print(int("42"))            # 42
print(float("3.14"))        # 3.14
print(str(100))             # "100"
print(bool(0))              # False
print(bool(1))              # True
print(bool(""))             # False
print(bool("salom"))        # True
print(list("abc"))          # ['a', 'b', 'c']
print(tuple([1, 2, 3]))     # (1, 2, 3)
print(set([1, 1, 2, 3]))    # {1, 2, 3}
print(dict(a=1, b=2))       # {'a': 1, 'b': 2}

# --- Ko'p qiymat ---
a, b, c = 1, 2, 3
x = y = z = 0               # hammasi 0

# --- Global va lokal ---
global_var = "global"

def funksiya():
    lokal_var = "lokal"
    print(global_var)       # global o'zgaruvchiga kirish mumkin

# --- Konstantalar (konventsiya) ---
PI = 3.14159
MAX_SIZE = 100
