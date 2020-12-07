nama= input(" Silahkan Masukkan Nama Anda Untuk Melanjutkan Pembelian  :    ")
print("\n\t\tSelamat datang Di toko Kami, {} ".format(str.capitalize(nama)))
print("\t\t++===================================================++")
print("\t\t||                                                   ||")
print("\t\t||               PROGRAM BELANJA BUSANA              ||")
print("\t\t||                                                   ||")
print("\t\t||               DIBUAT OLEH KELOMPOK 5              ||")
print("\t\t||                                                   ||")
print("\t\t++===================================================++")

eror = True
while(eror):
    jenis_kelamin = (input)("\n\nSilahkan Pilih Jenis Kelamin Anda, pria atau wanita ? : ")
    if (str.upper(jenis_kelamin) == "PRIA"):
        eror = False
        print("\n\nBaik, Selamat Datang Bapak",nama)
    elif (str.upper(jenis_kelamin) == "WANITA"):
        eror = False
        print("\n\nBaik, Selamat Datang Nyonya",nama)
    else:
        print("\n\nSilahkan Masukkan Jenis Kelamin Anda Dengan Benar! pria / wanita ? : ")

s = int (50000)
m = int (55000)
l = int (60000)
xl = int (65000)

eror=True
while(eror):
    jenis_baju = str(input("Silahkan Pilih Jenis Baju Yang Anda Inginkan ? ( lengan Panjang / lengan pendek) : "))
    if (str.upper(jenis_baju) == "LENGAN PANJANG" or str.upper(jenis_baju) == "LENGAN PENDEK" ):
        eror= False
        print("\nAnda Memilih Jenis Baju >>>>>",jenis_baju)
    else:
        print("Silahkan Pilih Jenis Baju Yang Benar ( lengan panjang / lengan pendek ? : ")

eror = True
while(eror):
    print("\t\t\t\tKami sedang mengadakan promo!")
    print("\t\t================================================================")
    print("\t\tJika anda membeli 3 Sampai 5 Baju kami akan memberi   diskon 10%")
    print("\t\tJika anda membeli 6 Baju atau lebih kami akan memberi diskon 15%")
    print("\t\t================================================================")
    ukuran_baju = str(input("\nPilihlah Ukuran Baju Anda  s, m, l, xl ? = ") )
    if (str.upper(ukuran_baju) == "S" or str.upper(ukuran_baju) == "M" or str.upper(ukuran_baju) == "L" or str.upper(ukuran_baju) == "XL" ):
        eror = False
        print("\nAnda Memilih Ukuran Baju >>>>> ",ukuran_baju)
        
    else:
        print("nUkuran Yang Anda Pilih Salah! (Silahkan Pilih Kembali Antara ukuran S , M , L, XL")

eror=True
while(eror):
    warna = str(input("\nPilihlah Warna baju ( hitam , putih , biru , merah , hijau) : "))
    if (str.upper(warna) == "HITAM" or str.upper(warna) == "PUTIH" or str.upper(warna) == "BIRU" or str.upper(warna) == "MERAH" or str.upper(warna) == "HIJAU"):
        eror=False
        print("\nAnda Memilih Baju Warna >>>>> ",warna)

    else:
        print("Silahkan Masukkan Warna Yang Benar ( hitam , putih , biru , merah , hijau ? : ")



if ukuran_baju == "s":
    print ("\nHarga Baju Ukuran S adalah : ", s)
    eror=True
    while(eror):
        try:
            jumlah_baju = int(input("\nSilahkan Masukkan Jumlah Baju Yang Anda Ingin Beli : "))
            if jumlah_baju <3 :
                b = jumlah_baju * 50000
                print("\nAnda memesan {0} baju dengan ukuran S" .format(jumlah_baju))
                print("\nBiaya yang anda bayar Rp.{0} tanpa diskon." .format(b))
                print("\nRincian Harga : {0} baju x Rp.50000 = Rp.{1}." .format(jumlah_baju, b))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
            elif jumlah_baju >=3 and jumlah_baju <=5 :
                b = jumlah_baju * 50000
                c = b * 10 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran S" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 10%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.50000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
            elif jumlah_baju >5 :
                b = jumlah_baju * 50000
                c = b * 15 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran S" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 15%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.50000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
        except ValueError:
            print("\nSilahkan Masukkan Jumlah Yang Benar ( Hanya Angka ) : ")
elif ukuran_baju == "m":
    print ("\nHarga Baju Ukuran M adalah : ", m)
    eror=True
    while(eror):
        try:
            jumlah_baju = int(input("\nSilahkan Masukkan Jumlah Baju Yang Anda Ingin Beli = "))
            if jumlah_baju <3 :
                b = jumlah_baju * 55000
                print("\nAnda memesan {0} baju dengan ukuran M" .format(jumlah_baju))
                print("\nBiaya yang anda bayar Rp.{0} tanpa diskon." .format(b))
                print("\n Rincian Harga : {0} baju x Rp.55000 = Rp.{1}." .format(jumlah_baju, b))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
            elif jumlah_baju >=3 and jumlah_baju <=5 :
                b = jumlah_baju * 55000
                c = b * 10 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran M" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 10%" .format(a))
                print("\n{0} baju x Rp.55000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
            elif jumlah_baju >5 :
                b = jumlah_baju * 55000
                c = b * 15 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran M" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 15%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.55000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
        except ValueError:
            Print("\nMasukkan Jumlah Yang Benar ( Hanya Angka ) : ")

elif ukuran_baju == "l":
    print ("\nHarga Baju Ukuran L adalah : ", l)
    eror=True
    while(eror):
        try:
            jumlah_baju = int(input("\nSilahkan Masukkan Jumlah Baju Yang Anda Ingin Beli = "))
            if jumlah_baju <3 :
                b = jumlah_baju * 60000
                print("\nAnda memesan {0} baju dengan ukuran L" .format(jumlah_baju))
                print("\nBiaya yang anda bayar Rp.{0} tanpa diskon." .format(b))
                print("\nRincian Harga : {0} baju x Rp.60000 = Rp.{1}." .format(jumlah_baju, b))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
            elif jumlah_baju >=3 and jumlah_baju <=5 :
                b = jumlah_baju * 60000
                c = b * 10 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran L" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 10%" .format(a))
                print("\n{0} baju x Rp.60000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
            elif jumlah_baju >5 :
                b = jumlah_baju * 60000
                c = b * 15 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran L" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 15%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.60000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
        except ValueError:
            print("\nSilahkan Masukkan Jumlah Yang Benar ( Hanya Angka ) : ")
    
elif ukuran_baju == "xl":
    print ("\nHarga Baju Ukuran XL adalah : ", xl)
    eror=True
    while(eror):
        try:
            jumlah_baju = int(input("\nSilahkan Masukkan Jumlah Baju Yang Anda Ingin Beli = "))
            if jumlah_baju <3 :
                b = jumlah_baju * 65000
                print("\nAnda memesan {0} baju dengan ukuran XL" .format(jumlah_baju))
                print("\nBiaya yang anda bayar Rp.{0} tanpa diskon." .format(b))
                print("\nRincian Harga : {0} baju x Rp.65000 = Rp.{1}." .format(jumlah_baju, b))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
            elif jumlah_baju >=3 and jumlah_baju <=5 :
                b = jumlah_baju * 65000
                c = b * 10 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran XL" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 10%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.65000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
            elif jumlah_baju >5 :
                b = jumlah_baju * 65000
                c = b * 15 / 100
                a = b - c
                print("\nAnda memesan {0} baju dengan ukuran XL" .format(jumlah_baju))
                print("\nDiskon yang anda dapatkan adalah Rp.{0}." .format(c))
                print("\nBiaya yang anda bayar Rp.{0} dengan diskon 15%" .format(a))
                print("\nRincian Harga : {0} baju x Rp.65000 = {1} - {2} = Rp.{3}." .format(jumlah_baju, b, c, a))
                print("\nTerimakasih Telah Berbelanja Di Toko Kami,",nama)
                eror=False
        except ValueError:
            ("\nSilahkan Masukkan Jumlah Yang Benar ( Hanya Angka ) : ")
