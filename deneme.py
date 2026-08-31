print("Merhaba Dünya!")
print("""Merhaba
Dünya""")
print("Merhaba\nDünya")
print("Merhaba\t\t\tDünya")

mesaj = "Merhaba"
mesaj2 = "Bera"
mesaj = mesaj.upper()
print(mesaj)
mesaj = mesaj.lower()
print(mesaj)

print(mesaj + " " + mesaj2)

print(mesaj[1])

print(mesaj[1:4])

print(mesaj[::])
print(mesaj[::-1])

mesaj = mesaj.capitalize()
print(mesaj)

print(mesaj.startswith("Me"))
print(mesaj.endswith("a"))
print(len(mesaj + mesaj2))

mesaj = "Merhaba"

mesaj2 = "Dünya"

print("Merhaba" + " " + mesaj2)
print("Merhaba" * 10)

isim = "Ali"

yas = "20"

print("{} , {} yasindadir".format(isim,yas))

isim = "Ahmet"

mesaj = "merhaba"

print("{} , {} dedi".format(isim,mesaj))

print(f"{isim}, {mesaj} dedi")