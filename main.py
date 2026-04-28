with open("kitoblar.txt", "r") as f:
    lines = f.readlines()
qidir = input("Kitob nomi: ").lower()
for line in lines:
    nom, sahifa, soni = line.strip().split(",")
    if qidir in nom.lower():
        print(f"Topildi: {nom},\nKitob sahifasi: {sahifa}-bet,\nKitob foydalanuvchilar soni: {soni}ta")
max_sahifa = 0
min_sahifa = 10**9
eng_kop_oqilgan = 0
kitob_max = ""
kitob_min = ""
kitob_kop = ""
for line in lines:
    nom, sahifa, soni = line.strip().split(",")
    sahifa = int(sahifa)
    soni = int(soni)
    if sahifa > max_sahifa:
        max_sahifa = sahifa
        kitob_max = nom
    if sahifa < min_sahifa:
        min_sahifa = sahifa
        kitob_min = nom
    if soni > eng_kop_oqilgan:
        eng_kop_oqilgan = soni
        kitob_kop = nom
print("Eng ko‘p sahifali:", kitob_max, max_sahifa,"-bet")
print("Eng kam sahifali:", kitob_min, min_sahifa,"-bet")
print("Eng ko‘p o‘qilgan:", kitob_kop, eng_kop_oqilgan,"ta foydalanuvchi")
with open("result.txt", "w") as f:
    f.write("Eng ko‘p sahifali: " + kitob_max + " " + str(max_sahifa) + "\n")
    f.write("Eng kam sahifali: " + kitob_min + " " + str(min_sahifa) + "\n")
    f.write("Eng ko‘p o‘qilgan: " + kitob_kop + " " + str(eng_kop_oqilgan))
# Kutubxona loyihasida kitoblar text faylida kitoblar nomi,sahifasi,foydalanganlar soni berilgan.
# Dasturda foydalanuvchidan unga kerak bo'lgan kitob nomini so'raydi va kitob nomi, sahifasi va foydalanuvchilar soni haqida malumot chiqaradi.
# Undan so'ng eng ko'p va kam sahifali kitob va eng ko'p o'qilgan kitoblarni chiqarib beradi.
# Natijalarni yangi result text fayliga saqlaydi.