# 1. Išveskite visus skaičius nuo 1 iki 20.
import random

# num = 0
# while num<=20:
#     print (num)
#     num += 1

# 2. Išveskite visus skaičius nuo 1 iki 50. Prie kiekvieno lyginio skaičiaus
# parašykite žodį "lyginis", o prie kiekvieno nelyginio – "nelyginis".

# num = 1
# while num <=50:
#     if num % 2 == 0:
#         print (num, 'lyginis')
#     else:
#         print (num, 'nelyginis')
#     num += 1

# 3. Išveskite visus skaičius nuo 25 iki 50. Vietoj skaičių, kurie dalinasi iš 3
# išveskite tekstą "dalinasi iš 3".

# num = 25
#
# while num <50:
#     if num % 3 == 0:
#         print ('dalinasi is 3')
#     else:
#         print (num)
#     num +=1

# 4. Išveskite visus skaičius nuo 1 iki 100 arba iki tol kol pasitaikys toks, kuris
# dalinasi iš 7.

# num = 0
# while num < 100:
#     num += 1
#     print(num)
#     if num % 7 == 0:
#         break

# 5. Išvedinėkite visus skaičius nuo 1 iki tol kol pasitaikys skaičius, kuris
# dalinasi iš 3 ir iš 5.

# num = 0
# while True:
#     num +=1
#     print (num)
#     if num % 3 == 0 and num % 5 == 0:
#         break

# 6. Vartotojas turi suvesti rėžių pradžią ir pabaigą. Tačiau jūs turite patikrinti
# ar nurodyti rėžiai yra geri (pradžia mažesnė už pabaigą). Liepkite
# vartotojui kartoti įvedimą tol, kol rėžiai jau bus įvesti tinkamai. Turint
# tinkamus rėžius, išveskite visus skaičius nuo rėžių pradžios iki pabaigos
# (šitam jau vietoj while galite naudoti for ciklą), šalia kiekvieno skaičiaus
# išvedant jo kvadratą, bei ar jis lyginis/nelyginis.

# while True:
#     pradzia = int(input("Iveskite rezio prdzia: "))
#     pabaiga = int(input("Iveskite rezio pabaiga: "))
#     if pradzia < pabaiga:
#         break
#     else:
#         print ('Bandykite dar karta...')
#
# for i in range (pradzia, pabaiga +1):
#     kvadratas = i ** 2
#     lyginis = "lyginis" if i % 2 == 0 else "nelyginis"
#
#     print(f"Skaičius: {i}, Kvadratas: {kvadratas}, {lyginis}")

# 7. Išveskite visus skaičius nuo 1 iki kol pasitaikys toks, kuris yra pirminis ir
# yra didesnis nei 20.
#
# import math
#
# def pirminis(skaicius):
#     sqrt_skaicius = math.sqrt(skaicius)
#     if skaicius < 2:
#         return False
#     for i in range(2, int(sqrt_skaicius) + 1):
#         if skaicius % i == 0:
#             return False
#     return True
#
# skaicius = 1
#
# while True:
#     print(skaicius)
#     if pirminis(skaicius) and skaicius > 20:
#         break
#     skaicius += 1

# 8. Liepkite vartotojui įvedinėti bet kokius skaičius. Vykdykite įvedinėjimą iki
# kol įvestas skaičius bus lygus 0. Raskite įvestų skaičių sumą.

import random

# skaiciu_suma = 0
# skaicius = 0
#
# while skaicius != 0:
#     # skaicius =  int(input(random.randint(0, 100)))
#     skaicius = int(input("Ivesti skaiciu: "))
# if skaicius != 0:
#     skaiciu_suma += skaicius
#
# print (f'Suma: {skaiciu_suma}') #NEVEIKIA

# skaiciu_suma = 0
#
# while True:
#     skaicius = int(input("Ivesti skaiciu: "))
#     if skaicius == 0:
#         break
#
#     skaiciu_suma += skaicius
#
# print(f'Suma: {skaiciu_suma}')

# 9. Leiskite vartotojui atlikti norimus skaičiavimus tiek kartų kiek jis nori.
# Pavyzdžiui, leiskite vartotojui įvesti du skaičius, tuomet jam parodykite
# pačius skaičius, veiksmus (sudėtis, atimtis, daugyba, dalyba) ir
# suskaičiuotus atsakymus (5 + 3 = 8; 5 - 3 = 2; ...). Kai atsakymai bus
# parodyti, vartotojas turi turėti galimybę pakartoti skaičiavimus, todėl
# leiskite pasirinkti ar dar kartoti veiksmą, ar jau programa turėtų baigti
# savo darbą.

# 10.Vartotojui išveskite pasirinkto skaičiaus daugybos lentelę (pvz, skaičiaus 5
# daugybos lentelė būtų 5 * 1 = 5; 5 * 2 = 10; 5 * 3 = 15; ...). Leiskite
# vartotojui kartoti veiksmą (tiek kartų kiek norės) ir gauti dar vieną
# daugybos lentelę su kitu pasirinktu skaičiumi.

# 11.Liepkite vartotojui įvesti kiek jis nori skaičių. Įvedimą sustabdykite tuomet,
# kai vartototojas įves 0 ar -1, ar kitą jūsų pasirinktą skaičių ar simbolį.
# Raskite vartotojo įvestų skaičių sumą, vidurkį.


# 12.Sukurkite studentų pažymių vidurkių skaičiuoklę (kaip pavyzdį galite
# naudoti 17-ą pavyzdį). Tačiau tokia skaičiuoklė turėtų leisti skaičiuoti
# vidurkį ne tik iš vieno studento pažymių, bet leistų pakartoti pažymių
# įvedimą ir vidurkio skaičiavimą ant tiek studentų kiek reikia.

# 13.Sukurkite skaičiaus atspėjimo užduotį. Leiskite vartotojui pasirinkti
# žaidimo sudėtingumą (atsitiktinio skaičiaus rėžiai), ar suteikiamos
# pagalbos (skaičius mažesnis/didesnis nei spėjamas), kiek spėjimų
# leidžiama (neribotai, arba pvz iki 10 ėjimų), bei kiti pasirinkti parametrai.
# Vartotojas šiuos parametrus pasirenka žaidimo pradžioje. Turite užtikrinti,
# kad vartotojas pasirinko parametrus tik iš galimų - jeigu ne, liepkite
# įvedimą pakartoti.
