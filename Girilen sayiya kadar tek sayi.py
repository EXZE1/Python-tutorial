s = input('Sayi Girin.....  :\n')
try:
    if int(s)>=0:
        
        for i in range(int(s)):
            if i % 2 == 1:
                print(i)       
except:
        print("Yanlis Karakter ......:")