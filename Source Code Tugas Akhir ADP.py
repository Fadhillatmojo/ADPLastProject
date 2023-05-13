# global variabel
arraySatuanPanjang = ["mm","cm","dm", "m", "dam", "hm", "km"]
arraySatuanMassa = ["mg","cg","dg", "g", "dag", "hg", "kg"]
parameterPertama = 0
parameterKedua = 0
masukan = 0
konverter = ""

# fungsi pertanyaan apakah ingin mengulang penggunaan? 
def gunakanLagi():
    print("\n" + '--- Apakah ingin menggunakan lagi? ---')
    print('1 untuk ya, 2 untuk tidak'+"\n")
    angka = int(input("Masukkan angka: "))
    if angka == 1:
        print("\n"+'='*60+"\n")
        print("\t"*3+"Go Convert")
        print("\n"+'='*60)
        fungsiPilih()
    elif angka == 2:
        print("")
        print('='*60)
        print("\t"+'--- Terima Kasih Telah Menggunakan ---')
        print('='*60)
    else:
        print("\n"+'='*60)
        print('!!! Masukkan angka yang benar !!!')
        print('='*60)
        gunakanLagi()
      
# fungsi konversi
def konversiPanjang():
    global masukan
    print('='*60)
    print("\n"+"--- Hasil ---")
    if parameterPertama < parameterKedua:
        count = 0
        for i in range(parameterPertama,parameterKedua):
            count += 1
        
        print(masukan, arraySatuanPanjang[parameterPertama-1],"=", "{:.3f}".format(masukan/(10**(count))), arraySatuanPanjang[parameterKedua-1])
    else:
        count = 0
        for i in range(parameterKedua,parameterPertama):
            count += 1
        print(masukan, arraySatuanPanjang[parameterPertama-1],"=", "{:.1f}".format(masukan*(10**(count))), arraySatuanPanjang[parameterKedua-1])
    print("\n"+'='*60)
    gunakanLagi()

def konversiMassa():
    global masukan
    print('='*60)
    print("\n"+"--- Hasil ---")
    if parameterPertama < parameterKedua:
        count = 0
        for i in range(parameterPertama,parameterKedua):
            count += 1
        print(masukan, arraySatuanMassa[parameterPertama-1],"=", "{:.3f}".format(masukan/(10**(count))), arraySatuanMassa[parameterKedua-1])
    else:
        count = 0
        for i in range(parameterKedua,parameterPertama):
            count += 1
        print(masukan, arraySatuanMassa[parameterPertama-1],"=", "{:.1f}".format(masukan*(10**(count))), arraySatuanMassa[parameterKedua-1])
    print("\n"+'='*60)
    gunakanLagi()
    
# fungsi masukan angka
def fungsiMasukanAngka():
    global masukan
    global konverter
    # global parameterPertama
    # global parameterKedua
    print("\n"+'='*60)
    print("")
    x = float(input("Angka yang ingin dikonversi (boleh angka real): "))
    masukan = x
    print("")
    if konverter == "panjang":
        konversiPanjang()
    else:
        konversiMassa()
        
# fungsi satuan panjang
def fungsiSatuanPanjang2():
    global parameterKedua
    print("\n"+"Satuan yang diinginkan (Ketikkan hanya angka): ")
    print("1. mm" + "\n" + "2. cm" +"\n"+ "3. dm" +"\n"+ "4. m" +"\n"+ "5. dam" +"\n"+ "6. hm" + "\n" + "7. km"+"\n")
    angka2 = int(input("Masukkan Angka: "))
    parameterKedua = angka2
    # percabangan apakah angkanya antara 1 dan 7
    if parameterKedua <= 7 and parameterKedua >= 1:
        fungsiMasukanAngka()
    else:
        print("\n"+'='*60)
        print("!!! Masukkan angka yang benar !!!")
        print('='*60)
        fungsiSatuanPanjang2()

def fungsiSatuanPanjang1():
    global parameterPertama
    print("\n"+"Satuan Awal (Ketikkan hanya angka): ")
    print("1. mm" + "\n" + "2. cm" +"\n"+ "3. dm" +"\n"+ "4. m" +"\n"+ "5. dam" +"\n"+ "6. hm" + "\n" + "7. km"+"\n")
    angka1 = int(input("Masukkan Angka: "))
    parameterPertama = angka1
    # percabangan apakah angkanya antara 1 dan 7
    if parameterPertama <= 7 and parameterPertama >= 1:
        fungsiSatuanPanjang2()
    else:
        print("\n"+'='*60)
        print("!!! Masukkan angka yang benar !!!")
        print('='*60)
        fungsiSatuanPanjang1()
        
# fungsi satuan massa
def fungsiSatuanMassa2():
    global parameterKedua
    print("\n"+"Satuan yang diinginkan (Ketikkan hanya angka): ")
    print("1. mg" + "\n" + "2. cg" +"\n"+ "3. dg" +"\n"+ "4. g" +"\n"+ "5. dag" +"\n"+ "6. hg" + "\n" + "7. kg"+"\n")
    angka2 = int(input("Masukkan Angka: "))
    parameterKedua = angka2
    # percabangan apakah angkanya antara 1 dan 7
    if parameterKedua <= 7 and parameterKedua >= 1:
        fungsiMasukanAngka()
    else:
        print("\n"+'='*60)
        print("!!! Masukkan angka yang benar !!!")
        print('='*60)
        fungsiSatuanMassa2()

def fungsiSatuanMassa1():
    global parameterPertama
    print("\n"+"Satuan Awal (Ketikkan hanya angka): ")
    print("1. mg" + "\n" + "2. cg" +"\n"+ "3. dg" +"\n"+ "4. g" +"\n"+ "5. dag" +"\n"+ "6. hg" + "\n" + "7. kg"+"\n")
    angka1 = int(input("Masukkan Angka: "))
    parameterPertama = angka1
    # percabangan apakah angkanya antara 1 dan 7
    if parameterPertama <= 7 and parameterPertama >= 1:
        fungsiSatuanMassa2()
    else:
        print("\n"+'='*60)
        print("!!! Masukkan angka yang benar !!!")
        print('='*60)
        fungsiSatuanMassa1()
    
# fungsi memilih panjang/ massa
def fungsiPilih():
    global konverter
    print("\n"+"-- Silakan memilih fungsi panjang/massa --" + "\n" + "(Ketikkan hanya angka)"+"\n"+"1.Panjang"+"\n"+"2.Massa"+"\n")
    x = int(input("Masukkan Angka: "))
    print("\n"+'='*60)
    if x == 1:
        konverter = "panjang"
        fungsiSatuanPanjang1()
    elif x == 2:
        konverter = "massa"
        fungsiSatuanMassa1()
    else:
        print("!!! Masukkan Angka yang benar !!!")
        print('='*60)
        fungsiPilih()
        
# mulai program
print('='*60)
print("\t"*3+"Go Convert"+"\n")
print("Mengkonversi semua skala panjang dan massa (Mili - Kilo)")
print('='*60)

fungsiPilih()












