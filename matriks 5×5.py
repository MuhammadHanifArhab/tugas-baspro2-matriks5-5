matriks = []

for i in range(5):
    baris = []
    for j in range(5):
        baris.append(i * 5 + j + 1)
    matriks.append(baris)

for baris in matriks:
    print(baris)
