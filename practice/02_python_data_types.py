# Practice 01 — Basic Data Types

angka = 100
desimal = 100.0
teks = "100"
aktif = True

print(type(angka))
print(type(desimal))
print(type(teks))
print(type(aktif))

# Practice 02 — Division Operators

a = 15 / 3
b = 15 // 3

print(a, type(a))
print(b, type(b))

#dynamic typing - reassignment

nilai = 50
nilai = "Lima Puluh"
nilai = 75.5

print(nilai)
print(type(nilai))

a = 10
b = a

a = 20

print(a)
print(b)

x = 50
y = x

x = 100
y = 200

print(x)
print(y)

angka = 10
# print(angka)
angka = 20
# print(angka)
print(angka)

angka = 30
print(angka)

# type conversion

angka_teks = "100"
angka_bulat = int(angka_teks)

print(angka_bulat)
print(type(angka_bulat))

harga = "25000"
jumlah = 2

total = int(harga) * jumlah

print(total)
print(type(total))

harga = "25000"
jumlah = 2

print(harga * jumlah)

# Experiment: Type Conversion
harga = "15000"
jumlah = 3

total_a = harga * jumlah
total_b = int(harga) * jumlah

print(total_a, type(total_a))
print(total_b, type(total_b))

# Experiment: String to Float Conversion

harga = "12500.50"
jumlah = 2

total = float(harga) * jumlah

print(total)
print(type(total))

# Experiment: Integer to String Conversion

stok_awal = 100
stok_masuk = 50

hasil_a = stok_awal + stok_masuk
hasil_b = str(stok_awal) + str(stok_masuk)

print(hasil_a, type(hasil_a))
print(hasil_b, type(hasil_b))

stok_awal = 100
stok_masuk = 50

hasil_a = stok_awal + stok_masuk
hasil_b = str(stok_awal) + str(stok_masuk)

print(hasil_a)
print(hasil_b)
print(type(hasil_b))

# Experiment: Boolean Conversion — Numeric Truthiness

nilai_a = 0
nilai_b = 25
nilai_c = -10
nilai_d = 0.0

print(bool(nilai_a))
print(bool(nilai_b))
print(bool(nilai_c))
print(bool(nilai_d))

# Experiment: Boolean Conversion — String Truthiness

teks_a = ""
teks_b = "0"
teks_c = "False"
teks_d = " "

print(bool(teks_a))
print(bool(teks_b))
print(bool(teks_c))
print(bool(teks_d))

# Experiment: Boolean Truthiness vs Business Logic

stok_a = 0
stok_b = -5
stok_c = 20

print(bool(stok_a), stok_a > 0)
print(bool(stok_b), stok_b > 0)
print(bool(stok_c), stok_c > 0)