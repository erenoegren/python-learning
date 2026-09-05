#Fibonacci sayi dizisi ilk iki terimi 1 olan ve sonraki her terimi kendisinden önceki iki terimin toplamı olan bir sayı dizisidir.
# Ilk 100 Fibonacci sayisini ekrana yazdiran programi yaziniz.

fibonacci_list = []
fibonacci_list.append(1)
fibonacci_list.append(1)

index = 2
while True:
    fibonacci_list.append(fibonacci_list[index - 1] + fibonacci_list[index - 2])
    index += 1
    if len(fibonacci_list) == 100:
        break
    
print(fibonacci_list)
