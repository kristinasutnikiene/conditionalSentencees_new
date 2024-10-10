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
# kiekis = int(input("Įveskite, kiek pažymių norite pridėti: "))

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

# city_list = ['Vilnius', 'Kaunas', 'Klaipeda']
# print (city_list)
# city_list.insert(1, input("Iraykite miesta: "))
# print (city_list)

# 5. Sukurkite pasirinktą list ir užpildykite jį duomenimis. Iš jo pašalinkite
# keletą įrašų, tiesiog parašant pop() funkciją. Taip pat, sukurkite, kad
# vartotojas galėtų pasirinkti kiek dar duomenų pašalinti ir pašalinkite iš list
# pasirinktą kiekį įrašų.

# list = [7, 8, 9, 5, 6, 2, 8]
# list.pop()
# print (list)
# list.pop (2)
# print (list)
#
# list.pop(int(input("kuri skaiciu istrinti? ")))
#
# print (list)

# 6. Sukurkite list su pasirinktais duomenimis. Patikrinkite ar sąraše yra
# daugiau nei 5 įrašai ir jeigu taip - jį išvalykite (clear funkcija).

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print (list)
#
# print(f'sarase skaiciu yra: {len(list)}')
#
# if len(list) > 5:
#     list.clear()
# print (list)

# 7. Sukurkite list, kuriame būtų surašyti bet kokie žodžiai. Leiskite vartotojui
# atlikti paiešką tame sąraše - vartotojas įvestų norimą žodį ir programa
# pasakytų ar tame sąraše tas žodis yra ir jeigu yra, tai kurioje vietoje.

# list = ["mano", "namas", "yar", "labai", "mazas"]
# naujas = str(input('iveskite zodi ir patikrinkite ar jusu zodis yra sarase? '))
# if naujas in list:
#     print (f'{True} \n ivesto zodzio vieta sarase: {list.index (naujas)+1}')
# else:
#     print (f'{False} \n {naujas} nera sarase')

# 8. Sukurkite sąrašą, kuriame būtų surašyti studentų pažymiai. Galite
# padaryti taip, kad pasirinktą kiekį pažymių galėtų suvesti pats vartotojas.
# Programa turi pasakyti kiek dešimtukų studentas turi.

# st_paz = []
# kiek_paz = int(input("kiek pazymiu norite ivesti: "))
# for i in range (kiek_paz):
#     paz = int(input("iveskite paymius: "))
#     st_paz.append(paz)
# print (f'studentu pazymiai: {st_paz}')
#
# desimtukai = st_paz.count(10)
# paz_vid = sum(st_paz)/len(st_paz)
#
# print (f'pazymiu vidurkis: {paz_vid}')
#
# print (f'desimtuku yra: {desimtukai}')

# 9. Susikurkite automobilių markių sąrašą ir užpildykite jį duomenimis
# (kuriantis sąrašą arba su vartotojo įvestimi). Išveskite turimus duomenis
# ekrane. Tuomet surikiuokite automobilių markes didėjimo tvarka ir
# išveskite. Taip pat, surikiuokite mažėjimo tvarka ir išveskite.

# markes = []
# kiekis = int(input("kiek automobiliu markiu norite ivesti? "))
#
# for i in range (kiekis):
#     auto = str(input(f"iveskite {i+1} automobiliu markes: "))
#     markes.append(auto)
#
# print (f"Auto sarasa: {markes}")
#
# markes.sort()
# print (f"surikiuota didejimo tvarka: {markes}")
#
# markes.reverse()
#
# print ((f"surikiuota mazejimo tvarka: {markes}"))

# 10.Susikurkite studento pažymių sąrašą ir užpildykite duomenimis. Išveskite
# tris didžiausius turimus pažymius.

# st_paz = []
# kiekis = int(input("kiekis? "))
#
# for i in range (kiekis):
#     paz = int(input(f"Iveskite {i+1} pazmius: "))
#     st_paz.append(paz)
#
# print (f"Ivesti pazymiai: {st_paz}")
# st_paz.sort(reverse=True)
# print (st_paz)
# trys_did = st_paz[:3]
#
# print (f"Trys didziausi pazymiai: {trys_did}")


# 11.Susikurkite studentų pažymių sąrašą ir užpildykite duomenimis. Jeigu
# studentas turi neigiamų pažymių (1, 2, 3, arba 4), išveskite kiek tokių
# pažymių jis turi.

# st_paz = [7, 6, 9, 1, 8, 2, 3, 7, 9, 4, 6]
# st_paz.sort()
# print (st_paz)
# neig = [paz for paz in st_paz if paz < 5]
#
# print (len(neig))

# 12.Susikurkite pasirinktą sąrašą su duomenimis. Pritaikykite list slicing tokiais
# būdais ir gautus atsakymus išveskite:
# 1. Paimkite pirmus tris narius.
# 2. Paimkite du narius, pradedant trečiu.
# 3. Paimkite paskutinius keturis narius.
# 4. Paimkite kas antrą narį, pradedant trečiu nariu.
# 5. Paimkite visus atbuline tvarka.



# 13.Susikurkite list studentų vidurkiams saugoti. Išsitraukite ir pasidėkite į
# atskirą list tris didžiausius pažymius (galite surikiuoti ir išsikirpti ką reikia).

# 14.Pamėginkite sukurti žodžių žodyną. Šį žodyną turėtų užpildyti vartotojas,
# įvesdamas visus norimus žodžius. Po kiekvieno įvedimo jam turėtų būti
# parodomi visi žodžiai, tačiau surikiuoti, t.y. įdėjus žodį į sąrašą, jį
# surikiuokite iš naujo.

# 15.Sukurkite sąrašą, kuriame saugotumėte sandėlio likučius. Į atskirą sąrašą
# persikelkite visus likučius kurių lieka mažai (mažiau nei 5 vnt. arba trijų
# prekių likučius, kurių likę mažiausiai).

# 17.Pabandykite atlikti list unpacking. Sąraše sudėkite informaciją ir iškart
# padarykite list unpacking. Tai atlikus išsiveskite gautas reikšmes.
# Pavyzdžiui, sąraše galėtų būti taip pateikta informacija:
# 1. pirmoje vietoje - naudojama programavimo kalba
# 2. antroje vietoje - aplinka (desktop, web, ...)
# 3. likusiose vietose nuo trečios - failai, su kuriais būtų dirbama