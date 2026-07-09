# ============================================================
# 06 - SHARTLAR
# ============================================================

x = 10

# --- If / elif / else ---
if x > 0:
    print("Musbat")
elif x < 0:
    print("Manfiy")
else:
    print("Nol")

# --- Ternary ---
natija = "katta" if x > 5 else "kichik"
print(natija)

# --- Ichma-ich ternary ---
baho = 85
daraja = "A" if baho >= 90 else "B" if baho >= 80 else "C" if baho >= 70 else "D"
print(daraja)

# --- Mantiqiy operatorlar ---
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# --- Taqqoslash ---
a = 5
print(a == 5)           # True
print(a != 5)           # False
print(a > 3)            # True
print(a < 3)            # False
print(a >= 5)           # True
print(a <= 5)           # True
print(a is None)        # False
print(a is not None)    # True

# --- Zanjirli taqqoslash ---
print(1 < x < 20)       # True
print(0 <= a <= 10)     # True

# --- in operatori ---
mevalar = ["olma", "banan", "uzum"]
print("olma" in mevalar)        # True
print("nok" not in mevalar)     # True
print("a" in "salom")           # True

# --- Match-case (Python 3.10+) ---
rang = "qizil"
match rang:
    case "qizil":
        print("Stop")
    case "yashil":
        print("Yuring")
    case "sariq":
        print("Ehtiyot")
    case _:
        print("Noma'lum rang")

# --- Match bilan guard ---
son = 42
match son:
    case n if n < 0:
        print("Manfiy")
    case n if n == 0:
        print("Nol")
    case n if n > 0:
        print("Musbat")

# --- Qisqa yozuvlar ---
lst = []
if lst:                 # bo'sh ro'yxat = False
    print("Bor")
else:
    print("Bo'sh")

val = None
result = val or "default"   # None bo'lsa default
print(result)
