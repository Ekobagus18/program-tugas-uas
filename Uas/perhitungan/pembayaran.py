def pembayaran():
    print("\n========================================================")
    nama = input("\n\tMasukan Nama = ")
    nim = input("\tMasukan Nim = ")
    semester = input("\tMasukan Semester Saat Ini = ")
    print("\n\t---Pilihan Pembayaran---")
    print("\t1. Pembayaran SPP")
    print("\t2. Pembayaran UTS")
    print("\t3. Pembayaran UAS")
    print("\t4. Pembayaran SPP & UTS")
    print("\t5. Pembayaran SPP & UAS")
    pilih = input("\n\tSilakan Pilih : ")
    if pilih == "1":
        spp()
    elif pilih == "2":
        uts()
    elif pilih == "3":
        uas()
    elif pilih == "4":
        spp_uts()
    elif pilih == "5":
        spp_uas()
    else:
        exit
        tanya()
def spp():
    bulan=int(input("\n\tjumlah bulan yang di bayar = "))
    bulan = float(bulan)
    total = 500000 * bulan
    print("===========================================================")
    print("\ttotal bayar spp Rp.500000 *",bulan," = Rp.",total)
        
def uts():
    matkul_uts =int(input("\n\tjumlah mata kuliah = "))
    matkul_uts =float(matkul_uts)
    byr_uts = 50000 * matkul_uts
    print("===========================================================")
    print("\ttotal bayar uas Rp.50000 *",matkul_uts," = Rp.",byr_uts)

def uas():
    matkul_uas =int(input("\n\tjumlah mata kuliah = "))
    matkul_uas =float(matkul_uas)
    byr_uas = 50000 * matkul_uas
    print("===========================================================")
    print("\ttotal bayar uas Rp.50000 *",matkul_uas," = Rp.",byr_uas)

def spp_uas():
    bulan=int(input("\n\tjumlah bulan yang di bayar = "))
    matkul =int(input("\tjumlah mata kuliah = "))
    matkul =float(matkul)
    bulan = float(bulan)
    total_spp = 500000 * bulan
    byr_uas = 50000 * matkul
    total = total_spp + byr_uas + 5000    
    print("\n\ttotal bayar spp Rp.500000 * ",bulan," = Rp.",total_spp)
    print("\ttotal bayar uas Rp.50000 * ",matkul," = Rp.",byr_uas)
    print("\tbiaya tambahan server sebesar Rp.5000")
    print("====================================")
    print("\ttotal yang harus di bayar Rp.",total)

def spp_uts():
    bulan=int(input("\n\tjumlah bulan yang di bayar = "))
    matkul =int(input("\tjumlah mata kuliah = "))
    matkul =float(matkul)
    bulan = float(bulan)
    total_spp = 500000 * bulan
    byr_uts = 50000*matkul
    total = total_spp + byr_uts + 5000
    print("\n\ttotal bayar spp Rp.500000 * ",matkul," = Rp.",byr_uts)
    print("\ttotal bayar uts Rp.50000 * ",bulan," = Rp.",total_spp)
    print("\tbiaya tambahan server sebesar Rp.5000")
    print("=============================================")
    print("\ttotal yang harus di bayar" ,total)

