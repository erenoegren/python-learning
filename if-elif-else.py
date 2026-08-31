#if True:
    #print("Kosul dogru")
    #print("Hala if blogunun icindeyiz")

#if False:
    #print("Kosul dogru")
    #print("Hala if blogunun icindeyiz")

a = 5
b = 7

#if a == b:
    #print("a ve b esit")
#else:
    #print("a ve b esit degil")

#if a > b:
    #print("a b den buyuk")
#elif a < b:
    #print("a b den kucuk")

#renk = "Siyah"
#if renk == "Beyaz":
    #print("Renk beyaz")
#elif renk == "Sari":
    #print("Renk sari")
#elif renk == "Kirmizi":
    #print("Renk kirmizi")
#else:
    #print("Bunlardan hicbiri degil")

a = 5
b = 8
c = 10

if a > b or c == a:
    print("Kosul dogru")
else:
    print("Kosul yanlis")

if a < b and c == a:
    print("Kosul dogru")
else: 
    print("Kosul yanlis")

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 4
if a in liste:
    print("Listede var")
else:
    print("Listede yok")

if not a == b:
    print("Kosul dogru")
else:
    print("Kosul yanlis")

d = "python"
e = "pytho"
f = "n"

if d is e:
    print("d = e")
else:
    print("d != e")
if d is not e:
    print("d != e")
