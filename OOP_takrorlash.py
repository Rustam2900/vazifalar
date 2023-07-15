# class Person:
#     def greet(self, name):
#         #print("Hello, " + name + "!")
#
# person = Person()
# person.greet("Alice")

"""class Student: 
    def __init__(self, name, age, region): 
        self.name = name 
        self.age = age 
        self.region = region 
 
    @property 
    def region_(self): 
        return self.region 
 
    @region_.setter 
    def region_(self, value): 
        self.region = value 
 
    @region_.deleter 
    def region_(self): 
        del self.region 
    # Property 
    # region_ = property(fget=get_region, fset=set_region) 
 
 
# region = 'Tashkent' 
# region = 'Samarkand' 
 
student = Student('Alisher', 25, 'Tashkent') 
# print(student.get_region()) 
# 
# print(student.get_region()) 
# 
# student.set_region('Samarkand') 
# student.region_ = 'Samarkand' 
 
# print(student.region_) 
student.region_ = 'Fergana' 
# print(student.region_) 
# del student.region_ 
# print(student.region_) 
 
# help(Student) 
 
# getattr 
# getattr(student, 'ne') 
 
# setattr 
# x.y = v 
setattr(student, 'name', 'John') 
# student.country = 'Uzbekistan' 
 
print(getattr(student, 'name')) 
# getattr(student, 'country') 
# delattr(student, 'country') 
# getattr(student, 'country')"""

class Talaba:
    def __init__(self,id,ism,familya,tyil):
        self.id = id
        self.ism = ism
        self.familya = familya
        self.tyil = tyil

    def __repr__(self):
        return f"aydi raqami {self.id} ismmi {self.ism} familyasi {self.familya} tug'ulgan tili {self.tyil}"

talaba = Talaba(29,"Rustam","Jumanazarov",2005)
#help(talaba) # class ichidaki hammasini chiqarib beradi
#print(getattr(talaba,'id')) # getattr vazifasi qaysi birini bersanggiz o'shani olib beradi
#setattr(talaba,'id',13) setattr vazifasi esa o'zgartirib beradi
#delattr(talaba,'id') # delattr vazifasi o'chiradi
#print(talaba)

class PersonInfo:
    country = "UZB"

    def __init__(self,ism,familya,yosh):
        self.ism = ism
        self.familya = familya
        self.yosh = yosh
    def get_ism_fam(self):
        return self.ism + ' ' + self.familya

    @staticmethod
    def to_upper(text):
        return text.upper()

    @classmethod
    def set_country(cls,value) -> None:
        cls.country = value

person = PersonInfo("Axtam","Yo'ldoshov",18)
person1 = PersonInfo("Bekki","Yo'ldoshov",19)
# print(person.ism,person.familya)
# print(person1.ism,person1.familya)
# print(person.get_ism_fam())
# print(person1.get_ism_fam())
#print(person.to_upper("salom"))
# person.set_country("USA")
# print(person.country)


# from random import  choices,randrange
#
# num = choices([i for i in range(10_000)],k=10)
# print(num)
# print(randrange(1,10_000))
# if __name__ == '__main__':
#     pass


""""Ota-onalar darslari

# Hayvon (nomi, yoshi, turi), usullari (displey, uyqu)

Bolalar sinflari,

# Cat +(rang, ovqat), usullar (uyqu mumkin, can_myav)

# It +(rang, ovqat), usullar (uy, sakrab, urish)

# Sigir +(eyish, rang berish), usullari (eyish mumkin, sut berishi mumkin, moa)

# Ot +(tezlik, rang, ovqatlanish), usullar (eyish mumkin, tezlikni olish,
# tezlikni_to'g'rilash, tez_tezlik, rang_olish, ovqat_olish, rang_o'rnatish, ovqat_olish, ovqat_otish)

# Tiger (eyish, rang berish, tezlik) usullari (tezlik_olish, o'ttizda_tezlik_olish, tezlikni_o'rnatish, tezlikni_o'chirish)

# Quyon (eyish, rang berish), usullar (sakrash, yeyish, rang olish)

# Yaguar (tezlik, ovqatlanish, rang) usullari (tezlik_olish, tezlikni sozlash,

# o'chirish_tezligi, qaerda_yashaydi, rangni oling, rangni o'rnating, attrni o'chirishda rangni o'chirish yangi xabarni qaytaradi)"""

class Hayvon:

    def __init__(self,nomi,yoshi,turi):
        self.nomi = nomi
        self.yoshi = yoshi
        self.turi = turi

    def __repr__(self):
        return f"nomi -> {self.nomi} yoshi -> {self.yoshi} turi -> {self.turi}"

    def get_nomi(self):
        return self.nomi

    def get_yoshi(self):
        return self.yoshi

    def get_turi(self):
        return self.turi

    @classmethod
    def set_uyqu(cls, value) -> None:
        cls.uyqu = value
"""
    @classmethod
    def set_nomi(cls,value) -> None:
        cls.nomi = value

    @classmethod
    def set_yoshi(cls,value) -> None:
        cls.yoshi = value

    @classmethod
    def set_turi(cls,value) -> None:
        cls.turi = value
"""


hayvon = Hayvon("qo'y",4,"wdccsc")
print(hayvon)

class Mushuk(Hayvon):
    def __init__(self,nomi,yoshi,turi,rangi,yey_ovqa):
        super().__init__(nomi,yoshi,turi)
        self.rangi = rangi
        self.yey_ovqa = yey_ovqa

    def __repr__(self):
        return f"nomi -> {self.nomi} yoshi -> {self.yoshi} " \
               f"turi -> {self.turi} rangi -> {self.rangi} yeydigan ovqati -> {self.yey_ovqa}"

    def get_rangi(self):
        return self.rangi

    def get_yey_ov(self):
        return self.yey_ovqa

    @classmethod
    def set_mushuk(cls, value,value1) -> None:
        cls.uyqu = value
        cls.can_myav = value1

mushuk = Mushuk("mushuk",3,"yo'q","qora","sichqon😂")
print(mushuk)

class It(Hayvon):
    def __init__(self,nomi,yoshi,turi,rangi,yey_ovqa):
        super().__init__(nomi,yoshi,turi)
        self.rangi = rangi
        self.yey_ovqa = yey_ovqa

    def __repr__(self):
        return f"nomi -> {self.nomi} yoshi -> {self.yoshi} " \
               f"turi -> {self.turi} rangi -> {self.rangi} yeydigan ovqati -> {self.yey_ovqa}"

    def get_rangi(self):
        return self.rangi

    def get_yey_ov(self):
        return self.yey_ovqa

    @classmethod
    def set_it_urush(cls, value) -> None:
        cls.urush = value

it = It("simba",2,"bo'ri bosar","qora","go'sht")
print(it)


class Sigir(Hayvon):
    def __init__(self,nomi,yoshi,turi,rangi,yey_ovqa):
        super().__init__(nomi,yoshi,turi)
        self.rangi = rangi
        self.yey_ovqa = yey_ovqa

    def __repr__(self):
        return f"nomi -> {self.nomi} yoshi -> {self.yoshi} " \
               f"turi -> {self.turi} rangi -> {self.rangi} yeydigan ovqati -> {self.yey_ovqa}"

    def get_rangi(self):
        return self.rangi

    def get_yey_ov(self):
        return self.yey_ovqa

sigir = Sigir("masha",5,"gallaniskiy","qizg'ish","yem")
print(sigir)

class Ot(Hayvon):
    def __init__(self,nomi,yoshi,turi,rangi,yey_ovqa,tezlik):
        super().__init__(nomi,yoshi,turi)
        self.rangi = rangi
        self.yey_ovqa = yey_ovqa
        self.tezlik = tezlik

    def __repr__(self):
        return f"nomi -> {self.nomi} yoshi -> {self.yoshi} " \
               f"turi -> {self.turi} rangi -> {self.rangi}" \
               f" yeydigan ovqati -> {self.yey_ovqa} otni tezligi -> {self.tezlik}"

    def get_rangi(self):
        return self.rangi

    def get_yey_ov(self):
        return self.yey_ovqa

    def get_tezlik(self):
        return self.tezlik


    @classmethod
    def set_ot_eyish_mumkin(cls, value) -> None:
        cls.ot_eyish_mumkin = value

    @classmethod
    def set_ot_tezlik_olishi(cls, value) -> None:
        cls.ot_tezlik_olishi = value

    @classmethod
    def set_ot_tezlikni_togrilash(cls, value) -> None:
        cls.ot_tezlikni_togrilash = value

    @classmethod
    def set_ot_tez_tezlik(cls, value) -> None:
        cls.ot_tez_tezlik = value

    @classmethod
    def set_ot_rang_olish(cls, value) -> None:
        cls.ot_rang_olish = value

    @classmethod
    def set_ot_ovqat_olish(cls, value) -> None:
        cls.ot_ovqat_olish = value

    @classmethod
    def set_ot_rang_ornatish(cls, value) -> None:
        cls.ot_rang_ornatish = value

    @classmethod
    def set_ot_ovqat_otish(cls, value) -> None:
        cls.ot_ovqat_otish = value

ot = Ot("chopar",4,"birornima","qora","yem",40)
print(ot)


class Tiger(Hayvon):
    def __init__(self,nomi,yoshi,turi,rangi,yey_ovqa,tezlik):
        super().__init__(nomi,yoshi,turi)
        self.rangi = rangi
        self.yey_ovqa = yey_ovqa
        self.tezlik = tezlik

    def __repr__(self):
        return f"nomi -> {self.nomi} yoshi -> {self.yoshi} " \
               f"turi -> {self.turi} rangi -> {self.rangi}" \
               f" yeydigan ovqati -> {self.yey_ovqa}  tezligi -> {self.tezlik}"

    def get_rangi(self):
        return self.rangi

    def get_yey_ov(self):
        return self.yey_ovqa

    def get_tezlik(self):
        return self.tezlik

    @classmethod
    def set_tiger_tezlik_olish(cls, value) -> None:
        cls.tiger_tezlik_olish = value

    @classmethod
    def set_tiger_tezlikni_ornatish(cls, value) -> None:
        cls.tiger_tezlikni_ornatish = value

    @classmethod
    def set_tiger_tezlikni_ochirish(cls, value) -> None:
        cls.tiger_tezlikni_ochirish = value


tiger = Tiger("yo'lbars",8,"hjjhf","qora","go'sht",70)
print(tiger)


class Quyon(Hayvon):
    def __init__(self,nomi,yoshi,turi,rangi,yey_ovqa):
        super().__init__(nomi,yoshi,turi)
        self.rangi = rangi
        self.yey_ovqa = yey_ovqa


    def __repr__(self):
        return f"nomi -> {self.nomi} yoshi -> {self.yoshi} " \
               f"turi -> {self.turi} rangi -> {self.rangi}" \
               f" yeydigan ovqati -> {self.yey_ovqa} "

    def get_rangi(self):
        return self.rangi

    def get_yey_ov(self):
        return self.yey_ovqa

    @classmethod
    def set_quyon_sakrash(cls, value) -> None:
        cls.quyon_sakrash = value

    @classmethod
    def set_quyon_yeyish(cls, value) -> None:
        cls.quyon_yeyish = value

    @classmethod
    def set_quyon_rang_olish(cls, value) -> None:
        cls.quyon_rang_olish = value

quyon = Quyon("chj",1,"dddcfc","oq","sabzi")
print(quyon)


class Yaguar(Hayvon):
    def __init__(self,nomi,yoshi,turi,rangi,yey_ovqa,tezlik):
        super().__init__(nomi,yoshi,turi)
        self.rangi = rangi
        self.yey_ovqa = yey_ovqa
        self.tezlik = tezlik


    def __repr__(self):
        return f"nomi -> {self.nomi} yoshi -> {self.yoshi} " \
               f"turi -> {self.turi} rangi -> {self.rangi}" \
               f" yeydigan ovqati -> {self.yey_ovqa} tezligi {self.tezlik}"

    def get_rangi(self):
        return self.rangi

    def get_yey_ov(self):
        return self.yey_ovqa

    def get_yaguar_tezlik(self):
        return self.tezlik

    @classmethod
    def set_yaguar_tezlik_olish(cls, value) -> None:
        cls.yaguar_tezlik_olish = value

    @classmethod
    def set_yaguar_tezlikni_sozlash(cls, value) -> None:
        cls.yaguar_tezlikni_sozlash = value

    @classmethod
    def set_yaguar_qaerda_yashaydi(cls, value) -> None:
        cls.yaguar_qaerda_yashaydi = value

yaguar = Yaguar("yaguar",10,"yirtqich","qora_jigar_rang","go'sht",90)
print(yaguar)
print(isinstance(Mushuk,Hayvon))
print(issubclass())

class MyClass:
    count = 0  # variable de classe

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Utilisation de la méthode de classe
print(MyClass.get_count())  # Affiche : 0

obj1 = MyClass()
print(MyClass.get_count())  # Affiche : 1

obj2 = MyClass()
print(MyClass.get_count())  # Affiche : 2

obj3 = MyClass()
print(MyClass.get_count())  # Affiche : 3













