import time
print("""Market Ödevi Uygulaması

1. Gerekenleri Yazmak

2. Gerekenleri Gormek

3. Gerekenleri Değiştirmek

4. Gerekenleri Silmek
""")


while True:
    dokuman = input("Islem Numarası?: ")
    if dokuman == "1":
        isim = input("Isminiz?: ")
        adet = int(input("Kaç adet satın aldınız?: "))
        fiyat = int(input("Adet Fiyatı: "))
        toplam = adet*fiyat
        with open("dokuman.txt","a",encoding="utf-8") as dosya:
            dosya.write("Isim: {} , Adet:{} , Fiyat:{} , Toplam:{}\n".format(isim,adet,fiyat,toplam))
            print("Belge'ye Not Edildi.\n")
    elif dokuman == "2":
        with open("dokuman.txt","r",encoding="utf-8") as dosya:
            print("Belge İçindeki Dökümanlar Gösteriliyor.\n")
            time.sleep(1)
            okuma = dosya.read()
            print(okuma)
        
    elif dokuman == "3":
        with open("dokuman.txt","r+",encoding="utf-8") as dosya:
            print("Belgede ki veriler hazırlanıyor.\n")
            time.sleep(1)
            soru = int(input("Değiştirmek İstediğiniz Satır Numarası?(0'dan itibaren): "))
            liste = dosya.readlines()
            if soru >= len(liste):
                print("Hatalı Satır, Lütfen tekrar deneyiniz.(0'dan başlıyor dikkat ediniz.)")
            elif soru <= len(liste):
                isim = input("Isminiz: ")
                adet = int(input("Kaç adet satın aldınız?: "))
                fiyat = int(input("Adet Fiyatı: "))
                toplam = adet*fiyat
                liste[soru] = ("Isim: {} , Adet:{} , Fiyat:{} , Toplam:{}\n".format(isim,adet,fiyat,toplam))
                with open("dokuman.txt", "w") as dosya:
                    dosya.write("".join(liste))

            
    elif dokuman == "4":
        with open("dokuman.txt","r+",encoding="utf-8") as dosya:
            print("Belgede ki veriler hazırlanıyor.\n")
            time.sleep(1)
            soru = int(input("Silmek İstediğiniz Satır Numarası?(0'dan itibaren): "))
            liste = dosya.readlines()
            if soru >= len(liste):
                print("Hatalı Satır, Lütfen tekrar deneyiniz.(0'dan başlıyor dikkat ediniz.)")
            elif soru <= len(liste):
                liste[soru] = ("")
                with open("dokuman.txt", "w") as dosya:
                    dosya.write("".join(liste))
    
    elif dokuman == "q":
        print("Programdan çıkılıyor...")
        input()
        break
        
    else:
        print("Yanlış değeri girdiniz.")