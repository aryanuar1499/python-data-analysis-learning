
# MP01.2.2 — Python List Structure Design

## Mini Project 01 — Basic Inventory Stock Analysis

**Project:** Python for Data Analysis  
**Phase:** MP01.2 — Data Requirements & Structure Design  
**Module:** MP01.2.2 — Python List Structure Design  
**Status:** In Progress

---

## 1. Gambaran Umum (Overview)

Pada modul ini, pembelajaran difokuskan pada perancangan dan pengolahan data persediaan (inventory) menggunakan struktur data Python Nested List.

Setiap data produk memiliki tiga atribut utama:

- Product ID: Identitas unik produk.
- Product Name: Nama produk.
- Stock Quantity: Jumlah persediaan produk.

Melalui latihan Q4–Q8, dilakukan penerapan berbagai konsep dasar Python untuk mengakses, melakukan iterasi, memfilter, menghitung, dan mengolah data persediaan.

Modul ini merupakan bagian dari Mini Project 01 — Basic Inventory Stock Analysis yang bertujuan membangun pemahaman fundamental sebelum mengembangkan analisis inventory lebih lanjut.

## 2. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan latihan Q4–Q8, kompetensi yang telah dipelajari meliputi:

1. Menghitung total persediaan menggunakan Nested List.
2. Memahami konsep Accumulator, Initialization, dan Iteration.
3. Mengidentifikasi produk dengan jumlah stok di bawah batas minimum (Low Stock).
4. Menghitung jumlah produk Low Stock menggunakan Counting Accumulator.
5. Menghitung total kuantitas Low Stock menggunakan Summation Accumulator.
6. Menyimpan hasil Filtering ke dalam List baru menggunakan method `.append()`.
7. Mengakses informasi produk menggunakan Nested List Indexing.
8. Memahami perbedaan Object Reference, Mutation, dan Shallow Copy menggunakan `.copy()`.

## 3. Tools dan Lingkungan Pengembangan

- Bahasa Pemrograman: Python
- Code Editor: Visual Studio Code
- Terminal: Git Bash
- Virtual Environment: `.venv`
- Version Control: Git & GitHub
- Repository: `python-data-analysis-learning`
- Branch: `main`
- File Praktik: `practice/mp01_2_2_list_structure.py`

---

## 4. Struktur Dataset (Dataset Structure)

Dataset inventory pada Mini Project 01 menggunakan struktur
Nested List, yaitu sebuah List yang berisi beberapa List
sebagai representasi data produk.

### 4.1 Representasi Dataset

```python
products = [
    ["P001", "Product A", 15],
    ["P002", "Product B", 6],
    ["P003", "Product C", 25],
    ["P004", "Product D", 3],
    ["P005", "Product E", 10],
    ["P006", "Product F", 8]
]
```

Setiap Inner List merepresentasikan satu produk, sedangkan
Outer List berfungsi sebagai tempat penyimpanan seluruh
data produk.

### 4.2 Struktur Atribut Produk

| Index | Atribut | Tipe Data | Contoh |
|---|---|---|---|
| 0 | Product ID | String | "P001" |
| 1 | Product Name | String | "Product A" |
| 2 | Stock Quantity | Integer | 15 |

Product ID digunakan sebagai identitas produk, sedangkan
Stock Quantity merupakan nilai numerik yang digunakan
dalam proses perhitungan inventory.

### 4.3 Nested List Indexing

Untuk mengakses informasi produk, digunakan dua index:

- Index pertama menentukan posisi produk dalam Outer List.
- Index kedua menentukan atribut dalam Inner List.

Contoh:

```python
print(products[1][0])
print(products[1][1])
print(products[1][2])
```

Expected Output:

```text
P002
Product B
6
```

Penjelasan:

1. `products[1]` mengambil data Product B.
2. `[0]` mengakses Product ID.
3. `[1]` mengakses Product Name.
4. `[2]` mengakses Stock Quantity.

### 4.4 Kesimpulan Struktur Dataset

Penggunaan Nested List memungkinkan beberapa atribut
produk disimpan dalam satu struktur data.

Struktur ini dapat digunakan untuk melakukan iterasi,
filtering, counting, dan summation menggunakan konsep
dasar Python.

Meskipun sesuai untuk pembelajaran fundamental,
struktur Nested List memiliki keterbatasan karena
pengaksesan atribut bergantung pada posisi index.

---

## 5. Total Stock Calculation (Q4–Q5)

### 5.1 Konsep Accumulator

Accumulator merupakan variabel yang digunakan untuk
menyimpan hasil perhitungan secara bertahap selama
proses iterasi berlangsung.

Dalam analisis inventory, accumulator digunakan untuk
menghitung total Stock Quantity dari seluruh produk.

### 5.2 Q4 — Calculating Total Stock

Contoh implementasi perhitungan total persediaan:

```python
total_stock = 0

for product in products:
    total_stock += product[2]

print(total_stock)
```

Penjelasan:

- `total_stock = 0` merupakan proses initialization.
- `for product in products` melakukan iterasi terhadap
  setiap produk dalam Nested List.
- `product[2]` mengakses Stock Quantity setiap produk.
- `+=` menambahkan Stock Quantity ke nilai accumulator
  yang telah tersimpan sebelumnya.

Berdasarkan dataset latihan Q4, proses perhitungan
berlangsung sebagai berikut:

| Iterasi | Stock Quantity | Total Stock |
|---|---:|---:|
| Initialization | - | 0 |
| 1 | 20 | 20 |
| 2 | 35 | 55 |
| 3 | 15 | 70 |

Expected Output:

```text
70
```

### 5.3 Pengaruh Posisi Initialization

Dilakukan eksperimen dengan menempatkan initialization
di dalam For Loop.

```python
for product in products:
    total_stock = 0
    total_stock += product[2]

print(total_stock)
```

Output:

```text
15
```

Hasil tersebut terjadi karena nilai `total_stock`
diinisialisasi ulang menjadi 0 pada setiap iterasi.

Akibatnya, accumulator tidak menyimpan hasil
perhitungan dari iterasi sebelumnya.

Untuk menghitung total persediaan secara keseluruhan,
initialization harus ditempatkan sebelum For Loop.

### 5.4 Q5 — Independent Total Stock Calculation

Pada latihan Q5, dilakukan implementasi perhitungan
total persediaan secara mandiri menggunakan dataset
dengan Stock Quantity yang berbeda.

| Iterasi | Stock Quantity | Total Stock |
|---|---:|---:|
| Initialization | - | 0 |
| 1 | 25 | 25 |
| 2 | 40 | 65 |
| 3 | 15 | 80 |
| 4 | 30 | 110 |

Expected Output:

```text
110
```

Actual Output:

```text
110
```

Validation Status: PASSED

### 5.5 Kesimpulan Pembelajaran Q4–Q5

Berdasarkan latihan dan eksperimen yang dilakukan,
diperoleh beberapa pemahaman:

- Accumulator menyimpan hasil perhitungan secara kumulatif.
- Initialization menentukan nilai awal accumulator.
- Posisi initialization memengaruhi hasil perhitungan.
- For Loop memungkinkan pengolahan seluruh data produk
  secara sistematis.
- Nested List Indexing memungkinkan pengambilan atribut
  numerik untuk kebutuhan analisis inventory.

Hasil prediksi dan runtime validation menunjukkan
hasil perhitungan yang sesuai.

**Learning Status: COMPLETED**


---

## 6. Conditional Filtering & Counting (Q6–Q7)

### 6.1 Konsep Conditional Filtering

Conditional Filtering merupakan proses seleksi data
berdasarkan kondisi atau kriteria tertentu.

Dalam analisis inventory, konsep ini digunakan untuk
mengidentifikasi produk yang memiliki Stock Quantity
di bawah batas minimum persediaan (Minimum Stock).

Kondisi yang digunakan adalah:

```python
product[2] < minimum_stock
```

Operator `<` digunakan karena produk dikategorikan
sebagai Low Stock apabila jumlah persediaannya lebih
kecil daripada Minimum Stock.

Produk dengan jumlah persediaan yang sama dengan
Minimum Stock tidak dikategorikan sebagai Low Stock.

### 6.2 Q6 — Identifying Low Stock Products

Implementasi Conditional Filtering:

```python
for product in products:
    if product[2] < minimum_stock:
        print(product[1])
```

Penjelasan:

- `for product in products` melakukan iterasi terhadap
  seluruh data produk.
- `if` melakukan evaluasi terhadap kondisi Low Stock.
- `product[2]` mengakses Stock Quantity.
- `product[1]` mengakses Product Name.
- `print()` hanya dijalankan apabila kondisi bernilai True.

Berdasarkan dataset latihan Q6, diperoleh hasil:

Expected Output:

```text
Product B
Product D
```

Actual Output:

```text
Product B
Product D
```

Validation Status: PASSED

### 6.3 Q7 — Counting and Summation Accumulator

Pada latihan Q7, proses Conditional Filtering
dikembangkan untuk menghitung:

1. Jumlah produk yang dikategorikan sebagai Low Stock.
2. Total Stock Quantity dari seluruh produk Low Stock.

Dataset latihan:

| Product ID | Product Name | Stock Quantity |
|---|---|---:|
| P001 | Product A | 30 |
| P002 | Product B | 7 |
| P003 | Product C | 12 |
| P004 | Product D | 4 |
| P005 | Product E | 9 |

Minimum Stock: 10

Implementasi:

```python
minimum_stock = 10
low_stock_count = 0
low_stock_quantity = 0

for product in products:
    if product[2] < minimum_stock:
        low_stock_count += 1
        low_stock_quantity += product[2]

print(low_stock_count)
print(low_stock_quantity)
```

### 6.4 Iteration Analysis

| Iterasi | Stock Quantity | Condition | Count | Quantity |
|---|---:|---|---:|---:|
| Initialization | - | - | 0 | 0 |
| 1 | 30 | False | 0 | 0 |
| 2 | 7 | True | 1 | 7 |
| 3 | 12 | False | 1 | 7 |
| 4 | 4 | True | 2 | 11 |
| 5 | 9 | True | 3 | 20 |

Expected Output:

```text
3
20
```

Actual Output:

```text
3
20
```

Validation Status: PASSED

### 6.5 Perbedaan Counting dan Summation Accumulator

Counting Accumulator:

```python
low_stock_count += 1
```

Digunakan untuk menghitung jumlah produk yang
memenuhi kondisi Low Stock.

Summation Accumulator:

```python
low_stock_quantity += product[2]
```

Digunakan untuk menjumlahkan Stock Quantity dari
produk yang memenuhi kondisi Low Stock.

| Accumulator | Fungsi | Hasil |
|---|---|---:|
| Counting | Menghitung jumlah produk Low Stock | 3 |
| Summation | Menghitung total kuantitas Low Stock | 20 |

Jumlah produk dan jumlah kuantitas persediaan
merupakan dua indikator inventory yang berbeda.

### 6.6 Pengaruh Indentation terhadap Hasil Perhitungan

Dilakukan eksperimen dengan menempatkan Summation
Accumulator di luar blok `if`, tetapi tetap berada
di dalam For Loop.

```python
low_stock_count = 0
low_stock_quantity = 0

for product in products:
    if product[2] < minimum_stock:
        low_stock_count += 1

    low_stock_quantity += product[2]

print(low_stock_count)
print(low_stock_quantity)
```

Output:

```text
3
64
```

Hasil tersebut terjadi karena:

- Counting Accumulator hanya dijalankan ketika
  kondisi Low Stock bernilai True.
- Summation Accumulator dijalankan pada setiap
  iterasi tanpa mempertimbangkan kondisi Low Stock.

Akibatnya, nilai 64 merupakan total persediaan
seluruh produk, bukan total persediaan Low Stock.

Eksperimen ini menunjukkan bahwa indentation
tidak hanya berkaitan dengan penulisan syntax,
tetapi juga menentukan alur logika program
(Control Flow).

### 6.7 Kesimpulan Pembelajaran Q6–Q7

Berdasarkan latihan dan eksperimen yang dilakukan,
diperoleh beberapa pemahaman:

- Conditional Filtering digunakan untuk menyeleksi
  data berdasarkan kondisi tertentu.
- Comparison Operator menentukan kriteria seleksi.
- Counting Accumulator menghitung jumlah data yang
  memenuhi kondisi.
- Summation Accumulator menjumlahkan nilai numerik
  dari data yang memenuhi kondisi.
- Indentation menentukan cakupan eksekusi suatu
  statement dalam program.
- Kesalahan logika dapat menghasilkan output yang
  tidak sesuai meskipun program berjalan tanpa error.

Hasil prediksi dan runtime validation menunjukkan
hasil perhitungan yang sesuai.

**Learning Status: COMPLETED**

---

## 7. Collecting Data & Object References (Q8)

### 7.1 Konsep Collecting Filtered Data

Pada latihan sebelumnya, hasil Conditional Filtering
ditampilkan secara langsung menggunakan fungsi `print()`.

Pada latihan Q8, proses tersebut dikembangkan dengan
menyimpan hasil filtering ke dalam List baru menggunakan
method `.append()`.

Pendekatan ini memungkinkan hasil filtering disimpan
dan digunakan kembali untuk kebutuhan analisis lanjutan.

### 7.2 Q8 — Collecting Product Names

Untuk menyimpan nama produk yang memenuhi kondisi
Low Stock, digunakan implementasi berikut:

```python
low_stock_products = []

for product in products:
    if product[2] < minimum_stock:
        low_stock_products.append(product[1])

print(low_stock_products)
```

Method `.append(product[1])` menambahkan Product Name
ke dalam List baru.

Output:

```text
['Product B', 'Product D', 'Product E']
```

Hasil filtering berbentuk One-Dimensional List yang
hanya menyimpan atribut Product Name.

### 7.3 Collecting Complete Product Records

Untuk menyimpan seluruh atribut produk, digunakan
method `.append(product)`.

```python
low_stock_products = []

for product in products:
    if product[2] < minimum_stock:
        low_stock_products.append(product)

print(low_stock_products)
```

Output:

```text
[
    ['P002', 'Product B', 7],
    ['P004', 'Product D', 4],
    ['P005', 'Product E', 9]
]
```

Hasil filtering berbentuk Nested List yang tetap
mempertahankan seluruh atribut produk.

### 7.4 Perbedaan Penyimpanan Data

| Method | Data yang Disimpan | Struktur Output |
|---|---|---|
| `.append(product[1])` | Product Name | One-Dimensional List |
| `.append(product)` | Seluruh atribut produk | Nested List |
| `.append(product.copy())` | Salinan Inner List produk | Nested List |

Pemilihan method bergantung pada kebutuhan analisis
dan pengelolaan data.

### 7.5 Q8.3 — Nested List Indexing

Data hasil filtering dapat diakses kembali menggunakan
Nested List Indexing.

```python
print(low_stock_products[1][2])
print(low_stock_products[2][1])
print(low_stock_products[1][0])
```

Expected Output:

```text
4
Product E
P004
```

Index pertama menentukan posisi produk dalam List
hasil filtering, bukan posisi produk pada dataset awal.

Index kedua menentukan atribut produk yang diakses.

### 7.6 Q8.4 — Independent Inventory Filtering

Pada latihan ini, dilakukan implementasi secara mandiri
dengan menggabungkan beberapa konsep yang telah dipelajari.

Dataset:

```python
products = [
    ["P001", "Product A", 15],
    ["P002", "Product B", 6],
    ["P003", "Product C", 25],
    ["P004", "Product D", 3],
    ["P005", "Product E", 10],
    ["P006", "Product F", 8]
]
```

Implementasi:

```python
minimum_stock = 10
low_stock_products = []
low_stock_count = 0
low_stock_quantity = 0

for product in products:
    if product[2] < minimum_stock:
        low_stock_products.append(product)
        low_stock_count += 1
        low_stock_quantity += product[2]

print(low_stock_products)
print(low_stock_count)
print(low_stock_quantity)
```

Iteration Analysis:

| Product ID | Stock | Condition | Count | Quantity |
|---|---:|---|---:|---:|
| P001 | 15 | False | 0 | 0 |
| P002 | 6 | True | 1 | 6 |
| P003 | 25 | False | 1 | 6 |
| P004 | 3 | True | 2 | 9 |
| P005 | 10 | False | 2 | 9 |
| P006 | 8 | True | 3 | 17 |

Actual Output:

```text
[['P002', 'Product B', 6], ['P004', 'Product D', 3], ['P006', 'Product F', 8]]
3
17
```

Hasil analisis:

| Inventory Indicator | Result |
|---|---:|
| Minimum Stock | 10 |
| Low Stock Product Count | 3 |
| Total Low Stock Quantity | 17 |

Product E tidak dikategorikan sebagai Low Stock karena
Stock Quantity sama dengan Minimum Stock.

Validation Status: PASSED

### 7.7 Q8.5 — Object Reference dan Aliasing

Penggunaan `.append(product)` tidak membuat salinan
Inner List, melainkan menyimpan referensi terhadap
objek Inner List yang sudah ada.

Meskipun `products` dan `low_stock_products` merupakan
dua objek Outer List yang berbeda, keduanya dapat
merujuk pada objek Inner List yang sama.

Kondisi berbagi referensi terhadap objek yang sama
disebut Aliasing.

Eksperimen:

```python
low_stock_products[0][2] = 100

print(products[1][2])
print(low_stock_products[0][2])
```

Expected Output:

```text
100
100
```

Perubahan Stock Quantity pada List hasil filtering
juga memengaruhi dataset awal karena kedua elemen
merujuk pada objek Inner List yang sama.

### 7.8 Q8.5.1 — Shallow Copy

Untuk mencegah perubahan Stock Quantity pada List hasil
filtering memengaruhi dataset awal, digunakan method
`.copy()` pada setiap Inner List yang memenuhi kondisi.

Eksperimen dilakukan kembali menggunakan dataset awal
Q8.4 sebelum terjadi Mutation.

```python
low_stock_products = []

for product in products:
    if product[2] < minimum_stock:
        low_stock_products.append(product.copy())

low_stock_products[0][2] = 100

print(products[1][2])
print(low_stock_products[0][2])
```

Expected Output:

```text
6
100
```

Method `.copy()` membuat objek Inner List baru sehingga
penggantian nilai Stock Quantity pada List hasil
filtering tidak mengubah dataset awal.

### 7.9 Perbandingan Object Reference dan Shallow Copy

| Aspek | `.append(product)` | `.append(product.copy())` |
|---|---|---|
| Outer List baru | Ya | Ya |
| Inner List baru | Tidak | Ya |
| Berbagi referensi Inner List | Ya | Tidak |
| Stock awal setelah Mutation | 100 | 6 |
| Stock hasil filtering setelah Mutation | 100 | 100 |

Shallow Copy cukup untuk dataset ini karena setiap
Inner List hanya berisi String dan Integer yang
bersifat Immutable.

Namun, apabila Inner List memiliki objek Mutable
lain di dalamnya, Shallow Copy masih dapat berbagi
referensi terhadap objek tersebut.

### 7.10 Kesimpulan Pembelajaran Q8

Berdasarkan latihan dan eksperimen yang dilakukan,
diperoleh beberapa pemahaman:

- Method `.append()` digunakan untuk mengumpulkan
  hasil filtering ke dalam List baru.
- Struktur hasil filtering bergantung pada objek
  yang ditambahkan ke dalam List.
- Nested List Indexing dapat digunakan untuk
  mengakses kembali hasil filtering.
- Conditional Filtering, Counting, dan Summation
  dapat dikombinasikan dalam satu For Loop.
- Object Reference dan Aliasing dapat menyebabkan
  perubahan data pada lebih dari satu List.
- Shallow Copy dapat digunakan untuk membuat
  salinan Inner List yang independen pada dataset ini.
- Pemahaman mengenai Mutation penting untuk menjaga
  integritas dataset selama proses analisis.

**Learning Status: COMPLETED**

---

## 8. Evaluasi Pembelajaran (Learning Evaluation)

### 8.1 Learning Assessment

Evaluasi pembelajaran dilakukan melalui beberapa pendekatan:

- Conceptual Understanding
- Output Prediction
- Independent Coding
- Runtime Validation
- Error and Logic Analysis

Pendekatan tersebut bertujuan untuk memastikan bahwa
pembelajaran tidak hanya berfokus pada keberhasilan
menjalankan program, tetapi juga pada pemahaman
terhadap proses dan logika program.

### 8.2 Learning Outcomes

| Materi | Kompetensi | Status |
|---|---|---|
| Q4 | Total Stock Calculation | PASSED |
| Q5 | Independent Stock Calculation | PASSED |
| Q6 | Conditional Filtering | PASSED |
| Q7 | Counting and Summation Accumulator | PASSED |
| Q8 | Collecting Filtered Data | PASSED |
| Q8.3 | Nested List Indexing | PASSED |
| Q8.4 | Independent Inventory Filtering | PASSED |
| Q8.5 | Object Reference and Aliasing | PASSED |
| Q8.5.1 | Shallow Copy | PASSED |

### 8.3 Runtime Validation Summary

| Eksperimen | Expected Output | Actual Output |
|---|---|---|
| Q4 - Total Stock | 70 | 70 |
| Q5 - Total Stock | 110 | 110 |
| Q6 - Low Stock Products | Product B, Product D | Sesuai |
| Q7 - Low Stock Count | 3 | 3 |
| Q7 - Low Stock Quantity | 20 | 20 |
| Q8.4 - Low Stock Count | 3 | 3 |
| Q8.4 - Low Stock Quantity | 17 | 17 |

Pada eksperimen Q8.5.1, hasil prediksi Shallow Copy
adalah 6 dan 100. Eksekusi program dilaporkan berjalan
tanpa error, tetapi output terminal tidak dicatat
secara langsung dalam evaluasi.

### 8.4 Key Learning Points

Beberapa pemahaman penting yang diperoleh selama
proses pembelajaran:

1. Posisi initialization memengaruhi hasil accumulator.
2. Comparison Operator menentukan batas kondisi filtering.
3. Counting dan Summation memiliki tujuan analisis
   yang berbeda.
4. Indentation menentukan alur eksekusi program.
5. Nested List Indexing memungkinkan pengaksesan
   atribut berdasarkan posisi index.
6. Object Reference dapat menyebabkan perubahan
   pada dataset awal.
7. Shallow Copy dapat menjaga independensi Inner List
   pada struktur dataset yang digunakan.

---

## 9. Kesimpulan Teknis (Technical Conclusion)

Python Nested List dapat digunakan sebagai struktur
data sederhana untuk melakukan analisis inventory
tanpa menggunakan library eksternal.

Dengan memanfaatkan konsep fundamental Python,
beberapa proses analisis telah berhasil diterapkan:

- Total Stock Calculation
- Low Stock Identification
- Low Stock Product Counting
- Low Stock Quantity Calculation
- Filtered Data Collection
- Object Reference Management

Pembelajaran ini memberikan fondasi untuk memahami
bagaimana data disimpan, diakses, diproses, dan
ditransformasikan menggunakan Python.

Pemahaman mengenai Object Reference, Mutation,
dan Shallow Copy juga menjadi dasar penting dalam
menjaga integritas data selama proses analisis.

Kompetensi tersebut akan mendukung pembelajaran
struktur data yang lebih kompleks serta penggunaan
library Data Analysis seperti NumPy dan Pandas
pada tahapan berikutnya.

---

## 10. Learning Checkpoint

**Mini Project:** MP01 - Basic Inventory Stock Analysis

**Module:** MP01.2.2 - Python List Structure Design

**Completed Exercises:** Q1-Q8

**Documentation Scope:** Q4-Q8

**Learning Evaluation:** PASSED

**Module Status:** IN PROGRESS

**Next Exercise:** MP01.2.2-Q9

**Last Updated:** 24 November 2026
