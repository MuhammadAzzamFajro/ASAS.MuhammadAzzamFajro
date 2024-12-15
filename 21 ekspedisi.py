while True:
    print("=== Program Perhitungan Biaya Ekspedisi ===")

    # Meminta input dimensi paket
    berat = float(input("Masukkan berat paket (kg): "))
      # Memastikan berat minimal adalah 1 kg
    if berat < 1:
        print("Maaf hanya melayani di atas 1 kg.")
        ulang = input("Apakah ingin memesan lagi? (y/n): ").lower()
        if ulang != 'y':
            print("Terima kasih telah menggunakan program ini!")
            break  # Keluar dari loop jika pengguna tidak ingin mencoba lagi
        continue  # Kembali ke awal loop jika pengguna ingin mencoba lagi
    panjang = float(input("Masukkan panjang paket (cm): "))
    lebar = float(input("Masukkan lebar paket (cm): "))
    tinggi = float(input("Masukkan tinggi paket (cm): "))
     # Meminta input lokasi pengiriman
    lokasi = input("Masukkan lokasi pengiriman (Kota/Kabupaten Pasuruan): ")
    lokasi_valid = ["Kota Pasuruan", "Kabupaten Pasuruan"]  # lokasi yang valid

    # Memeriksa apakh lokasi yang dimasukkan valid
    if lokasi not in lokasi_valid:
        print("Maaf, layanan hanya tersedia untuk area Kota dan Kabupaten Pasuruan.")
        # Menanyakan kepada pengguna apakah ingin memesan lagi
        ulang = input("Apakah ingin memesan lagi? (y/n): ").lower()
        if ulang != 'y':
            print("Terima kasih telah menggunakan program ini!")
            break  # Keluar dari loop jika pengguna tidak ingin mencoba lagi
        continue  # Kembali ke awal loop jika pengguna ingin mencoba lagi
        
    # Menghitung volume paket
    volume = panjang * lebar * tinggi
    biaya_tambahan = 0 

    # Menentukan biaya per kg berdasarkan volume paket
    if volume == 50 * 50 * 50:
        biaya_per_kg = 8000  # Biaya per kg jika volume tepat 50 x 50 x 50 cm³
    elif volume > 50 * 50 * 50:
        biaya_per_kg = 7000  # Biaya per kg jika volume lebih dari 125000 cm³
        biaya_tambahan = 50000  # Biaya tambahan untuk volume lebih besar
    else:
        biaya_per_kg = 5000  # Biaya per kg jika volume kurang dari 125000 cm³

    # Menghitung total biaya pengiriman
    total_biaya = berat * biaya_per_kg + biaya_tambahan

    # Menampilkan total biaya pengiriman
    print(f"Biaya total pengiriman: Rp {total_biaya:,}")

    # Menanyakan kepada pengguna apakah ingin menghitung ulang
    ulang = input("Apakah ingin menghitung ulang? (y/n): ").lower()
    if ulang != 'y':
        print("Terima kasih telah menggunakan program ini!")
        break  # Keluar dari loop jika pengguna tidak ingin menghitung ulang
