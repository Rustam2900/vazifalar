from uuid import  uuid4
class Avto:
    __num_avto = 0
    def __init__(self,make,model,rangi,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rangi = rangi
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
    # def __str__(self):
    #     return f"{self.make} {self.model}"

    def __repr__(self): # __str__ metid bilan birxil ishlaydi vazifasi str qilib qaytaradi buni metid chaqirmasa id manzilini qaytarib turadi
        return f"{self.make} {self.model}"


    def __eq__(self,y): # bu metid teng likga tekshirib beradi
        return self.narx==y.narx


    def __lt__(self, y): # bu metid esa ikkita class ichidaki obyektlarni kichik yo kattalikga tekshiruvchi metid
        return self.narx<y.narx


    def __le__(self, y):# kattoyo tengga tekshiradi
        return self.narx<=y.narx


class AftoSalon:
    def __init__(self,name): # bu metid siz esa manimcha class yozib bo'midi eng assoiy metid bo'lishi kerak manimcha
        self.name = name
        self.avtolar = []

    def __repr__(self): # bu etidni endi bilasiz tepada yozilgan
        return f"{self.name} avtosaloni"


    def __getitem__(self, index): # bu metid orqali index bilan chaqirsa bo'ladi
        return self.avtolar[index]


    def __setitem__(self, index, qiymat): # bu metid esa indek orqali qiymatini o'zgartirishga kerak bo'ladi
        self.avtolar[index]=qiymat


    def __call__(self,*qiymat): # bu metid vazifasi salon1() print qiganda mana shunday chaqirsa ham chiqarib beradi
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]


    def __add__(self, y): # bu metid ikkita class ichidaki obyektlarni qo'shishga yordam beradi
        if isinstance(y,AftoSalon):
            yangi_salon = AftoSalon(f"{self.name} {y.name}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon
        elif isinstance(y,Avto):
            self.add_avto(y)


    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting!")

salon1 = AftoSalon("MaxAvto")
salon2 = AftoSalon("Avto lider")
"""
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self,km):
        if km>=0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'maydi")
"""
avto1 = Avto("BMW","BMW","Qora",2022,50000,300)
avto2 = Avto("lam","lamban","Qora",2021,50000,180)
avto3 = Avto("lasetti","uzb","oq",2019,15000,270)
avto4 = Avto("coblt","uzb","Qora",2020,12000,500)
avto5 = Avto("jentra","uzb","Qora",2023,18000,400)
avto6 = Avto("spark","uzb","oq",2021,9000,600)
salon1.add_avto(avto1,avto2,avto3,avto4)
salon2(avto4,avto5,avto6)
#avto3 = Avto("BMW","BMW","Qora",2022,50000,300)
# print(Avto.get_num_avto())
# print(avto1.get_num_avto())
# print(avto1)
# print(repr(avto1))
# print(avto1<avto2)
# print(avto1==avto2)
# print(avto1>avto2)
# print(isinstance(avto2,AftoSalon))
# print(isinstance(1.1,int))
#print(salon1)
salon1[0] = Avto("BMW","x7","oq",2018,65000)
# print(salon1[:])
# print(salon1[0])
salon1(avto5,avto6)
# print(salon1())
print(salon1())
print(salon2())
salon3 = salon1 + salon2
print(salon3.name)
print(salon3())
