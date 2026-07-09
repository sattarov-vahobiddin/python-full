# ============================================================
# 08 - FUNKSIYALAR
# ============================================================

# --- Oddiy funksiya ---
def salomlash():
    print("Salom!")

salomlash()

# --- Parametrli ---
def qoshish(a, b):
    return a + b

print(qoshish(3, 5))        # 8

# --- Default parametr ---
def salom(ism="Foydalanuvchi"):
    print(f"Salom, {ism}!")

salom()                     # Salom, Foydalanuvchi!
salom("Ali")                # Salom, Ali!

# --- *args ---
def yigindi(*sonlar):
    return sum(sonlar)

print(yigindi(1, 2, 3, 4, 5))  # 15

# --- **kwargs ---
def ma_lumot(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

ma_lumot(ism="Ali", yosh=25, shahar="Toshkent")

# --- *args va **kwargs birga ---
def funksiya(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

funksiya(1, 2, 3, ism="Ali", yosh=25)

# --- Type hints ---
def qoshish2(a: int, b: int) -> int:
    return a + b

# --- Lambda ---
kvadrat = lambda x: x**2
print(kvadrat(5))           # 25

qo_shish = lambda a, b: a + b
print(qo_shish(3, 4))       # 7

# Saralash uchun lambda
odamlar = [{"ism": "Vali", "yosh": 30}, {"ism": "Ali", "yosh": 25}]
odamlar.sort(key=lambda x: x["yosh"])
print(odamlar)

# --- Closure ---
def hisoblagich():
    n = 0
    def increment():
        nonlocal n
        n += 1
        return n
    return increment

sanoq = hisoblagich()
print(sanoq())      # 1
print(sanoq())      # 2
print(sanoq())      # 3

# --- Decorator ---
def dekorator(func):
    def wrapper(*args, **kwargs):
        print("--- Oldin ---")
        natija = func(*args, **kwargs)
        print("--- Keyin ---")
        return natija
    return wrapper

@dekorator
def mening_funksiyam():
    print("Bu mening funksiyam!")

mening_funksiyam()

# --- Vaqt o'lchash decorator ---
import time

def vaqt_olchash(func):
    def wrapper(*args, **kwargs):
        boshlash = time.time()
        natija = func(*args, **kwargs)
        tugash = time.time()
        print(f"{func.__name__}: {tugash - boshlash:.4f} soniya")
        return natija
    return wrapper

@vaqt_olchash
def sekin_funksiya():
    time.sleep(0.1)

sekin_funksiya()

# --- Recursion ---
def faktorial(n):
    if n <= 1:
        return 1
    return n * faktorial(n - 1)

print(faktorial(5))     # 120

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))    # 55

# --- Generator ---
def sonlar_gen(n):
    for i in range(n):
        yield i

gen = sonlar_gen(5)
print(next(gen))        # 0
print(next(gen))        # 1
print(list(gen))        # [2, 3, 4]

# Generator expression
gen2 = (x**2 for x in range(10))
print(list(gen2))

# --- functools ---
import functools

@functools.lru_cache(maxsize=128)
def fib_kesh(n):
    if n < 2:
        return n
    return fib_kesh(n-1) + fib_kesh(n-2)

print(fib_kesh(40))     # tez ishlaydi

# --- partial ---
def ko_paytir(x, y):
    return x * y

ikki_baravar = functools.partial(ko_paytir, 2)
print(ikki_baravar(5))  # 10
