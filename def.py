# 1. Sukurkite funkciją, kuri išvestų jūsų vardą ir kodėl pasirinkote
# programavimą. Iškvieskite šią funkciją tris kartus.
import random


# def name(x):
#     print (f'Mano vardas: {x}')
#
# def why(y):
#     print (f'Programavima pasirinkau, nes {y}')
#
# vardas = "Kristina"
# priezastis = "smagu"
#
# name (vardas)
# why (priezastis)
# name (vardas)
# why (priezastis)
# name (vardas)
# why (priezastis)


# 2. Sukurkite funkciją, kuri išvestų 5 eilučių eilėraštį. Iškvieskite šią funkciją 5
# kartus.

# def eilerastis():
#     print('mano')
#     print('namas')
#     print('vijokliais')
#     print('yra')
#     print('apauges')
#     print()
#
# eilerastis()
# eilerastis()
# eilerastis()
# eilerastis()
# eilerastis()

# 3. Sukurkite tris funkcijas, kur kiekviena išvestų skirtingus tekstus. Iškvieskite
# visas tris funkcijas po vieną kartą.

# def pirma():
#     print('pirma funkcija')
#
# def antra():
#     print('antra funkcija')
#
# def trecia():
#     print('trecia funkcija')
#
# pirma()
# antra()
# trecia()

# 4. Sukurkite dvi funkcijas, kur vienoje būtų viena teksto eilutėje, kitoje kita.
# Sukurkite trečią funkciją, kuri iškviestų pirmas dvi funkcijas. Iškvieskite šią
# trečiąją funkciją už visų funkcijų ribų.

# def pirma():
#     print('pirma funkcija')
#
# def antra():
#     print('antra funkcija')
#
# def trecia():
#     pirma ()
#     antra ()
#
# trecia()

# 5. Sukurkite funkciją, kurios viduje sugeneruotumėte du atsitiktinius
# skaičius. Funkcijoje suskaičiuokite ir išveskite šių dviejų skaičių sumą,
# kartu išvedant ir patį atliekamą veiksmą (pvz 7 + 2 = 9). Iškvieskite šią
# funkciją keletą kartų.

# import random
#
# def sumine():
#     sk1 = random.randint(1, 100)
#     sk2 = random.randint(1, 100)
#     suma = sk1 + sk2
#     print(f"{sk1} + {sk2} = {suma}")
#
#
# sumine()
# sumine()
# sumine()

# 6. Sukurkite ir iškvieskite funkciją, kurioje kintamuosiuose būtų saugoma
# informacija apie policininką (vardas, pavardė, amžius, alga, etatas,
# specializacija). Išveskite šią informaciją suformatuotai (pavyzdžiui įterpkite
# į sakinį, ar išveskite sąrašu ar pan.).

# def policininko_informacija():
#     vardas = "Jonas"
#     pavarde = "Petrauskas"
#     amzius = 35
#     alga = 1500
#     etatas = 1.5
#     specializacija = "patrulis"
#     print(f"Policininko informacija:\n"
#           f"Vardas: {vardas}\n"
#           f"Pavardė: {pavarde}\n"
#           f"Amžius: {amzius} metai\n"
#           f"Alga: {alga} eurų\n"
#           f"Etatas: {etatas} etato\n"
#           f"Specializacija: {specializacija}")
#
# policininko_informacija()

# 7. Sukurkite funkciją, kuri išvestų 10 atsitiktinių skaičių. Po visų išvestų
# skaičių turėtų padėti tuščią eilutę. Šią funkciją iškvieskite 5 kartus.

# import random
#
#
# def atsitiktiniai_skaiciai():
#     # for i in range (10):
#     #     sk = random.randint(1, 100)
#     #     print (sk)
#     # print ()
#
#     at_sk = []
#     for i in range (10):
#         sk = random.randint(1, 100)
#         at_sk.append(sk)
#     print(at_sk)
#
# atsitiktiniai_skaiciai ()
# atsitiktiniai_skaiciai ()
# atsitiktiniai_skaiciai ()
# atsitiktiniai_skaiciai ()
# atsitiktiniai_skaiciai ()

# 8. Sukurkite funkciją, kuri išvestų atsitiktinį skaičių. Už funkcijos ribų
# sukurkite ciklą, kurį būtų vykdomas 10 kartų. Iškvieskite sukurtą funkciją
# cikle. Turėtumėte pamatyti 10 atsitiktinių skaičių.
#
# import random
#
# def atsitiktinis_skaicius ():
#     sk = random.randint (1, 8)
#     # for i in range(10):
#     #     print(i)
#     # print (sk)
#     return sk
#
# for i in range (10):
#     print(atsitiktinis_skaicius())
#
# ats_sk = []
# for i in range (10):
#     skaicius = atsitiktinis_skaicius()
#     ats_sk.append(skaicius)
# print (ats_sk)

# 9. Sukurkite funkciją pasisveikinimui, šiai funkcijai per argumentus
# perduokite vardą, funkcijoje išveskite tekstą labas ir gautą vardą.
# Sukurkite kitą funkciją, kuri irgi per argumentus gautų vardą, tačiau
# pasakytų 'viso gero' ir patį vardą. Ne funkcijose susikurkite kintamąjį
# vardui saugoti ir įrašykite vardą. Iškvieskite abi funkcijas, perduodant
# kintamąjį joms.

# def pasisveik(vardas):
#     print('labas,', vardas)
#
# def atsisveik(vardas):
#     print ('viso gero, ', vardas)
#
# vard = 'Kriste'
# pasisveik(vard)
# atsisveik(vard)

# 10.Sukurkite funkciją, kuriai perduotumėte du skaičius. Ši funkcija turi rasti
# kuris skaičius yra didesnis ir išvesti gautą atsakymą, o jei skaičiai lygūs -
# tuomet išvesti, kad skaičiai lygūs. Iškvieskite šią funkciją keletą kartų,
# duodant skirtingus skaičius.

# def skaiciai(a, b):
#     if a > b:
#         print (f'Skaicius {a} yra didesnis uz {b}')
#     elif a == b:
#         print (f'Skaiciai yra lygus')
#     else:
#         print(f'Skaicius {b} yra didesnis uz {a}')
#
# skaiciai(2,9)
# skaiciai(0, 0)
# skaiciai(-19, -125)

# 11.Sukurkite funkciją, kuri per argumentus gautų automobilių duomenis
# (markė, modelis, gamybos metai, darbinis tūris). Ši funkcija turėtų šiuos
# duomenis išvesti kaip nors gražiai formatuotai. Iškvieskite šią funkciją du
# kartus, perduodant skirtingus duomenis jai.

# def autoDuomenys(mark, mod, gam_m, darb_t):
#     print ('Automobilio markė: ', mark)
#     print ('Automobilio modelis: ', mod)
#     print ('Automobilio gamybos metai: ', gam_m)
#     print ('Automobilio darbinis tūris: ', darb_t)
#     print ()
#
# autoDuomenys('Citroen', 'C5 Aircorss', 2021, 1.4)
# autoDuomenys('Audi', 'A3', 2022, 2.0)

# 12.Sukurkite funkciją sumai skaičiuoti, ši funkcija per argumentus turėtų
# gauti du skaičius, bei išvesti patį veiksmą kartu su atsakymu (pvz 7 + 5 =
# 12). Sukurkite tokias pačias funkcijas skirtumui, sandaugai ir dalmeniui
# rasti. Sukurkite dar vieną funkciją, kuri sugeneruotų du atsitiktinius
# skaičius, bei iškviestų kitas 4 funkcijas, perduodant joms sugeneruotus
# skaičius. Šią bendrąją funkciją iškvieskite keletą kartų.
#
# def suma(a, b):
#     print (f'{a} + {b} = {a + b}')
#
# def skirtumas(a, b):
#     print (f'{a} - {b} = {a - b}')
#
# def sandauga(a, b):
#     print (f'{a} * {b} = {a * b}')
#
# def dalyba(a, b):
#     print (f'{a} / {b} = {a / b}')
#
# def atsitiktiniai ():
#     sk1 = random.randint(1, 100)
#     sk2 = random.randint(1, 20)
#     suma(sk1, sk2)
#     skirtumas(sk1, sk2)
#     sandauga(sk1, sk2)
#     dalyba(sk1, sk2)
#
# atsitiktiniai()
# print('***************')
# atsitiktiniai()


# 13.Susikurkite funkciją, kuri per argumentus priimtų žodžių masyvą.
# Funkcijoje išveskite visus žodžius iš masyvo atskirose eilutėse, nurodant
# žodžio ilgį (simbolių kiekį). Už funkcijos ribų susikurkite žodžių masyvą ir
# užpildykite jį duomenimis. Iškvieskite sukurtą funkciją perduodant turimą
# masyvą.

# def arg_masyvas(argumentai, masyvas):
#     print (argumentai)
#     for i in masyvas:
#         print (f'*  {i}, kur zodzio ilgis - {len(i)}')
#
# zodziai = ['vienas', 'du', 'trys', 'keturi', 'penki']
#
# arg_masyvas('Argumentu masyvas:', zodziai)

# 14.Susikurkite funkciją, kuri per argumentus priimtų skaičių masyvą. Funkcija
# turėtų atspausdinti visus skaičius, šalia jų išvedant to skaičiaus kvadratą ir
# jį padalintą iš dviejų. Už funkcijos ribų susikurkite du skaičių masyvus ir
# užpildykite jį duomenimis. Iškvieskite funkciją du kartus, kiekvieną kartą
# perduodant skirtingą turimą masyvą.

# def skMasyvas(komentaras, masyvas):
#     print (komentaras)
#     for i in masyvas:
#         print (f'<*> {i}, skaiciaus kvadratas - {i ** 2}, kuris padalintas pusiau - {i ** 2 / 2}')
#
# mas1 = [5, 7, 8, 11, 29]
# mas2 = [6, 7, 9, 15, 4, 1]
#
# skMasyvas('Pirmojo masyvo rezultatas: ', mas1)
# print ('-----------------')
# skMasyvas('Antrojo masyvo rezultatas:', mas2)

# 15.Susikurkite funkciją, kuri per argumentus priimtų pažymių masyvą, bei
# studento vardą su pavarde. Funkcija turėtų išvesti studento vardą ir
# pavardę, jo pažymius. Taip pat, suskaičiuoti vidurkį, bei jį išvesti. Už
# funkcijos ribų susikurkite reikiamus kintamuosius ir masyvus, arba
# objektus studentų pažymiams saugoti ir užpildykite juos duomenimis.
# Iškvieskite šią funkciją perduodant visus reikalingus duomenis.

# def pazymiuMasyvas( vardas, pavarde, masyvas):
#     print(f'Studento (-es) {vardas} {pavarde} pazymiai:')
#
#     for i in masyvas:
#         print (i)
#
#     vidurkis = sum(masyvas)/len(masyvas)
#     print (f'Pazymiu vidurkis: {vidurkis:.2f}')
#
# stVardas = 'Tomas'
# stPavarde = 'Tomauskas'
# stPazymiai = [3, 8, 6, 9, 10, 5, 4, 7, 8]
#
# pazymiuMasyvas(stVardas, stPavarde, stPazymiai)

# 16.Susikurkite funkciją, kuri per argumentus priimtų skaičių masyvą. Funkcija
# turėtų rasti didžiausią skaičių iš masyvo bei išvesti gautą atsakymus. Taip
# pat, susikurkite funkciją, kuri per argumentus priimtų masyvą ir į jį
# sugeneruotų pasirinktą kiekį atsitiktinių skaičių. Susikurkite tris tuščius
# masyvus. Iškvieskite atsitiktinių skaičių generavimo funkciją tris kartus,
# kiekvieną kartą perduodant funkcijai vis kitą masyvą. Kai duomenys bus
# užpildyti, masyvuose esančią informaciją išsiveskite norimu būdu (per
# console.log arba per dar atskirą funkciją). Tuomet kvieskite didžiausio
# skaičiaus paieškos funkciją tris kartus, kiekvieną kartą perduodant
# skirtingą masyvą į ją.

# import random
#
# def didziausiasSkaicius (masyvas):
#     skaicius = max (masyvas)
#     print (f'Didziausias skaicius: {skaicius}')
#
# def atsitiktiniaiSkaiciai (masyvas):
#     for i in range (15):
#         ats_skaiciai = random.randint (0, 100)
#         masyvas.append (ats_skaiciai)
#
# masyvas1 = []
# masyvas2 = []
# masyvas3 = []
#
# atsitiktiniaiSkaiciai(masyvas1)
# atsitiktiniaiSkaiciai(masyvas2)
# atsitiktiniaiSkaiciai(masyvas3)
#
# print (f'Pirmas masyvas: {masyvas1}')
# didziausiasSkaicius(masyvas1)
# print (f'Antras masyvas: {masyvas2}')
# didziausiasSkaicius(masyvas2)
# print (f'Trecias masyvas: {masyvas3}')
# didziausiasSkaicius(masyvas3)

# 17.Susikurkite funkciją, kuri grąžintų bet kokį jūsų norimą sakinį. Iškvieskite
# šią funkciją ir išspausdinkite gautus rezultatus.

def norimasSakinys ():
    sak = 'Noriu miego'
    return (sak)

print (norimasSakinys())

# 18.Susikurkite funkciją, kuri grąžintų atsitiktinai sugeneruotą skaičių.
# Iškvieskite šią funkciją kelis kartus ir gautus atsakymus išveskite kokiu
# norite būdu.



# 19.Susikurkite funkciją, kuri per argumentus priimtų studento vardą ir
# vidurkį. Ši funkcija turėtų sugeneruoti iš to sakinį (pvz Studentas Tomas
# turi vidurkį 8.7) ir tai grąžinti kaip atsakymą. Iškvieskite šią funkciją bent
# porą kartų, perduodant vis skirtingus duomenis. Gautus atsakymus
# išveskite.

# 20.Susikurkite funkciją, kuri per argumentus gautų skaičių. Ji turėtų surasti
# duoto skaičiaus mažiausią daliklį (skaičių iš kurio dalinasi be liekanos). Už
# funkcijos ribų sukite ciklą nuo 10 iki 30 ir kiekvienoje ciklo iteracijoje
# iškvieskite šią funkciją, perduodant ciklo kintamąjį.



# 21.Susikurkite funkciją, kuri per argumentus gautų skaičių. Ji turėtų patikrinti
# ar šis skaičius yra pirminis (grąžina True jei pirminis, ir False jei ne
# pirminis). Už funkcijos ribų sukite ciklą nuo 2 iki 15, kiekvienoje ciklo
# iteracijoje išveskite tikrinamą skaičių ir šalia jo iškviestos funkcijos
# atsakymą (pvz 10 false, 11 true, ...).

# 22.Susikurkite bent 3 matematines funkcijas, priimančias reikiamus
# argumentus (pvz suma iš dviejų skaičių, suma iš trijų skaičių, skirtumas,
# sandauga, dalyba) ir grąžinančias atitinkamus atsakymus. Taip pat,
# susikurkite funkciją, kurioje būtų sugeneruojamas reikiamas kiekis
# atsitiktinių skaičių ir išvedami visų skaičiavimų atsakymai su veiksmais
# (iškviečiant atitinkamas kitas funkcijas ir perduodant reikiamus
# kintamuosius) (pagal 23 pavyzdį). Iškvieskite šią pagrindinę funkciją bent
# kartą.



# 23.Susikurkite funkciją kuri priimtų skaičių masyvą per argumentus. Ši
# funkcija turėtų rasti duotųjų skaičių sumą ir grąžinti gautą atsakymą. Už
# funkcijos ribų susikurkite du skaičių masyvus ir užpildykite juos
# duomenimis. Iškvieskite turimą funkciją du kartus, jai abu kartus
# perduodant skirtingą masyvą. Gautus atsakymus išveskite. Taip pat,
# raskite kuri suma gavosi didesnė ir išveskite atsakymą.



# 24.Susikurkite funkciją kuri per argumentus priimtų žodžių masyvą. Ji turėtų
# rasti ir grąžinti ilgiausią žodį masyve. Už funkcijos ribų susikurkite žodžių
# masyvą. Iškvieskite funkciją perduodant jai žodžių masyvą. Gautą
# atsakymą išveskite, taip pat, nurodykite šio žodžio ilgį.



# 25.Susikurkite funkciją kuri per argumentus priimtų pažymių masyvą. Ji
# turėtų patikrinti ar visi pažymiai teigiami: jei visi teigiami turėtų grąžintų
# True kaip atsakymą, o jei yra bent vienas neigiamas - False. Susikurkite du
# pažymių masyvus. Iškvieskite šią funkciją du kartus, abu kartus
# perduodant skirtingus masyvus. Gautus atsakymus paverskite į tekstą
# (jeigu gavote True - išveskite tekstą 'visi studento pažymiai teigiami', jei
# False - 'studentas turi bent vieną neigiamą pažymį'). Šiam iškonvertavimui
# iš True/False į tekstą galite pamėginti pasikurti atskirą funkciją, jai
# perduoti kitos funkcijos atsakymą.



# 26.Pabandykite parašyti bent dvi pasirinktas funkcijas, kuriose būtų
# naudojami default parametrai. Iškvieskite šias funkcijas įvairiais būdais
# (perduodant visus argumentus, bei neperduodant tų kuriuos galima
# praleisti (turinčius default reikšmes)).
