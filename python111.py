#  print(yazdir demek , isimlerde tirnak kullanilir)#

#  \t (bosluk birakir yazdirmak istediniz seyler arasinda)#

#  \n (alt satirda baslatir yazdirmak istediniz seyler arasinda)#

#  .format (degiskenlere s�sl� parantez i�indeki yerler siralamasiyla bastan sona kendini siralar ve deger verir. #

#  s�sl� parantez i�indekilere atadigimiz degiskenlerle eslestirir) #

#  print("adim {adim} ,yasim {yasim} " .format(adim="ogi" ,yasim= 19))#

#   sayi = 10 print(sayi) #

#sayi=10
#sayi=sayi+1
#print(sayi)

#SyntaxError (Yazimsal hata demek) degiskeni yazarken iki kelimeli degiskenlerde bosluk olmicak python boslugu tanimaz

#Input (kullanicidan bir sayi almak i�in kullanilir)

#Print (kullanirken ��er tirnakli kullanirsaniz arka arkaya yazabilirsiniz alt satirda yazma kolayligi saglar)





print("Merhaba Efendim")

Birinci_Sayiyi = int(input("Birinci Sayiyi Giriniz..:"))

Ikinci_Sayiyi = int(input("Ikinci Sayiyi Giriniz..:"))

print("""
 Toplama Yapmak I�in '+'
 �ikarma Yapmak I�in '-'
 �arpma Yapmak I�in '*'
 B�lme Yapmak I�in '/'
 """)

Yapilmak_Istenen_Islem = input("Yapmak Istediniz Islemin Isaretini Giriniz")

if(Yapilmak_Istenen_Islem == '+'):
    print("Sonuc :",Birinci_Sayiyi + Ikinci_Sayiyi)

elif(Yapilmak_Istenen_Islem == '-'):
    print("Sonuc :",Birinci_Sayiyi - Ikinci_Sayiyi)

if (Yapilmak_Istenen_Islem == '*'):
    print("Sonuc :",Birinci_Sayiyi * Ikinci_Sayiyi)

elif (Yapilmak_Istenen_Islem == '/'):
    print("Sonuc :",Birinci_Sayiyi / Ikinci_Sayiyi)
