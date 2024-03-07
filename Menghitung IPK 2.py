# List mata kuliah
mata_kuliah = ["Algoritma", "Perancangan Objek", "Kalkulus", "Etika Profesi", "Databases", "English"]

# List kriteria dan nilai IPK
kriteria = [(90, 100, 4), (85, 89, 3.75), (80, 84, 3.5), (75, 79, 3.25), (70, 74, 3), (65, 69, 2.75),
            (60, 64, 2.5), (55, 59, 2.25), (50, 54, 2), (45, 49, 1.75), (40, 44, 1.5), (35, 39, 1.25),
            (30, 34, 1), (0, 29, 0)]

# Input nilai mata kuliah
nilai_mata_kuliah = []
for matkul in mata_kuliah:
    nilai = float(input("Masukkan nilai {} Anda: ".format(matkul)))
    nilai_mata_kuliah.append(nilai)

# Menghitung IPK untuk setiap mata kuliah
ipk_mata_kuliah = []
for nilai in nilai_mata_kuliah:
    for k in kriteria:
        if k[0] <= nilai <= k[1]:
            ipk_mata_kuliah.append(k[2])
            break

# Menghitung IPK semester
ipk_semester = sum(ipk_mata_kuliah) / len(mata_kuliah)

# Menampilkan hasil
print("IPK Anda untuk semester ini adalah:", ipk_semester)