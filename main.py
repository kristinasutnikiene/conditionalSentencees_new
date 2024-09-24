#2. Liepkite vartotojui suvesti savo amžių. Patikrinkite ar amžius yra didesnis
#arba lygus 18-ai, jei taip -išveskite "jūs galite balsuoti".

# amzius = int(input('Kiek jums metu?'))
# if  amzius >= 18:
#     print('Jus galite balsuoti!')
# else:
#     print('Jus negalite balsuoti :(')

# 3. Leiskite vartotojui suvesti norimą kiekį pažymių (pavyzdžiui, jūs nusimatote 3-is kintamuosius,
# tai leidžiate padaryti 3 įvedimus). Raskite šių pažymių vidurkį.
# Patikrinkite ar vidurkis teigiamas (daugiau arba lygu 5-iems), jei taip -išveskite "vidurkis teigiamas".

# print ('Iveskite 4 pazymius:')
# Mat = int(input("Matematika "))
# Liet = int(input('Lietuviu kalba '))
# Fiz = int(input('Fizika '))
# Ang = int(input('Anglu kalba '))
#
# Vid = (Mat+Liet+Fiz+Ang)/4
# print (f'Vidurkis: {Vid}')
#
# if Vid  >= 5:
#     print('Vidurkis yra teigiamas!')
# else:
#     print('Liekate kartoti kurso!')

# 4. Susikurkite skaičiaus kintamąjį arba leiskite šį skaičių įvesti vartotojui.
# Atlikite šiuos patikrinimus ir veiksmus:
# 1. Jei skaičius dalinasi iš 5, tuomet išveskite šio skaičiaus daugybos lentelę nuo 1 iki 5.
# 2. Jei skaičius lyginis, tuomet išveskite šį skaičių, jo kvadratą ir jį padalintą iš 2.
# 3. Jei skaičius nesidalina iš 7, tuomet susikurkite antrąjį kintamąjį, išveskite šių dviejų
# skaičių sumą, skirtumą, sandaugą, dalmenį.

# number = int(input("Įveskite skaičių: "))
# if number % 5 == 0:
#     print(f"{number} daugybos lentelė:")
#     for i in range(1, 6):
#         print(f"{number} x {i} = {number * i}")
#
# elif number %2 == 0:
#     print(f'Skaiciaus {number} kvadratas {number **2}, o padalinus is 2 gausime {number/2}')
#
# elif number %7 != 0:
#     number2 =int(input('Iveskite nauja skaiciu: '))
#     print (f'Skaiciu suma {number+number2}, skirtumas {number-number2}, sandauga {number*number2} ir dalyba {number/number2}')
#
# else:
#     print ('niekam tike skaiciai :D')

# 5. Susikurkite tris skaičių kintamuosius su norimomis reikšmėmis, arba leiskite šiuos skaičius
# suvesti vartotojui. Patikrinkite šias sąlygas (naudojant elif dalis):
# 1. Ar pirmas skaičius didesnis už antrą?
# 2. Ar antras skaičius didesnis už trečią?
# 3. Ar trečias skaičius didesnis už pirmą?

# no1 = int(input("Pirmas skaicius: "))
# no2 = int(input("Antras skaicius: "))
# no3 = int(input("Trecias skaicius: "))
#
# if no1>no2:
#     print('pirmas didesnis uz antra')
# elif no2>no3:
#     print('antras didesnis uz trecia')
# elif no3>no1:
#     print('trecias didesnis uz pirma')
# else:
#     print('nu ner sprendimo')

# 6. Susikurkite tris skaičių kintamuosius su norimomis reikšmėmis, arba leiskite šiuos skaičius
# suvesti vartotojui. Patikrinkite šias sąlygas (naudojant elif dalis):
# 1. Ar pirmi du skaičiai yra lygūs?
# 2. Ar paskutiniai du skaičiai yra lygūs?
# 3. Ar pirmas skaičius yra lygus 0?
# 4. Ar antras skaičius neigiamas?
# 5. Ar trečias skaičius teigiamas?
#
# no1 = int(input("Pirmas skaicius: "))
# no2 = int(input("Antras skaicius: "))
# no3 = int(input("Trecias skaicius: "))
#
# if no1==no2:
#     print('pirmas ir antras lygus')
# elif no2!=no3:
#     print('antras nelygus treciam')
# elif no1==0:
#     print('pirmas lygus 0')
# elif no2 < 0:
#     print('antras neigiamas')
# elif no3>0:
#     print('trecias teigiamas')
# else:
#     print('vel ner sprendimo')

# 7. Susikurkite kintamąjį egzamino pažymiui saugoti [0-10]. Naudojant elif dalis
# patikrinkite šias sąlygas ir išveskite atitinkamą tekstą:
# 1. Jei pažymys yra lygus 10 išvesti “puiku”.
# 2. Jei pažymys yra lygus arba didesnis nei 9 išvesti “labai gerai”.
# 3. Jei pažymys yra lygus arba didesnis nei 7 išvesti “gerai”.
# 4. Jei pažymys yra lygus arba didesnis nei 5 išvesti “patenkinamai”.
# 5. Jei pažymys mažesnis nei 5 išvesti “egzaminas neišlaikytas”.

# ev = int(input("Iveskite egzamino pazimi (0-10): "))
# if ev==10:
#      print('puiku')
# elif ev>=9:
#     print('labai gerai')
# elif ev>=7:
#     print('gerai')
# elif ev>=5:
#     print('patenkinamai')
# elif ev<5:
#     print('egzaminas neišlaikytas')

# 7. Leiskite vartotojui suvesti norimą skaičių. Patikrinkite ar jis yra lyginis,
# jei taip išveskite vieną informaciją, jei ne -kitą.
#no = int(input("Iveskite skaiciu: "))
# if no %2 == 0:
#      print('lyginis')
# else:
#     print('nelyginis')

# 8. # Leiskite vartotojui suvesti norimą skaičių. Patikrinkite ar šis skaičius dalinasi iš 7,
# jei taip išveskite vieną tekstą, jei ne -kitą.
# no = int(input("Iveskite skaiciu: "))
# if no %7 == 0:
#      print('dalinasi is 7')
# else:
#     print('nesidalina is 7')

# 9. # Susikurkite kintamąjį, kuriame nurodytumėte kelią iki norimo failo. Patikrinkite ar šis failas
# yra .py tipo, jei taip išveskite vieną tekstą, jei ne -kitą.

# failo_kelias = str(input("Iveskite failo kelia: "))
# if failo_kelias.endswith(".py"):
#     print("Tai yra Python failas")
# else:
#     print("Tai nėra Python failas")


