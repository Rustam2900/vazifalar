class Region:
    def __init__(self,name):
        self.name = name


    def __repr__(self):
        return f"{self.name} "


class Marketi:
    def __init__(self,title,id):
        self.title = title
        self.id = id

    def __repr__(self):
        return f" nomi -> {self.title}  id -> {self.id}"
marketi = Marketi("Shvr",4)
class Modeli:
    def __init__(self,title,id):
        self.title = title
        self.id = id

    def __repr__(self):
        return f" rangi -> {self.title} id -> {self.id}"
modeli = Modeli("qora",7)
class Car:
    def __init__(self,region,name,narxi,market,modeli,yil):
        self.region = region
        self.name = name
        self.narxi = narxi
        self.market = market
        self.modeli = modeli
        self.yil = yil
    def __repr__(self):
        return f" qayrdan -> {self.region}  nomi -> {self.name} " \
               f"narxi -> {self.narxi} {self.market} {self.modeli}" \
               f"chiqgan yili -> {self.yil}"


    def narx_(self,narx):
        if self.narxi -narx <= 1300:
            return f"sotiladi"
        else:
            return f"kechirasiz sota olmaymiz"
region = Region("Toshkent")
car = Car(region,"Coblt",15000,marketi,modeli,2019)
region = Region("Samarqand")
car1 = Car(region,"Laseti",12000,marketi,modeli,2020)
print(car)
print(car1.narx_(14000))


