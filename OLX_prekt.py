# OOP_bo'yicha birinchi prektimni ko'taramiz bu prekt OLX ni yozmoqchi bo'lamiz nasb bo'lsa tugatamiz "👍👍👍👍"

class OLX:
    def __init__(self,bolalar_dunyosi,kochmas_mulk,transport,elektr_jixozlar):
        self.bolalar_dunyosi = bolalar_dunyosi
        self.kochmas_mulk = kochmas_mulk
        self.transport = transport
        self.elektr_jixozlar = elektr_jixozlar

    def __repr__(self):
        return f"{self.bolalar_dunyosi} {self.kochmas_mulk} " \
               f"{self.transport}   {self.elektr_jixozlar}"

class Bolalar_dunyosi:
    def __init__(self,bolalar_kiyimi,bolalar_oyoq_kiyim,oyinchoqlar):
        self.bolalar_kiyimi = bolalar_kiyimi
        self.bolalar_oyoq_kiyim = bolalar_oyoq_kiyim
        self.oyinchoqlar = oyinchoqlar

    def __repr__(self):
        return f"{self.bolalar_kiyimi} {self.bolalar_oyoq_kiyim} {self.oyinchoqlar}"

class Bolalar_kiyimi:
    def __init__(self,nomi,qayrda_ishlab,narxi,magazin_nomi):
        self.nomi = nomi
        self.qayrda_ishlab = qayrda_ishlab
        self.narxi = narxi
        self.magazin_nomi = magazin_nomi

    def __repr__(self):
        return f" kiyim nomi -> {self.nomi}  kiyim qayrda ishlab chiqarilgani -> {self.qayrda_ishlab} " \
               f"kiyim narxi -> {self.narxi}  ma" \
               f"magazin nomi -> {self.magazin_nomi}"

kiyim = Bolalar_kiyimi("fidbolka_GUCCI:","Turkiya:",200000,"Vip_brent")
#print(kiyim)

class Bolalar_oyoq_kiyim:
    def __init__(self, nomi, qayrda_ishlab, narxi, magazin_nomi):
        self.nomi = nomi
        self.qayrda_ishlab = qayrda_ishlab
        self.narxi = narxi
        self.magazin_nomi = magazin_nomi

    def __repr__(self):
        return f" oyoq kiyim nomi -> {self.nomi}  oyoq kiyim qayrda ishlab chiqarilgani -> {self.qayrda_ishlab} " \
               f"oyoq kiyim narxi -> {self.narxi}  ma" \
               f"magazin nomi -> {self.magazin_nomi}"

oyoq_kiyim = Bolalar_oyoq_kiyim("GUCCI:","Turkiya:",400000,"Vip_brent")
#print(oyoq_kiyim)

class Oyinchoqlar:
    def __init__(self, nomi, qayrda_ishlab, narxi, magazin_nomi):
        self.nomi = nomi
        self.qayrda_ishlab = qayrda_ishlab
        self.narxi = narxi
        self.magazin_nomi = magazin_nomi

    def __repr__(self):
        return f" o'yinchoq nomi -> {self.nomi}  o'yinchoq qayrda ishlab chiqarilgani -> {self.qayrda_ishlab} " \
               f"o'yinchoq  narxi -> {self.narxi}  ma" \
               f"magazin   nomi -> {self.magazin_nomi}"

oyinchoq = Oyinchoqlar("Qo'g'irchoq","UZB",200000,"detiski_magazin")
#print(oyinchoq)

#bolalar_dunyosi = Bolalar_dunyosi("fudbolkalar","tapichka","qo'g'irchoq")
#print(bolalar_dunyosi)

class Kochmas_mulk:
    def __init__(self,sutkali_ijara,kvartera):
        self.sutkali_ijara = sutkali_ijara
        self.kvartera = kvartera

    def __repr__(self):
        return f"{self.sutkali_ijara} {self.kvartera}"

class Sutkali_ijara:
    def __init__(self,qayrdaligi,narxi):
        self.qayrdaligi = qayrdaligi
        self.narxi = narxi

    def __repr__(self):
        return f"qayrdaligi -> {self.qayrdaligi} narxi -> {self.narxi}"

sutkali = Sutkali_ijara("Chilonzor_Qatortol",300000)
#print(sutkali)

class Kvartera:
    def __init__(self,qayrdaligi,narxi,xonalar_soni,nechikishi_turushi,mak_narx):
        self.qayrdaligi = qayrdaligi
        self.narxi = narxi
        self.xonalar_soni = xonalar_soni
        self.nechikishi_turushi = nechikishi_turushi
        self.mak_narx = mak_narx

    def __repr__(self):
        return f"qayrdaligi -> {self.qayrdaligi}: narxi -> {self.narxi}:" \
               f" xonalar soni -> {self.xonalar_soni}: nechi kishi turushiga ruxsad -> {self.nechikishi_turushi}: " \
               f"makler narxi -> {self.mak_narx}"

kvartera = Kvartera("Yunisabot_Bodomzor",3_500_000,2,5,1_500_000)
#print(kvartera)

class Transport:
    def __init__(self,avtobuslar,yangi_moshinalar,yuk_moshinalar):
        self.avtobuslar = avtobuslar
        self.yangi_moshinalar = yangi_moshinalar
        self.yuk_moshinalar = yuk_moshinalar

    def __repr__(self):
        return f"{self.avtobuslar} {self.yangi_moshinalar} {self.yuk_moshinalar}"

# transport = Transport(115,"BMW","Kamaz")
# print(transport)

class Elektr_jixozlar:
    def __init__(self,telfonlar,kompterlar,uy_texnikalari):
        self.telfonlar = telfonlar
        self.kompterlar = kompterlar
        self.uy_texnikalari = uy_texnikalari

    def __repr__(self):
        return f"{self.telfonlar} {self.kompterlar} {self.uy_texnikalari}"

bolalar = Bolalar_dunyosi(kiyim,oyoq_kiyim,oyinchoq)
print(bolalar)

kochmas_mulklar = Kochmas_mulk(sutkali,kvartera)
print(kochmas_mulklar)
""" Hali juda ko'p qo'shimchalar qo'shish kerak """
