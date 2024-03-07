# 1a. Inputan nilai dan pengecekan kelulusan
nilai = float(input("Masukkan nilai Anda: "))
if nilai > 75:
    print("Selamat, Anda lulus!")
else:
    print("Maaf, Anda belum lulus.")

# 1b. Inputan tahun lahir dan pengecekan generasi
tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
if tahun_lahir >= 2000:
    print("Anda merupakan bagian dari generasi Gen-Z.")
else:
    print("Anda bukan merupakan bagian dari generasi Gen-Z.")
