from random import *

# #zad1
#
# A = [1-x for x in range(1,11)]
# print(A)
#
# B = [4**x for x in range(0,8)]
# print(B)
#
# C = [x for x in B if x % 2 == 0]
# print(C)



# #zad2
#
# lista1 = []
# for a in range(10):
#     lista1.append(randint(0,10))
# print(lista1)
# lista2 = [x for x in lista1 if x % 2 == 0]
# print(lista2)



# #zad3
#
# produkty = {'Jablka': 'kg','Ziemniaki': 'kg', 'Jajka': 'sztuki', 'Chleb': 'sztuki'}
# sztuki = [produkty.keys() for x in produkty if produkty.values() == 'sztuki']
# print(sztuki)



# #zad4
#
# def czy_prostokatny(a, b, c):
#     if(a**2 + b**2 == c**2):
#         return 1
#     elif(a**2 + c**2 == b**2):
#         return 1
#     elif(b**2 + c**2 == a**2):
#         return 1
#     else:
#         return 0
#
# print(czy_prostokatny(3, 4, 5))
# print(czy_prostokatny(4, 3, 5))
# print(czy_prostokatny(5, 4, 3))
# print(czy_prostokatny(1, 2, 1))



# #zad5
#
# def pole_trapezu(a=1, b=2, h=3):
#     pole = (a+b)*h/2
#     return pole
#
# print(pole_trapezu())



# #zad6
#
# def iloczyn_ciagu(a=1, b=4, ile=10):
#     iloczyn = 1
#     for x in range(ile):
#         iloczyn = iloczyn*a
#         a = a*b
#     return iloczyn
#
# print(iloczyn_ciagu(1,2,3))



# #zad7
#
# def iloczyn_ciagu(*liczba):
#     iloczyn = 1
#     a = int(liczba[0])
#     b = int(liczba[1])
#     ile = int(liczba[2])
#     for x in range(ile):
#         iloczyn = iloczyn*a
#         a = a*b
#     return iloczyn
#
# print(iloczyn_ciagu(1,2,3))




# #zad8
#
# def zakupy(**produkt):
#     ilosc = 0
#     cena = 0
#     for x in produkt:
#         ilosc += 1
#     for x in produkt:
#         cena += int(produkt[x])
#     return ilosc, cena
#
# print(zakupy(jablka = '5', cola = '3'))


#zad9

from ciagi import *

print(arytmetyczne.suma_aryt(1, 2, 2))
print(arytmetyczne.wyraz_aryt(1, 2, 2))
print(geometryczne.suma_geo(1, 2, 2))
print(geometryczne.wyraz_geo(1, 2, 2))
