#A)
lista_dezordonata = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista_dezordonata)
#B)
lista_dezordonata.sort()
print(lista_dezordonata)
#C)
lista_dezordonata.sort(reverse=True)
print(lista_dezordonata)
#D)
lista_dezordonata = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista_dezordonata_sliced = lista_dezordonata[1:10:2]
print(lista_dezordonata_sliced)
#E
lista_dezordonata = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista_dezordonata_sliced = lista_dezordonata[0:10:2]
print(lista_dezordonata_sliced)
#F)
lista_dezordonata = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
multiples_3 = [n for n in lista_dezordonata if n % 3 == 0]
print(multiples_3)
