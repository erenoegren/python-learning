 #listeler  

renkler = ["Siyah" , "Beyaz" , "Sari" , "Mavi" , "Yesil"]
print(renkler)
print(len(renkler))
print(renkler[1])
#indeksler 0 dan baslar o yüzden 1 beyazi verir. 

print(renkler[2:])
print(renkler[1:4])
print(renkler[::2])

#Append methodu listenin sonuna eleman eklemeye yarar...

renkler.append("Gri")
print(renkler)

#Insert methodu

renkler.insert(2,"Pembe")
print(renkler)

#Remove methodu

renkler.remove("Sari")
print(renkler)

#Extend methodu

renkler2 = ["Turuncu" , "Lila"]
renkler.append(renkler2)
print(renkler)

renkler.extend(renkler2)
print(renkler)

#Pop methodu

silinen = renkler.pop()
print(renkler)
print(silinen)

#Reverse methodu

renkler.reverse()
print(renkler)


renkler3 = ["Nürdün", "Kahverengi", "Beyaz"]
sayilar = [1,2,39,4,3,7,8]
print(min(renkler3))

print(min(sayilar))

print(sum(sayilar))

#for döngüsü 

for renk in renkler3: 
    print(renk)

#enumarate fonksiyonlar

print(list(enumerate(renkler)))
print(list(enumerate(renkler,start=3)))
print("Siyah" in renkler)

#listeyi stringe cevirmek ve join methodu

stringrenkler = ",".join(renkler3)
print(stringrenkler)

#stringi listeye cevirmek split methodu

print(stringrenkler)

renkler5 = stringrenkler.split(",")
print(renkler5)