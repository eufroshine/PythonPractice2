import math

def hitung_luas_lingkaran(r):
    luas = math.pi * r**2
    return luas

def hitung_keliling_lingkaran(r):
    keliling = 2 * math.pi * r
    return keliling

# Input jari-jari
r = float(input("Masukkan jari-jari lingkaran: "))

# Hitung luas dan keliling
luas_lingkaran = hitung_luas_lingkaran(r)
keliling_lingkaran = hitung_keliling_lingkaran(r)

# Menampilkan hasil
print(f"Luas lingkaran: {luas_lingkaran:.2f}")
print(f"Keliling lingkaran: {keliling_lingkaran:.2f}")