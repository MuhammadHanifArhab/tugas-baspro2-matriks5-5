# Inisialisasi matriks kosong
matriks = []

# Membuat matriks 5x5 dengan menggunakan append
for i in range(5):
    baris = []
    for j in range(5):
        baris.append(i * 5 + j + 1)  # Mengisi angka 1 - 25. Bisa juga diganti dengan nilai lain
    matriks.append(baris)

# Print matriks
for baris in matriks:
    print(baris)