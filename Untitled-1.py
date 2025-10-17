#7.1

zp = int(input("your salary: "))
ras = int(input("amount of expense: "))
eknm = zp-ras
if eknm>zp:
    print('Siz unemdegen summa:', eknm)
else:
    print('Siz artyq summa qoldandynyz:', abs(eknm))

shygyn = input("Айлық/күндік шығындарыңызды енгізіңіз (үтір арқылы жазыңыз): ").split(",")
print('Сіздің жалпы шығындарыңыз:', shygyn)
print("Қайталанатын шығын тұрлерін алып тастасақ:", set(shygyn))
cnst = ("табыс", "шығын", "үнем")
print('Өзгермеу керек мәліметтер', cnst, ". Бұл сіздің мәліметтеріңіздің қауіпсіздігі мен тұрақтылығы үшін.")

po = input("Қандай шығын түрін іздегіңіз келеді?")
if po in shygyn:
    print("Бұл шығын түрі біздің тізімде бар!")
else:
    print("Ондай шығын түрі табылмады")
    add = input("Бұл шығынды тізімге қосқыңыз келеме? (иә/жоқ): ".lower())
    if add == 'иә':
        shygyn.append(po)
        print("Сәтті түрде тізімге қосылды.", shygyn)
    else:
        print("Жақсы, тізімге ештеңе қосылмады.")


print("Айлық шығындарыңызды нақты есептеп көрейік! Әр санаттың атын және жұмсалған сумманы енгізіңіз:")

shygyn_dict = {}
sany = int(input("Неше түрлі шығын енгізесіз? "))

for i in range(sany):
    s1 = input(str(i+1) + "-шығын атауы: ")
    sum = int(input(s1 + " шығынының сомасы (теңге): "))
    shygyn_dict[s1] = sum

print(" Сіздің шығындарыңыз")
for at, aqsha in shygyn_dict.items():
    print(at + ": " + str(aqsha) + " теңге")

jalpy = sum(shygyn_dict.values())
print("Жалпы шығын сомасы: " + str(jalpy) + " теңге")



