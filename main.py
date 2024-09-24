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

# 10. Susikurkite skaičiui saugoti skirtą kintamąjį, arba reikšmę leiskite suvesti vartotojui.
# Tikrinkite (naudojant visas if sąlygos dalis):
# 1. Ar skaičius yra lyginis?
# 2. Ar dalinasi iš 5?
# 3. Ar skaičius lygus 3?
# 4. Jeigu nieko nepavyko rasti, išveskite klaidos pranešimą.

# sk = int(input("Iveskite skaicius: "))
# if sk %2 == 0:
#     print("lyginis")
# elif sk %5 == 0:
#     print("dalinasi is 5")
# elif sk == 3:
#     print("lygus 3")
# else:
#     print("false")

# 11. Susikurkite tris skaičius arba leiskite visus skaičius suvesti vartotojui.
# Tikrinkite (naudojant visas if sąlygos dalis):
# 1. Ar pirmi du skaičiai lygūs? 2. Ar pirmas ir trečias skaičiai lygūs?
# 3. Ar trečias skaičius didesnis už pirmą? 4. Ar antras skaičius lygus dvigubai trečio skaičiaus reikšmei?
# 5. Ar pirmas skaičius dalinasi iš 3? 6. Jei nieko nepavyko rasti, išveskite klaidos pranešimą.
#
# no1 = int(input("Pirmas skaicius: "))
# no2 = int(input("Antras skaicius: "))
# no3 = int(input("Trecias skaicius: "))
#
# if no1==no2:
#     print("1 ir 2 lygus")
# elif no1==no3:
#     print("1 ir 3 lygus")
# elif no3>no1:
#     print("3 didesnis uz 1")
# elif no2==no3*2:
#     print("2 lygus dvigubam 3")
# elif no1 %3==0:
#     print("3 dalinasi is 3")
# elif no2==no3*2:
#     print("2 lygus dvigubam 3")
# else:
#     print("nepavyko")

# 12. Leiskite vartotojui suvesti tris skaičius. Suraskite kuris iš šių skaičių yra didžiausias.

# no1 = int(input("Pirmas skaicius: "))
# no2 = int(input("Antras skaicius: "))
# no3 = int(input("Trecias skaicius: "))
#
# didz = max(no1,no2,no3)
#
# if no1==didz:
#     print("pirmas didziausias")
# elif no2==didz:
#     print("antras didziausias")
# elif no3==didz:
#     print("trecias didziausias")
# else:
#     print("gavos nesamone")

# 13. Leiskite vartotojui suvesti tris skaičius. Suraskite kuris iš šių skaičių yra mažiausias.
# no1 = int(input("Pirmas skaicius: "))
# no2 = int(input("Antras skaicius: "))
# no3 = int(input("Trecias skaicius: "))
#
# maz = min(no1,no2,no3)
#
# if no1==maz:
#     print("pirmas maziausias")
# elif no2==maz:
#     print("antras maziausias")
# elif no3==maz:
#     print("trecias maziausias")
# else:
#     print("gavos nesamone")

# 14. Susikurkite trijų egzaminų rezultatų kintamuosius arba paprašykite, kad vartotojas suvestų šias reikšmes.
# Suraskite pažymių vidurkį. Atlikite šiuos patikrinimus:
# 1. ar gautas vidurkis yra [8-10];
# 2. ar gautas vidurkis yra [5-8);
# 3. ar gautas vidurkis yra < 5.

rezultatas1 = int(input("Įveskite pirmo egzamino rezultatą: "))
rezultatas2 = int(input("Įveskite antro egzamino rezultatą: "))
rezultatas3 = int(input("Įveskite trečio egzamino rezultatą: "))

vidurkis = (rezultatas1 + rezultatas2 + rezultatas3) / 3

print(f"Egzaminų vidurkis: {vidurkis:.2f}")
# {vidurkis:.2f} vidurkis suapvalinamas iki 2 sk po kablelio kaip float

if 8 <= vidurkis <= 10:
    print("Vidurkis yra tarp 8 ir 10 (įskaitant). Puikus rezultatas!")
elif 5 <= vidurkis < 8:
    print("Vidurkis yra tarp 5 ir 8. Vidutinis rezultatas.")
elif vidurkis < 5:
    print("Vidurkis yra mažesnis nei 5. Reikia pasistengti daugiau.")
