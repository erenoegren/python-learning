#ekrandan alinan bir sayinin faktoriyelini hesaplayan program

#sayi = int(input("Lütfen bir sayi giriniz: "))
#print(type(sayi))
#sayi = int(sayi)

#faktoriyel = 1

#for i in range(1, sayi + 1):
    #faktoriyel *= i

#i = 2
#while i <= sayi:
    #faktoriyel *= i
    #i+= 1
#print(f"{sayi}! = {faktoriyel}")



#Ekrandan alınan bir sayının asal olup olmadığını kontrol eden program

#sayi = int(input("Lütfen bir sayi giriniz: "))

#prime = True 

#for i in range(2, sayi):
    #if sayi % i == 0:
        #prime = False
        #print(f"{sayi} sayısı asal bir sayı değildir.")
        #break
    #elif sayi % i != 0:
        #prime = True
        #print(f"{sayi} sayısı asal bir sayıdır.")
        #break


#Ekrandan alinan bir sayinin pozitif kac tane böleni oldugunu hesaplayan bir program

#sayi = int(input("Bir sayi giriniz: "))

#bolen_sayisi = 0

#for i in range(1, sayi + 1):
    #if sayi % i == 0:
        #bolen_sayisi += 1
#print(f"{sayi} sayisinin {bolen_sayisi} tane böleni vardir.") 


#Ekrandan okunan bir sayinin rakamlari toplamini hesaplayan bir program yaziniz.

#sayi = int(input("Bir sayi giriniz: "))
#str_sayi = str(sayi)
#toplam = 0

#for rakam in str_sayi:
    #toplam += int(rakam)

#print(f"{sayi} sayisinin rakamlari toplami: {toplam}")


#Ekrandan pespese okunan 5 sayinin en kücügünü ve en büyügünü ekrana yazdiran program. 

#liste = []

#for i in range(5):
    #sayi = int(input(f"{i+1}. sayiyi giriniz: "))
    #liste.append(sayi)
    #print(f"Girilen sayilar: {liste}")
    #print(f"En kucuk sayi: {min(liste)}")
    #print(f"En buyuk sayi: {max(liste)}")


#Ekrandan okunan bir metinde hangi harfin kac kere kullanildigini gösteren bir program yaziniz.

#metin = input("Bir metin giriniz: ")
#sozluk = dict()

#for harf in metin:
    #if harf in metin:
        #if harf in sozluk:
            #sozluk[harf] += 1
        #else:
            #sozluk[harf] = 1
#for harf, sayi in sozluk.items():
    #print(harf, sayi)




#Ekrandan okunan bir metinnde a harflerini büyük yapan bir program yaziniz.

metin = input("Bir metin giriniz: ")

metin2 = "" 

for harf in metin: 
    if harf == "a":
        metin2 += "A"
    else:
        metin2 += harf
print(metin2)
