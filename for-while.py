liste = [1,2,3,4,5,6]
print(liste[0])
#Bu klasiktir cok zaman harcar 

isim = "Ahmet"
for harf in isim:
    print(harf)

demet = (1,2,3,4,5,6)
for eleman in demet:
    print(eleman)

#Mesela ben bir islemi 20 kere tekrar etmek istiyorsam range fonk. 
#ilk paramtere baslangic, ikinci paramtetre bitis, ucuncu parametre adim 
for i in range(1,17,2):
    print(i)

sonuc = 1
for i in range(0,10):
    sonuc *= 2
print(sonuc)

liste1 = ["a", "b", "c"]
liste2 = [1, 2, 3]

for harf in liste1:
    for rakam in liste2:
        print(harf, rakam)


#break and continue

liste3 = [1,2,3,4,5,6,7,8,9]
for i in liste3:
    if i == 3:
        print("3 bulundu!")
        continue
    if i == 6:
        print("6 sayisini atladik!")
        break
    print(i)

liste4 = range(100)

for i in liste4:
    if i % 3 != 0:
        continue
    if i == 81:
        break  
    print(i)

#while
x = 2

#while x < 10:
    #print(x)
    #x += 1   
    #print("x = ", x)

a = 2
b = 3

while a * b < 1000:
    print(a,b)
    a += 2
    b += 2


z = 1
#while True:
    #print(z)
    #z += 1
    #if z == 10000:
        #break

while True:
    if z % 2 == 0:
        z += 1
        continue
    print(z)
    z += 1
    if z == 10000:
        break
    print("z = ", z)