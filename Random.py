# 1. Sukurkite 4 kintamuosius, kurie saugotų jūsų vardą, pavardę, gimimo metus ir šiuos metus
# (nebūtinai tikrus). Parašykite kodą, kuris pagal gimimo metus paskaičiuotų jūsų amžių ir
# naudodamas vardo ir pavardės kintamuosius atspausdintų tokį sakinį :
# "Aš esu Vardenis Pavardenis. Man yra XX metai(ų)".
#
# w1 = str(input("Iveskite varda: "))
# w2 = str(input("Iveskite pavarde: "))
# w3 = int(input("Gimimo metai: "))
# from datetime import datetime
#
# print(f'As esu {w1} {w2}. Man yra {datetime.now().year-w3} metai(u).')
import random
from itertools import count

# 2. Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite
# atsitiktines reikšmes nuo 0 iki 4. Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite
# rezultatą jį suapvalinę iki 2 skaičių po kablelio.
#
# import random
# n1 = random.randint(0,4)
# n2 = random.randint(0,4)
#
# print(n1)
# print(n2)
#
# if n1 !=0 and n2 !=0:
#     if n1>n2:
#         print(round(n1/n2,2))
#     else:
#         print(round(n2/n1,2))
# else:
#     print('dalyba is 0 negalima')
#
# 3. Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius ir naudodamiesi
# funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 25.
# Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.

# n1 = random.randint(0,25)
# n2 = random.randint(0,25)
# n3 = random.randint(0,25)
#
# print(n1)
# print(n2)
# print(n3)
#
# numbers = [n1, n2, n3]
# vidurine_r = sorted(numbers)[1]
# print(vidurine_r)

# 4. Įvedami skaičiai - a, b, c –kraštinių ilgiai, trys kintamieji (naudokite random.randint(x,x)
#  funkciją nuo 1 iki 10). Parašykite Python programą, kuri nustatytų, ar galima sudaryti trikampį
# ir atsakymą atspausdintų.

a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)

print(a)
print(b)
print(c)

if c**2 == a**2 + b**2:
   print('galima sudaryti trikampi')
else:
   print('neimanoma')

# 5. Sukurkite keturis kintamuosius ir random.randint(x,x) funkcija sugeneruokite jiems reikšmes nuo 0 iki 2.
# Suskaičiuokite kiek yra nulių, vienetų ir dvejetų. (sprendimui masyvo nenaudoti).

a = random.randint(0,2)
b = random.randint(0,2)
c = random.randint(0,2)
d = random.randint(0,2)

print(a)
print(b)
print(c)
print(d)

count0 = 0
count1 = 1
count2 = 2

#
# 6. Naudokite funkcija random.randint(x,x). Sukurkite ir atspausdinkite 3 skaičius nuo -10 iki 10.
# Skaičiai mažesni už 0 turi būti  laužtiniuose skliaustuose [], 0 -  (), didesni už 0 {}.   [-4],  (0)
#
# 7. Įmonė parduoda žvakes po 1 EUR. Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida, daugiau
# kaip 2000 vienetų- 4 % nuolaida. Parašykite programą, kuri skaičiuos žvakių kainą ir atspausdintų
# atsakymą kiek žvakių ir kokia kaina perkama. Žvakių kiekį generuokite ​random.randint(x,x) funkcija
# nuo 5 iki 3000.

# 8. Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius su atsitiktinėm reikšmėm
# nuo 0 iki 100. Paskaičiuokite jų aritmetinį vidurkį. Ir aritmetinį vidurkį atmetus tas reikšmes,
# kurios yra mažesnės nei 10 arba didesnės nei 90. Abu vidurkius atspausdinkite. Rezultatus apvalinkite
# iki sveiko skaičiaus.
