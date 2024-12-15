def hitung_biaya_parkir(jenis_kendaraan, waktu_parkir):
    # Memastikan apakah waktu parkir tidak negatif
    if waktu_parkir < 0:
        return None  # Mengembalikan None jika waktu parkir negatif

    # Memproses perhitungan biaya berdasarkan jenis kendaraan
    if jenis_kendaraan.lower() == "mobil":  # Jika jenis kendaraan adalah mobil
        if waktu_parkir <= 2:  # Jika waktu parkir kurang dari atau sama dengan 2 jam
            biaya = 3000  # Biaya dua jam pertama adalah 3000
        elif waktu_parkir <= 24:  # Jika waktu parkir antara 3jam hingga 24 jam
            biaya = 3000 + (waktu_parkir - 2) * 1500  # Jika lebih dari dua jam,maka Rp1500 per jam
        else:  # Jika waktu parkir lebih dari 24 jam
            biaya = 3000 + (waktu_parkir - 2) *1500 + 10000  # Tambahan biaya 10000 setelah 24 jam
    elif jenis_kendaraan.lower() == "motor":  # Jika jenis kendaraan adalah motor
        if waktu_parkir <= 2:  # Jika waktu parkir kurang dari atau sama dengan 2 jam
            biaya = 3000  # Biaya dua jam pertama adalah 3000
        elif waktu_parkir <= 24:  # Jika waktu parkir antara 3 hingga 24 jam
            biaya = 3000 + (waktu_parkir - 2) * 1000  # Jika lebih dari dua jam,maka Rp1000 per jam
        else:  # Jika waktu parkir lebih dari 24 jam
            biaya = 3000 + (waktu_parkir - 2) *1000 + 10000  # Tambahan biaya 10000 setelah 24 jam
    else:  # Jika jenis kendaraan tidak valid
        return None  # Mengembalikan None untuk jenis kendaraan tidak dikenali

    # Mengembalikan hasil biaya parkir
    return biaya

# Input dari pengguna
jenis_kendaraan = input("Masukkan jenis kendaraan (Mobil, Motor): ")  # Meminta input jenis kendaraan
waktu_parkir = float(input("Masukkan waktu parkir (dalam jam): "))  # Meminta input durasi waktu parkir

# Hitung biaya
biaya = hitung_biaya_parkir(jenis_kendaraan, waktu_parkir)  # Memanggil fungsi untuk menghitung biaya parkir

# Output biaya
if biaya is None:  # Jika hasil perhitungan tidak valid maka None
    print("Waktu parkir tidak valid atau jenis kendaraan tidak valid. Tidak bisa melayani.")
else:  # Jika hasil perhitungan valid
    print(f"Biaya parkir untuk {jenis_kendaraan} selama {waktu_parkir} jam adalah: {biaya} rupiah")
