# 1.
# import random
#
# vardai = ['Andrius', 'Kristina','Ieva','Ruta','Joris']
# print (vardai)
# print (vardai[0])
# print (vardai[4])
# print ('Vardu skaicius: ', len(vardai))

# 2.
# ugiai = [178, 205, 159, 146, 170, 188, 190]
# print (f'ugiai: {ugiai}, \nivesta ugiu: {len(ugiai)}')

# 3.
# Sukuriame tuščią sąrašą pažymiams saugoti
pazymiai = []

# Paprašome vartotojo įvesti, kiek pažymių jis nori pridėti
kiekis = int(input("Įveskite, kiek pažymių norite pridėti: "))

# Naudojame ciklą norimam kiekiui pažymių pridėti
# for i in range(kiekis):
#     pazymys = int(input(f"Įveskite {i+1}-ąjį pažymį: 4"))
#     pazymiai.append(pazymys)
#
# # Išvedame visus pažymius ir jų kiekį
# print("Įvesti pažymiai:", pazymiai)
# print("Viso pažymių kiekis:", len(pazymiai))

# import random
#
# for i in range(kiekis):
#     pazymys = random.randint(1, 10)
#     pazymiai.append(pazymys)
#
# # Išvedame visus pažymius ir jų kiekį
# print("\nSugeneruoti pažymiai:", pazymiai)
# print("Viso pažymių kiekis:", len(pazymiai))

# 4. Susikurkite miestų sąrašą. Į šį list pridėkite duomenų kurdami patį list.
# Toliau sukurkite galimybę vartotojui papildyti list. Išveskite tiek pradinį list,
# tiek papildytą duomenimis. Pamėginkite papildyti programą, kad
# vartotojas galėtų pasirinkti į kurią list vietą būtų įrašytas naujas miestas.

city_list = ['Vilnius', 'Kaunas', 'Klaipeda']