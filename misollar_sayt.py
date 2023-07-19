# saytdan misollar bajaramiz
# 1_misol ==>
"""
Sizga ikkita manfiy bo'lmagan butun sonni ifodalovchi ikkita bo'sh bo'lmagan bog'langan ro'yxatlar beriladi.
Eng muhim raqam birinchi bo'lib keladi va ularning har bir tugunida bitta raqam mavjud.
Ikki raqamni qo'shing va yig'indini bog'langan ro'yxat sifatida qaytaring.
Siz ikkita raqamda 0 raqamidan tashqari hech qanday bosh nol yo'q deb taxmin qilishingiz mumkin.
Har bir bog'langan ro'yxatdagi tugunlar soni [1, 100] oralig'ida.
0 <= Node.val <= 9
Ro'yxat boshida nolga ega bo'lmagan raqamni ifodalashi kafolatlanadi.
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
"""
def fun_lst(lst1,lst2):
    lst3 = []
    if len(lst1)>len(lst2):
        for i in lst1:
            pass
        for j in lst2:
            if i==j:
                lst3.append(i)
    return lst3

lst1=[1,2,3,4,6,7]
lst2=[1,2,3,4,5]
#print(fun_lst(lst1,lst2)) chiqmadi

# 2_misol ==>
"""
Butun sonlar massivi va butun sonli maqsadni hisobga olgan holda, ikkita raqamning indekslarini maqsadni qo'shadigan qilib qaytaring.
Siz har bir kirishda aynan bitta yechim bo'ladi deb taxmin qilishingiz mumkin va siz bir xil elementni ikki marta ishlata olmaysiz.
Javobni istalgan tartibda qaytarishingiz mumkin.

Kirish: raqamlar = [2,7,11,15], maqsad = 9
Chiqish: [0,1]
Izoh: nums[0] + nums[1] == 9 bo'lgani uchun biz [0, 1] ni qaytaramiz.
"""


def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
nums = [2,7,11,15]
target = 9
#print(twoSum(nums,9)) # oldin bajargan ekanman😅

# 3_misol ==>
"""Sizga ikkita manfiy bo'lmagan butun sonni ifodalovchi ikkita bo'sh bo'lmagan bog'langan ro'yxatlar beriladi. 
Raqamlar teskari tartibda saqlanadi va ularning har bir tugunida bitta raqam mavjud. 
Ikki raqamni qo'shing va yig'indini bog'langan ro'yxat sifatida qaytaring.
Siz ikkita raqamda 0 raqamidan tashqari hech qanday bosh nol yo'q deb taxmin qilishingiz mumkin.
Input: l1 = [2,4,3],
       l2 = [5,6,4]
       l2_= [4,6,5]
Output: [7,0,8]
Explanation: 342 + 465 = 807
"""
def fun_lst1(lst1,lst2):
    lst3 = []
    if len(lst1) != len(lst2):
        return "Ro'yxatlar uzunligi bir xil bo'lishi kerak"
    for i in range(len(lst1)):
        lst=lst2[::-1]
        lst3.append(lst1[i] + lst[i])
    return lst3
#print(fun_lst1([2,4,3],[5,6,4]))

def palindrom_tekshirish(n):
    if n < 0:
        return False
    original = n
    reverse = 0
    while n > 0:
        last_digit = n % 10
        reverse = reverse * 10 + last_digit
        n //= 10
    return original == reverse
#print(palindrom_tekshirish(121))

# chiqmayabti tichgina vazifani qilayda
"""# Base class
#Father attrs(first_name,last_name,gender,profession),methods(
# set/get/del profession,
#get/set/del address,get/set/del surname)
# Mother attrs(first_name,last_name,gender) methods()
#child(Mother,Father) attrs(),methods(get/set/del address, get/set/del surname, get/set/del last_name

# Asosiy sinf
#Ota attrlari(ismi,familiyasi,jinsi,kasbi),usullari(
# to'plam/olish/del kasbi,
#get/set/del manzili, get/set/del familiyasi)
# Onaning attrlari(ismi,familiyasi,jinsi) usullari()
#child(Ona,Ota) attrs(),usullar(get/set/del manzili, get/set/del familiyasi, get/set/del familiyasi
"""


class Manzil:
    def __init__(self, viloyat, tuman, mahala, uy):
        self.viloyat = viloyat
        self.tuman = tuman
        self.mahala = mahala
        self.uy = uy

    def __repr__(self):
        return f"viloyati: {self.viloyat} tumanai: {self.tuman}" \
               f" mahala: {self.mahala} uy_raqami: {self.uy}"

    def get_viloyat(self):
        return self.viloyat

    def get_tuman(self):
        return self.tuman

    def get_mahala(self):
        return self.mahala

    def get_uy(self):
        return self.uy


manzil = Manzil("Buxoro", "Qarako'l", "Sayot", 164)
manzil1 = Manzil("Buxoro", "Olot", "Mirishkor", 32)
class Ota:
    def __init__(self,ism,familya,jinsi,kasbi,manzil,til):
        self.ism = ism
        self.familyasi = familya
        self.jinsi = jinsi
        self.kasbi = kasbi
        self.manzil = manzil
        self.til = til

    def __repr__(self):
        return f"ismi: {self.ism} familyasi: {self.familyasi} " \
               f"jinsi: {self.jinsi} ishlaydigan kasbi: {self.kasbi} " \
               f" manzili ==> {self.manzil} qaysi tillari bilishi {self.til}"

    def get_ism(self):
        return  self.ism

    def get_familyasi(self):
        return self.familyasi

    def get_jinsi(self):
        return self.jinsi

    def get_kasb(self):
        return self.kasbi

    def get_manzi(self):
        return self.manzil

    def get_til(self):
        return self.til

    def speak(self):
        return f"ismi: {self.ism} familyasi: {self.familyasi} " \
               f"jinsi: {self.jinsi} ishlaydigan kasbi: {self.kasbi} " \
               f" manzili ==> {self.manzil} biladigan tillari: {self.til}"

ota = Ota("Rustam","Jumanazarov","erkak","Talaba",manzil,"UZB_RUS")
# print(ota)
# print(getattr(ota,'ism'))
# setattr(Ota,'ism',"Muhammadali")
# delattr(ota,'ism')
# print(ota)
# print(ota.speak())


class Ona:
    def __init__(self,ism,familya,jinsi,kasbi,manzil,til):
        self.ism = ism
        self.familyasi = familya
        self.jinsi = jinsi
        self.kasbi = kasbi
        self.manzil = manzil
        self.til = til

    def __repr__(self):
        return f"ismi: {self.ism} familyasi: {self.familyasi} " \
               f"jinsi: {self.jinsi} ishlaydigan kasbi: {self.kasbi} " \
               f" manzili ==> {self.manzil} biladigan tillari: {self.til}"

    def get_ism(self):
        return  self.ism

    def get_familyasi(self):
        return self.familyasi

    def get_jinsi(self):
        return self.jinsi

    def get_kasb(self):
        return self.kasbi

    def get_manzi(self):
        return self.manzil

    def get_til(self):
        return self.til

    def speak(self):
        return f"ismi: {self.ism} familyasi: {self.familyasi} " \
               f"jinsi: {self.jinsi} ishlaydigan kasbi: {self.kasbi} " \
               f" manzili ==> {self.manzil} biladigan tillari: {self.til}"

ona = Ona("Durdona","Hamdamova","ayol","O'qtuvchi",manzil1,"UZB_INGILIS")
# print(ona)
# print(getattr(ona,'ism'))
# setattr(Ona,'ism',"Shaxina")
# delattr(ona,'ism')
# print(ona)
# print(ona.speak())


class Bola(Ota,Ona):
    def __init__(self,ism,familyasi,jinsi,kasbi,manzil,til,hobbisi):
       super().__init__(ism,familyasi,jinsi,kasbi,manzil,til)
       self.hobbisi = hobbisi

    def speak(self):
         return f"ismi: {self.ism} familyasi: {self.familyasi} " \
               f"jinsi: {self.jinsi} ishlaydigan kasbi: {self.kasbi} " \
               f" manzili ==> {self.manzil} qaysi tillari bilishi: {self.til}" \
                f"qiziqadigan hobbisi: {self.hobbisi}"
bola = Bola("Ali","Valiyev","erkak","Talaba",manzil,"UZB_RUS_INGILIS","PUBK")
print(bola)
print(getattr(bola,'hobbisi'))
# setattr(bola,'kasbi','dasturchi')
# delattr(bola,'jinsi')
#print(bola)









