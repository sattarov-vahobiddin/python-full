# ============================================================
# 04 - DICTIONARY (LUG'AT)
# ============================================================

d = {"ism": "Ali", "yosh": 25, "shahar": "Toshkent"}

# --- O'qish ---
print(d["ism"])                         # "Ali"
print(d.get("ism"))                     # "Ali"
print(d.get("telefon", "yo'q"))         # "yo'q"
print(d.keys())
print(d.values())
print(d.items())

# --- Qo'shish / Yangilash ---
d["email"] = "ali@mail.com"
d.update({"yosh": 26, "kasb": "dasturchi"})
d.setdefault("telefon", "noma'lum")     # yo'q bo'lsa qo'shadi

# --- O'chirish ---
del d["shahar"]
popped = d.pop("yosh")                  # o'chirib qaytaradi
d.pop("yo'q", None)                     # topilmasa None

# --- Tekshirish ---
print("ism" in d)       # True
print(len(d))

# --- Dict Comprehension ---
result = {k: v*2 for k, v in {"a": 1, "b": 2}.items()}
print(result)

# --- Birlashtirish ---
d1 = {"a": 1}
d2 = {"b": 2}
d3 = {**d1, **d2}       # {"a": 1, "b": 2}
d4 = d1 | d2            # Python 3.9+
print(d3)

# --- Saralash ---
data = {"b": 3, "a": 1, "c": 2}
sorted_by_key = dict(sorted(data.items()))
sorted_by_val = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_by_key)
print(sorted_by_val)

# --- defaultdict ---
from collections import defaultdict

dd = defaultdict(int)
dd["kalit"] += 1
dd["boshqa"] += 5
print(dict(dd))

dd_list = defaultdict(list)
dd_list["fruits"].append("olma")
dd_list["fruits"].append("banan")

# --- Counter ---
from collections import Counter

c = Counter("abracadabra")
print(c.most_common(3))     # [('a', 5), ('b', 2), ('r', 2)]
print(c["a"])               # 5

words = ["olma", "banan", "olma", "uzum", "banan", "olma"]
wc = Counter(words)
print(wc.most_common())
