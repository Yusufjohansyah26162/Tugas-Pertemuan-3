# Input nilai
nilai = float(input("Masukkan nilai Anda: "))

# Konversi nilai
if nilai < 50:
    konversi = "E"
elif 50 <= nilai < 60:
    konversi = "D"
elif 60 <= nilai < 70:
    konversi = "C"
elif 70 <= nilai < 80:
    konversi = "B"
else:
    konversi = "A"

# Menampilkan hasil konversi
print("Konversi nilai Anda adalah:", konversi)
