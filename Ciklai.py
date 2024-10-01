# 1. Su for pagalba penkis kartus išveskite savo vardą.

# name = 'Kristina'
# for i in range (5):
#     print (name)

# 2. Parašyti for, kuris išvestų kiekvieną skaičių pradedant nuo 0 ir baigiant 10.

# for i in range (0, 11):
#     print(i)

# 3. Parašyti for, kuris išvestų kas antrą skaičių pradedant 0 ir baigiant 15.

# for i in range (0, 16, 2):
#     print(i)

# 4. Parašyti for, kuris išvestų kas trečią skaičių, pradedant 1 ir baigiant 20.
# Kiekvieną skaičių apskliausti laužtiniais skliaustais. Pvz.: [1][4][7]...

# for i in range (1, 20, 3):
#     print([i])

# 5. Parašyti for, kuris eitų pro kiekvieną skaičių nuo 1 iki 20. Jame apsirašyti if
# sąlygą, kuri patikrintų ar dabartinis skaičius dalinasi iš 4, jei taip tai šį
# skaičių išvesti.

# for i in range (1, 20):
#     if i % 4 == 0:
#         print (f'skaicius {i} dalinasi is 4 be liekanos')

# 6. Išveskite visus skaičius nuo 1 iki 15, prie kiekvieno jų nurodant tai lyginis
# ar nelyginis skaičius. Pvz:
# 1 - nelyginis
# 2 - lyginis
# 3 - nelyginis
# ...

# for i in range (1, 16):
#     if i % 2 == 0:
#         print (f'skaicius {i} yra lyginis')
#     else:
#         print (f'skaicius {i} yra nelyginis')

# 7. Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti. Patikrinkite,
# kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga). Jei rėžiai
# tinkami, tuomet vykdyti for, kuris atskirose eilutėse išvestų kiekvieną
# skaičių iš tų rėžių, bei atskiriant tarpu - tų skaičių kvadratus.

# pradzia = int(input("Įveskite rėžių pradžią: "))
# pabaiga = int(input("Įveskite rėžių pabaigą: "))
#
# if pradzia < pabaiga:
#     for i in range(pradzia, pabaiga + 1):
#         print(f"skaicius ir kvadratas: {i} {i ** 2}")
# else:
#     print("rėžių pradžia yra mažesnė nei pabaiga")

# 8. Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti. Patikrinkite,
# kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga). Jei rėžiai
# tinkami, tuomet vykdyti for, kuris iš duotų skaičių išvestų visus nelyginius
# skaičius arba tuos, kurie dalinasi iš 8.

# pradzia = int(input("Įveskite rėžių pradžią: "))
# pabaiga = int(input("Įveskite rėžių pabaigą: "))
#
# if pradzia < pabaiga:
#     for i in range(pradzia, pabaiga + 1):
#         if i % 2 != 0 or i % 8 == 0:
#             print (i)
# else:
#     print("rėžių pradžia yra mažesnė nei pabaiga")

# 9. Leiskite vartotojui įvesti savo vardą. Ciklą for vykdykite tiek kartų kiek
# tame varde yra raidžių. Visais atvejais išveskite tą patį pasisveikinimą,
# pavyzdžiui "Labas, Ieva" (ši eilutė kartotųsi 4 kartus).

# name = str(input("Įveskite savo vardą: "))
# for i in range(len(name)):
#     print(f'{name}{[i+1]}')

# 10.Susikurkite tokį ciklą: for elementas in [88, 65, 21, 26, 47]
# Iš duotų skaičių išveskite visus skaičius, kurie yra lyginiai.

# for elementas in [88, 65, 21, 26, 47]:
#     if elementas % 2 == 0:
#         print (elementas)

# 11.Leiskite vartotojui nurodyti rėžių pradžią, pabaigą, žingsnį. Taip pat, kokius
# skaičius jis nori matyti (lyginius ar nelyginius). Patikrinkite ar rėžiai tinkami,
# jei taip vykdykite ciklą, kuris eitų per nurodytą rėžių, darant atitinkamą
# žingsnį. Išveskite tik tokius skaičius kokius vartotojas pasirinko (lyginius
# arba nelyginius).

# pradzia = int(input("Įveskite rėžių pradžią: "))
# pabaiga = int(input("Įveskite rėžių pabaigą: "))
# zingsnis = int(input("Įveskite žingsnį: "))
# skaicius = str(input("Įveskite kokius skaičius norite matyti (lyginius ar nelyginius): "))
#
# if pradzia < pabaiga:
#     for i in range(pradzia, pabaiga +1, zingsnis):
#         if skaicius == "lyginius" and i % 2 == 0:
#             print (i)
#         elif skaicius == "nelyginius" and i % 2 !=0:
#             print (i)
# else:
#     print ("rėžių pradžia yra mažesnė nei pabaiga")

# 12.Su for pagalba, pamėginkite išvesti tokią eglutę:
# *
# **
# ***
# ****
# *****
# (papildomai) leiskite vartotojui pasirinkti kokio dydžio eglutė turėtų būti
# išvesta.

# for i in range(1, 6):
#     print('*' * i)

# dydis = int(input("Įveskite eglutės dydį: "))

# for i in range(1, dydis + 1):
#     print('*' * i)

# 13.Leiskite vartotojui įvesti bet kokį žodį, bei pasirinkti po kiek kartų turėtų
# būti pakartojama kiekviena raidė. Su ciklo pagalba išveskite kiekvieną
# raidę iš žodžio atskiroje eilutėje, taip pat, tą raidę eilutėje kartokite tiek
# kartų kiek pasirinko vartotojas (16 pvz).

# zodis = str(input("Įveskite bet kokį žodį: "))
# kartai = int(input("Po kiek kartų turėtų būti kartojama raidė? "))

# for i in zodis:
#     print (i * kartai)


# 14.(papildomai, sunkiau) Be daugybos veiksmo programoje, sudauginkite du
# skaičius.

# sk1 = int(input("Įveskite pirmąjį skaičių: "))
# sk2 = int(input("Įveskite antrąjį skaičių: "))
#
# sandauga = 0
#
# for i in range(sk2):
#     sandauga += sk2  # pridedame 'a' prie rezultato
#
# print(f"{sk1} padauginta iš {sk2} yra {sandauga}")

# 15.Raskite visų skaičių nuo 1 iki 100 sumą.

# suma = 0
#
# for i in range(100):
#     suma += i
# print(f'gauta suma: {suma}')

# 16.Raskite visų lyginių skaičių nuo 20 iki 50 sumą.

suma = 0

for i in range(20, 50):
    if i % 2 == 0:
        suma += i

print(f'lyginiu suma: {suma}')

# 17.Raskite visų nelyginių skaičių nuo 30 iki 60 sumą.

suma = 0

for i in range(30, 60):
    if i % 2 != 0:
        suma += i

print(f'nelyginiu suma: {suma}')

# 18.Rasti visų skaičių, žemesnių už 1000 ir kurie dalinasi iš 3 arba 5, sumą.
# Pavyzdys:
# Visi skaičiai mažesni už 10 ir kurie dalinasi iš 3 arba 5 yra: 3, 5, 6, 9.
# Šių skaičių suma yra 23.
# Turite gauti 233168 atsakymą.

suma = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        suma += i

print(f'suma: {suma}')

# 19.The "Fizz-Buzz test" is an interview question designed to help filter out the
# 99.5% of programming job candidates who can't seem to program their
# way out of a wet paper bag. The text of the programming assignment is
# as follows:
#
# "Write a program that prints the numbers from 1 to 100. But for multiples
# of three print “Fizz” instead of the number and for the multiples of five
# print “Buzz”. For numbers which are multiples of both three and five print
# “FizzBuzz”."


# 20.(sunkesnė) Parašyti for ciklą, kuris išvestų norimą kiekį fibonačiaus skaičių
# į ekraną. Fibonačiaus sekoje kiekvienas skaičius yra lygus prieš jį ėjusių
# dviejų skaičių sumai: 1, 1, 2, 3, 5, 8, 13, 21...
# 1. Susikurkite tris sveikųjų skaičių kintamuosius, kurie jums padės tai pasiekti.
# 1. Pirmi du kintamieji saugos paskutinius du skaičius.
# 2. Trečiasis bus šių pirmų dviejų skaičių suma.
# 2. Pirmus du skaičius išveskite ne cikle, o prieš jį ir ciklą pradėkite vykdyti nuo 2, o ne nuo 0.
# 3. Kiekvieno ciklo metu turite perskaičiuot trečiąjį skaičių (pirmų dviejų skaičių sudėtis),
# tuomet pirmasis skaičius yra lygus antram, o antrasis lygus trečiam, išvesti į ekraną trečią
# skaičių.