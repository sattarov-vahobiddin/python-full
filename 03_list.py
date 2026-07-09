# ============================================================
# 03 - LIST (RO'YXAT)
# ============================================================

lst = [3, 1, 4, 1, 5, 9, 2, 6]

# --- Qo'shish ---
lst.append(7)               # oxiriga
lst.insert(0, 0)            # indeksga
lst.extend([10, 11])        # ro'yxat qo'shish
lst += [12, 13]

# --- O'chirish ---
lst.remove(1)               # birinchi 1 ni
lst.pop()                   # oxirgisini
lst.pop(0)                  # indeks bo'yicha
del lst[0]
lst.clear()                 # hammani

# --- Qayta yaratish ---
lst = [3, 1, 4, 1, 5, 9, 2, 6]

# --- Qidirish ---
print(lst.index(5))         # 4
print(lst.count(1))         # 2
print(5 in lst)             # True

# --- Saralash ---
lst.sort()                              # kichikdan kattaga
lst.sort(reverse=True)                  # kattadan kichikka
lst.sort(key=lambda x: -x)             # maxsus kalit
print(sorted(lst))                      # yangi ro'yxat
lst.reverse()                           # teskari

# --- Ma'lumot ---
print(len(lst))     # uzunlik
print(min(lst))     # eng kichik
print(max(lst))     # eng katta
print(sum(lst))     # yig'indisi

# --- Nusxa ---
import copy
nusxa1 = lst.copy()
nusxa2 = lst[:]
nusxa3 = copy.deepcopy(lst)    # chuqur nusxa

# --- List Comprehension ---
kvadratlar = [x**2 for x in range(10)]
juft = [x for x in range(20) if x % 2 == 0]
matrix = [[i*j for j in range(3)] for i in range(3)]
print(kvadratlar)
print(juft)

# --- Zip, Enumerate, Map, Filter ---
print(list(zip([1, 2, 3], ["a", "b", "c"])))
print(list(enumerate(["a", "b", "c"])))
print(list(map(lambda x: x*2, [1, 2, 3])))
print(list(filter(lambda x: x > 2, [1, 2, 3, 4])))

# --- Unpack ---
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4, 5]
*init, last = [1, 2, 3, 4, 5]
print(first, rest)
print(init, last)
