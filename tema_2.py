# ex 1:
# lista_numere = (2, -19, 6, 'y', 'q', [55, 'b', 'cad'])
# def sum_of_numbers(*numere):
#     total_sum = 0
#
#     for num in numere:
#         if isinstance(num, (int)):
#             total_sum += num
#     return total_sum
#
# result = sum_of_numbers(*lista_numere)
# print(result)

# ex 2:
# lista_numere = [23, 4, 45, 67, 81, 65, 43, 2, 3, 88, 39, 21]
# def recursive_sum(lista):
#     if not lista:
#         return 0, 0, 0
#
#     numerele_mele = lista[0]
#     total, even_sum, odd_sum = recursive_sum(lista[1:])
#
#     total += numerele_mele
#
#     if numerele_mele % 2 == 0:
#         even_sum += numerele_mele
#     else:
#         odd_sum += numerele_mele
#     return total, even_sum, odd_sum
#
# total_sum, even_sum, odd_sum = recursive_sum(lista_numere)
#
# print("Suma Totala:", total_sum)
# print("Suma Numere Pare:", even_sum)
# print("Suma Numere Impare:", odd_sum)

# ex 3
def nr_intreg_tastatura():
    try:
        nr_meu = input("Scrie orice numar: ")
        nr_meu_returnat= int(nr_meu)
        return nr_meu_returnat

    except ValueError:
        return 'MARE 0 = Culca-te!Honk mimimi ^-^'

result = nr_intreg_tastatura()
print("Rezultat:", result)