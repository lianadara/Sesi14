def konversi_mata_uang(jumlah, nilai_tukar):    
    return jumlah * nilai_tukar
nilai_tukar_usd_ke_idr = 15000

jumlah_usd = float(input("Masukkan jumlah dlm USD: "))
jumlah_idr = konversi_mata_uang(jumlah_usd, nilai_tukar_usd_ke_idr)
print(f"{jumlah_usd} USD setara dengan {jumlah_idr} IDR.")