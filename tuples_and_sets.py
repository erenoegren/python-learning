#demet = ("Sari" , "Mavi" , "Yesil" , "Kirmizi" , "Siyah")
#print(type(demet))
#print(len(demet))

#for renk in demet:
#    print(demet)



kume = {"Sari" , "Mavi" , "Yesil" , "Kirmizi" , "Siyah"}
for renk in kume:
    print(renk)

print(kume)

kume.add("Pembe")
print(kume)

kume.discard("Gri")
print(kume)

kume2 = {"Sari" , "Mavi" , "Yesil" , "Beyaz" , "Gri"}

print(kume.intersection(kume2))

print(kume.union(kume2))

print(kume2.difference(kume))

print("Sari" in kume.union(kume2))



bosliste1 = []
bosliste2 = list()

bosdemet1 = ()
bosdemet2 = tuple()

boskume1 = set()
boskume2 = {} #Bu bir sözlüktür.
print(type(boskume2))

python = set("PYTHON")
print(python)