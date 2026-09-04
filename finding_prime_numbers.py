#Ilk 10000 asal sayinin kac tanesi 3 ile baslar ve 7 ile biter. 

prime_list = list()

prime_list.append(2)

sayi = 3 

while True: 
    prime = True
    for i in range(2, sayi):
        if sayi % i == 0:
            prime = False
            break
    if prime: 
        prime_list.append(sayi)
        if len(prime_list) == 1000:
            break
    sayi += 1
    list2 = []


for prime in prime_list:
    strprime = str(prime)
    if strprime.startswith('3') and strprime.endswith('7'):
        list2.append(prime)
        
print(list2)
print(len(list2))


