# Input data pendaftar
nama = input("Nama: ")
tempat_lahir = input("Tempat Lahir: ")
tanggal_lahir = input("Tanggal Lahir (format: YYYY-MM-DD): ")
jenis_kelamin = input("Jenis Kelamin (Laki-laki/Perempuan): ")

# Mendapatkan tahun lahir dari tanggal lahir
tahun_lahir = int(tanggal_lahir.split("-")[0])

# Input nilai mata pelajaran
nilai_english = float(input("Nilai English: "))
nilai_matematika = float(input("Nilai Matematika: "))
nilai_indonesia = float(input("Nilai Indonesia: "))

# Menghitung rata-rata nilai
rata_rata_nilai = (nilai_english + nilai_matematika + nilai_indonesia) / 3

# Menentukan jurusan berdasarkan rata-rata nilai dan jenis kelamin
if rata_rata_nilai > 80:
    if jenis_kelamin.lower() == "laki-laki":
        jurusan = "Teknik Informatika"
    elif jenis_kelamin.lower() == "perempuan":
        jurusan = "Sistem Informasi"
    else:
        jurusan = "DKV"
else:
    jurusan = "DKV"

# Menentukan apakah mahasiswa diterima atau tidak berdasarkan umur
umur = 2024 - tahun_lahir
if umur < 25:
    status_penerimaan = "Diterima"
else:
    status_penerimaan = "Tidak Diterima (Umur di atas 25 tahun)"

# Menampilkan hasil
print("\nHasil Pendaftaran:")
print("Nama:", nama)
print("Tempat Lahir:", tempat_lahir)
print("Tanggal Lahir:", tanggal_lahir)
print("Umur:", umur, "tahun")
print("Jenis Kelamin:", jenis_kelamin)
print("Rata-rata Nilai:", rata_rata_nilai)
print("Jurusan:", jurusan)
print("Status Penerimaan:", status_penerimaan)
