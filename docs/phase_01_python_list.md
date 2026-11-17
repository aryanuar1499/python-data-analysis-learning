# Phase 01 — Python List

## 1. Overview

Python List merupakan salah satu built-in data structure pada Python yang digunakan untuk menyimpan sekumpulan elemen dalam satu variabel.

List bersifat **ordered**, **mutable**, dan dapat menyimpan elemen dengan berbagai tipe data, termasuk nested list.

Materi ini dipelajari sebagai bagian dari Python Programming Fundamentals untuk membangun kemampuan mengelola, memanipulasi, dan mengolah data sebelum mempelajari teknik analisis data yang lebih lanjut.

## 2. Learning Objectives

Setelah menyelesaikan pembelajaran Python List, tujuan pembelajaran yang ingin dicapai adalah:

1. Memahami karakteristik dan struktur Python List.
2. Mengakses elemen menggunakan indexing dan slicing.
3. Memodifikasi elemen menggunakan assignment dan list methods.
4. Memahami perbedaan aliasing, shallow copy, dan slicing.
5. Menggunakan `for loop`, `range()`, dan `enumerate()` untuk melakukan iterasi.
6. Mengolah nested list menggunakan nested loop.
7. Menerapkan conditional statements dan accumulator untuk melakukan perhitungan data.
8. Mengidentifikasi dan memperbaiki kesalahan logika maupun runtime melalui debugging.
9. Mengimplementasikan konsep Python List dalam studi kasus sederhana pengelolaan stok gudang.

## 3. Core Concepts & Practical Experiments

### 3.1 List Creation, Indexing & Slicing

#### Theory Summary

Python List merupakan struktur data yang dapat menyimpan beberapa elemen dalam satu variabel menggunakan tanda kurung siku `[]`.

Karakteristik utama Python List:

- **Ordered:** Elemen memiliki urutan dan posisi indeks.
- **Mutable:** Elemen dapat diubah setelah list dibuat.
- **Allows Duplicates:** Nilai yang sama dapat muncul lebih dari satu kali.
- **Heterogeneous:** Dapat menyimpan berbagai tipe data.
- **Nested Structure:** List dapat menyimpan list lain sebagai elemen.

#### Experiment 01 — List Creation

```python
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(numbers)
```

**Expected Output:**

```text
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

#### Experiment 02 — Indexing

```python
print(numbers[2])
print(numbers[-3])
```

**Expected Output:**

```text
15
40
```

**Experiment Findings:**

- Positive indexing dimulai dari indeks `0`.
- Negative indexing dimulai dari indeks `-1` untuk elemen terakhir.
- Indexing mengakses satu elemen berdasarkan posisi.

#### Experiment 03 — Slicing

```python
print(numbers[2:5])
print(numbers[1:8:3])
```

**Expected Output:**

```text
[15, 20, 25]
[10, 25, 40]
```

**Experiment Findings:**

- Slicing menggunakan format `[start:stop:step]`.
- Nilai `start` termasuk dalam hasil.
- Nilai `stop` tidak termasuk dalam hasil.
- Nilai `step` menentukan jarak antarindeks yang diambil.
- Slicing menghasilkan list baru.

#### Key Takeaways

Indexing digunakan untuk mengakses satu elemen, sedangkan slicing digunakan untuk mengambil sekumpulan elemen berdasarkan rentang indeks tertentu.

Pemahaman indexing dan slicing menjadi dasar untuk melakukan manipulasi data menggunakan Python List.

### 3.2 List Mutation & Methods

#### Theory Summary

Python List bersifat **mutable**, artinya elemen di dalam list dapat ditambahkan, diubah, maupun dihapus setelah list dibuat.

Mutasi list dapat dilakukan melalui index assignment, list methods, dan statement seperti `del`.

#### Experiment 04 — Index Assignment & Insert

```python
numbers = [5, 10, 15, 20]

numbers[1] = 50
numbers.insert(1, 100)

print(numbers)
```

**Expected Output:**

```text
[5, 100, 50, 15, 20]
```

**Experiment Findings:**

- Index assignment mengganti nilai elemen pada indeks tertentu.
- `insert(index, value)` menyisipkan elemen pada posisi tertentu tanpa mengganti elemen yang sudah ada.

#### Experiment 05 — Append vs Extend

```python
numbers = [5, 10]

numbers.append([15, 20])
print(numbers)

numbers.extend([25, 30])
print(numbers)
```

**Expected Output:**

```text
[5, 10, [15, 20]]
[5, 10, [15, 20], 25, 30]
```

**Experiment Findings:**

- `append()` menambahkan satu objek sebagai elemen terakhir, termasuk ketika objek tersebut berupa list.
- `extend()` menambahkan setiap elemen dari iterable ke dalam list.
- Nested list yang ditambahkan menggunakan `append()` tetap dihitung sebagai satu elemen pada tingkat terluar.

#### Experiment 06 — Remove, Pop & Clear

```python
numbers = [5, 10, 15, 10, 20]

numbers.remove(10)
print(numbers)

deleted = numbers.pop(2)
print(deleted)
print(numbers)

numbers.clear()
print(numbers)
```

**Expected Output:**

```text
[5, 15, 10, 20]
10
[5, 15, 20]
[]
```

**Experiment Findings:**

- `remove(value)` menghapus kemunculan pertama nilai yang sesuai.
- `pop(index)` menghapus dan mengembalikan elemen pada indeks yang ditentukan.
- `pop()` tanpa argumen menghapus elemen terakhir.
- `clear()` menghapus seluruh elemen sehingga list menjadi kosong.

#### Experiment 07 — Sorting & Reversing

```python
numbers = [30, 10, 20]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)
```

**Expected Output:**

```text
[10, 20, 30]
[30, 20, 10]
[10, 20, 30]
```

**Experiment Findings:**

- `sort()` mengurutkan elemen secara ascending secara default.
- `sort(reverse=True)` mengurutkan elemen secara descending.
- `reverse()` membalik urutan elemen yang sedang ada, bukan melakukan sorting.
- Ketiga metode tersebut memodifikasi list secara langsung (*in-place*).

#### Key Takeaways

List mutation memungkinkan perubahan struktur maupun nilai elemen tanpa harus membuat list baru.

Pemilihan metode yang tepat penting untuk menjaga struktur data dan menghindari kesalahan logika, khususnya ketika bekerja dengan nested list.

### 3.3 Copy, Aliasing & Slicing

#### Theory Summary

Dalam Python, assignment tidak selalu membuat objek baru. Ketika sebuah list diberikan kepada variabel lain menggunakan operator `=`, kedua variabel dapat merujuk pada objek list yang sama. Kondisi ini disebut **aliasing**.

Untuk membuat list baru, Python menyediakan metode `copy()` dan slicing `[:]`.

Keduanya menghasilkan **shallow copy**, yaitu list terluar yang baru, tetapi objek nested yang ada di dalamnya tetap dapat berbagi referensi.

#### Experiment 08 — Aliasing

```python
numbers = [5, 10, 15]
selected = numbers

selected.append(20)

print(numbers)
print(selected)
```

**Expected Output:**

```text
[5, 10, 15, 20]
[5, 10, 15, 20]
```

**Experiment Findings:**

- Assignment `selected = numbers` tidak membuat list baru.
- Kedua variabel merujuk pada objek list yang sama.
- Mutasi melalui salah satu variabel terlihat melalui variabel lainnya.

#### Experiment 09 — List Copy

```python
numbers = [5, 10, 15]
selected = numbers.copy()

selected.append(20)

print(numbers)
print(selected)
```

**Expected Output:**

```text
[5, 10, 15]
[5, 10, 15, 20]
```

**Experiment Findings:**

- `copy()` membuat objek list terluar yang baru.
- Menambahkan elemen ke `selected` tidak mengubah struktur list `numbers`.
- Jika terdapat nested mutable objects, shallow copy belum tentu memisahkan seluruh objek di dalamnya.

#### Experiment 10 — Slicing as Copy

```python
numbers = [5, 10, 15, 20]
selected = numbers[1:3]

selected[0] = 100

print(numbers)
print(selected)
```

**Expected Output:**

```text
[5, 10, 15, 20]
[100, 15]
```

**Experiment Findings:**

- Slicing menghasilkan list baru.
- `numbers[1:3]` mengambil elemen pada indeks 1 dan 2.
- Mengubah elemen pada list hasil slicing tidak mengganti elemen pada list asli dalam contoh ini.

#### Experiment 10.1 — Shallow Copy with Nested List

```python
numbers = [[10, 20], [30, 40]]
selected = numbers.copy()

selected[0][1] = 200

print(numbers)
print(selected)
```

**Expected Output:**

```text
[[10, 200], [30, 40]]
[[10, 200], [30, 40]]
```

**Experiment Findings:**

- `numbers.copy()` membuat list terluar yang baru.
- Nested list di dalam `numbers` dan `selected` masih merujuk pada objek yang sama.
- Mutasi `selected[0][1] = 200` mengubah nested list yang juga diakses melalui `numbers`.
- Shallow copy tidak sama dengan deep copy.
- Untuk membuat salinan independen dari seluruh nested mutable objects, dapat digunakan `copy.deepcopy()` dari Python Standard Library.

**Key Learning:**

Dalam pengolahan data bertingkat, memahami perbedaan shallow copy dan deep copy membantu mencegah perubahan data yang tidak disengaja.

#### Key Takeaways

Memahami aliasing dan shallow copy penting untuk mencegah perubahan data yang tidak disengaja.

Dalam proses analisis data, kita perlu mengetahui apakah suatu operasi mengubah objek asli atau menghasilkan objek baru.

### 3.4 Iteration, Nested Loop & Accumulator

#### Theory Summary

Iteration merupakan proses mengakses elemen dalam sebuah iterable secara berurutan.

Dalam Python List, iterasi dapat dilakukan menggunakan `for loop`, `range()`, dan `enumerate()`.

- **For Loop:** Mengakses setiap elemen dalam iterable.
- **range():** Menghasilkan urutan bilangan integer yang dapat digunakan dalam iterasi.
- **enumerate():** Menghasilkan pasangan penghitung iterasi dan elemen.
- **Nested Loop:** Menjalankan loop di dalam loop lainnya.
- **Accumulator:** Variabel yang digunakan untuk mengumpulkan hasil perhitungan secara bertahap.

#### Experiment 11 — Basic Iteration

```python
numbers = [5, 10, 15, 20]

for number in numbers:
    print(number)
```

**Expected Output:**

```text
5
10
15
20
```

**Experiment Findings:**

Setiap iterasi mengambil satu elemen dari list `numbers` dan menyimpannya sementara dalam variabel `number`.

#### Experiment 12 — Range & Enumerate

```python
warehouse_names = [
    "Central Warehouse",
    "Urban Warehouse",
    "Regional Warehouse"
]

for index, name in enumerate(warehouse_names, start=1):
    print(index, name)
```

**Expected Output:**

```text
1 Central Warehouse
2 Urban Warehouse
3 Regional Warehouse
```

**Experiment Findings:**

- `enumerate()` menghasilkan pasangan penghitung dan nilai elemen.
- `start=1` menentukan nilai awal penghitung.
- `start=1` tidak mengubah indeks asli list.
- Jika penghitung digunakan untuk mengakses list lain, nilai awalnya harus disesuaikan dengan indeks list tersebut.

#### Experiment 13 — Nested Loop & Accumulator

```python
warehouse_stock = [
    [10, 20, 30],
    [15, 25, 35],
    [5, 10, 15]
]

for warehouse in warehouse_stock:
    total_stock = 0

    for stock in warehouse:
        total_stock += stock

    print(total_stock)
```

**Expected Output:**

```text
60
75
30
```

**Experiment Findings:**

- Outer loop mengakses setiap list stok gudang.
- Inner loop mengakses setiap nilai stok dalam gudang tersebut.
- `total_stock = 0` ditempatkan di dalam outer loop agar perhitungan dimulai ulang untuk setiap gudang.
- `total_stock += stock` mengakumulasikan nilai stok.
- `print(total_stock)` ditempatkan setelah inner loop selesai agar hanya menampilkan total akhir masing-masing gudang.

#### Key Takeaways

Kombinasi iteration, nested loop, dan accumulator memungkinkan pengolahan data bertingkat tanpa bergantung pada fungsi agregasi bawaan seperti `sum()`.

Konsep ini menjadi dasar untuk melakukan pengelompokan, perhitungan, dan ringkasan data dalam proses analisis menggunakan Python.

### 3.5 List Comprehension & Filtering

#### Theory Summary

List comprehension merupakan sintaks Python untuk membuat list baru berdasarkan iterable yang sudah ada.

List comprehension dapat digunakan untuk melakukan transformasi nilai, filtering berdasarkan kondisi, atau kombinasi keduanya.

**Basic Syntax:**

```python
new_list = [expression for item in iterable]
```

**Filtering Syntax:**

```python
new_list = [expression for item in iterable if condition]
```

Komponen utama:

- `expression`: Nilai yang dimasukkan ke dalam list baru.
- `item`: Variabel yang merepresentasikan elemen selama iterasi.
- `iterable`: Objek yang dapat diiterasi, seperti list.
- `condition`: Kondisi untuk menentukan elemen yang disertakan.

#### Experiment 14 — Basic List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)
```

**Expected Output:**

```text
[1, 4, 9, 16, 25]
```

**Experiment Findings:**

- Setiap elemen dalam `numbers` diproses menggunakan ekspresi `x ** 2`.
- Hasil transformasi disimpan dalam list baru bernama `squares`.
- List asli `numbers` tidak mengalami perubahan.

#### Experiment 15 — Filtering Low Stock

```python
stock = [5, 12, 8, 20, 3, 15, 10]

low_stock = [x for x in stock if x < 10]

print(low_stock)
```

**Expected Output:**

```text
[5, 8, 3]
```

**Experiment Findings:**

- Kondisi `x < 10` digunakan untuk menyaring nilai stok.
- Hanya nilai yang memenuhi kondisi yang dimasukkan ke dalam `low_stock`.
- Nilai `10` tidak termasuk karena operator `<` bersifat strict.

#### Experiment 16 — Filtering & Transformation

```python
stock = [5, 12, 8, 20, 3, 15, 10]

selected = [x * 2 for x in stock if x >= 10]

print(selected)
print(stock)
```

**Expected Output:**

```text
[24, 40, 30, 20]
[5, 12, 8, 20, 3, 15, 10]
```

**Experiment Findings:**

- Kondisi `x >= 10` menentukan elemen yang dipilih.
- Ekspresi `x * 2` dijalankan untuk setiap elemen yang memenuhi kondisi.
- Hasil disimpan dalam list baru tanpa mengubah list asli.

#### Key Takeaways

List comprehension memungkinkan proses iterasi, filtering, dan transformasi ditulis secara ringkas.

Dalam analisis data, konsep ini dapat digunakan untuk mengidentifikasi stok rendah, memilih data berdasarkan kriteria, dan melakukan transformasi nilai sebelum analisis lebih lanjut.

Walaupun lebih ringkas, penggunaan list comprehension tetap harus mempertimbangkan keterbacaan kode (*code readability*).