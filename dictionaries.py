kisi = {"isim": "Ahmet", "yas": 30, "sehir": "İstanbul", "hobiler": ["futbol", "kitap okuma", "yüzme"]}

#print(kisi["isim"])  

print(kisi)

#kisi["isim"] = "Mustafa"  # Değeri güncelleme

kisi.update({"isim" : "Mustafa" , "yas" : 35})  # Değeri güncelleme
print(kisi)

kisi["id"] = 12345  # Yeni bir anahtar-değer çifti ekleme
print(kisi)
del kisi["id"]
print(kisi)

for x in kisi:
    print(x)  

for x in kisi:
    print(kisi[x])

print(kisi.keys())
print(kisi.values())

for k, v in kisi.items():
    print(k, v)
