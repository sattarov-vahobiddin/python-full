# ============================================================
# 02 - STRING (MATN) METODLARI
# ============================================================

s = "Salom Dunyo"

# --- Asosiy metodlar ---
print(len(s))                       # 10
print(s.upper())                    # "SALOM DUNYO"
print(s.lower())                    # "salom dunyo"
print(s.title())                    # "Salom Dunyo"
print(s.capitalize())               # "Salom dunyo"
print(s.strip())                    # bo'shliqlarni olib tashlash
print(s.lstrip())                   # chapdan
print(s.rstrip())                   # o'ngdan
print(s.replace("Salom", "Hi"))     # "Hi Dunyo"
print(s.split(" "))                 # ["Salom", "Dunyo"]
print(" ".join(["a", "b", "c"]))    # "a b c"
print(s.find("Dunyo"))              # 6
print(s.index("Dunyo"))             # 6
print(s.count("l"))                 # 1
print(s.startswith("Sal"))          # True
print(s.endswith("nyo"))            # True
print(s.isdigit())                  # False
print(s.isalpha())                  # False
print(s.isalnum())                  # False
print(s.isspace())                  # False
print(s.isupper())                  # False
print(s.islower())                  # False
print(s.swapcase())                 # "sALOM dUNYO"
print(s.zfill(15))                  # "00000Salom Dunyo"
print(s.center(20, "*"))            # "****Salom Dunyo****"
print(s.ljust(20, "-"))             # "Salom Dunyo---------"
print(s.rjust(20, "-"))             # "---------Salom Dunyo"

# --- Kesish (Slicing) ---
print(s[0])         # "S"
print(s[-1])        # "o"
print(s[0:5])       # "Salom"
print(s[6:])        # "Dunyo"
print(s[:5])        # "Salom"
print(s[::2])       # har ikkinchi harf
print(s[::-1])      # "oynoD molaS"

# --- Formatlash ---
ism = "Ali"
yosh = 25
print(f"Ismim {ism}, yoshim {yosh}")        # f-string
print("Ismim {}, yoshim {}".format(ism, yosh))
print("Ismim %s, yoshim %d" % (ism, yosh))
print(f"{3.14159:.2f}")                     # "3.14"
print(f"{1000000:,}")                       # "1,000,000"
print(f"{0.75:.0%}")                        # "75%"
print(f"{'ali':>10}")                       # "       ali"
print(f"{'ali':<10}")                       # "ali       "
print(f"{'ali':^10}")                       # "   ali    "

# --- Maxsus belgilar ---
print("Salom\nDunyo")   # yangi qator
print("Salom\tDunyo")   # tab
print("U dedi: \"Salom\"")

# --- Encode / Decode ---
encoded = "Salom".encode("utf-8")   # bytes
decoded = encoded.decode("utf-8")   # string
print(decoded)
