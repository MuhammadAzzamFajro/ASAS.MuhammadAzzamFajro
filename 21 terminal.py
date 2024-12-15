def hitung_biaya_parkir(waktu_parkir):
    # Tarif untuk 2 jam pertama
    tarif_awal = 3000
    # Tarif per jam tambahan setelah 2 jam
    tarif_tambahan_per_jam = 1500
    # Biaya tambahan jika parkir lebih dari 24 jam
    tambahan_lebih_24_jam = 10000
    
    # Mengecek apakah waktu parkir kurang dari 0
    if waktu_parkir < 0:
        return "maaf hanya melayani diatas 1 jam"
    
    # Mengecek apakah waktu parkir lebih dari 2 jam
    if waktu_parkir <= 2:
        # Jika parkir kurang dari 2 jam, biaya tetap 3000
        biaya = tarif_awal
    elif waktu_parkir <= 24:
        # Jika parkir lebih dari 2 jam tetapi kurang dari 24 jam
        biaya = tarif_awal + (waktu_parkir - 2) * tarif_tambahan_per_jam #Jika lebih dari 2 jam, maka 1500 per jam 
    else:
        # Jika parkir lebih dari 24 jam
        biaya = tarif_awal + (waktu_parkir - 2) * tarif_tambahan_per_jam + tambahan_lebih_24_jam # Jika lebih dari 24 jam maka ditambah Rp 10.000
    
    return biaya
        

# Input waktu parkir
waktu_parkir = float(input("Masukkan waktu parkir dalam jam: "))

# Menghitung biaya parkir
biaya = hitung_biaya_parkir(waktu_parkir)

# Menampilkan hasil
if isinstance(biaya, str):
    print(biaya)  # Menampilkan pesan kesalahan jika waktu tidak valid
else:
    print(f"Biaya parkir untuk {waktu_parkir} jam adalah Rp {biaya}")
