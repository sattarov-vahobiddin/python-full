# ============================================================
# 07 - SIKLLAR (LOOPS)
# ============================================================

# --- For loop ---
for i in range(5):
    print(i)                # 0, 1, 2, 3, 4

for i in range(1, 10):
    print(i)                # 1 dan 9 gacha

for i in range(0, 10, 2):
    print(i)                # 0, 2, 4, 6, 8

for i in range(10, 0, -1):
    print(i)                # 10 dan 1 gacha

# --- Ro'yxat bo'ylab ---
mevalar = ["olma", "banan", "uzum"]
for meva in mevalar:
    print(meva)

# --- Dict bo'ylab ---
d = {"a": 1, "b": 2, "c": 3}
for kalit in d:
    print(kalit)
for qiymat in d.values():
    print(qiymat)
for kalit, qiymat in d.items():
    print(f"{kalit}: {qiymat}")

# --- Enumerate ---
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)           # 0 a, 1 b, 2 c

for i, val in enumerate(["a", "b", "c"], start=1):
    print(i, val)           # 1 a, 2 b, 3 c

# --- Zip ---
ismlar = ["Ali", "Vali", "Soli"]
yoshlar = [25, 30, 22]
for ism, yosh in zip(ismlar, yoshlar):
    print(f"{ism}: {yosh}")

# --- While loop ---
i = 0
while i < 5:
    print(i)
    i += 1

# --- While True ---
# while True:
#     javob = input("Chiqish (q): ")
#     if javob == "q":
#         break

# --- break ---
for i in range(10):
    if i == 5:
        break
    print(i)                # 0, 1, 2, 3, 4

# --- continue ---
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)                # 1, 3, 5, 7, 9

# --- pass ---
for i in range(5):
    pass                    # hech narsa

# --- else in loop ---
for i in range(5):
    print(i)
else:
    print("Sikl tugadi")    # break bo'lmasa ishlaydi

# --- Nested loop ---
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()

# --- Ko'paytirish jadvali ---
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:3}", end=" ")
    print()

# --- List comprehension bilan ekvivalent ---
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
