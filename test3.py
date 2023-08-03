class yazilimci():

    def __init__(self,isim,soyisim,numarasi,maas,deneyim_yili,diller):

        self.isim=isim
        self.soyisim=soyisim
        self.numarasi=numarasi
        self.maas=maas
        self.deneyim_yili=deneyim_yili
        self.diller=diller
        
    def bilgilerigöster(self):
        print(""" Yazilimci bilgileri...
        isim : {}
        soyisim : {}
        numarasi : {}
        maas : {}
        deneyim : {}
        diller : {}

        """.format(self.isim,self.soyisim,self.numarasi,self.maas,self.deneyim_yili,self.diller))

yazili = yazilimci("oguzhan","yucedag",00000,1000000,4,"java, python, C, C#, C+")
yazili.bilgilerigöster()        