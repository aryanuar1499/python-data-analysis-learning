# Phase 01 — Python Programming Fundamentals

## 1. Gambaran Umum (Overview)

Phase 01 berfokus pada pemahaman fundamental bahasa pemrograman Python sebagai dasar untuk mempelajari Data Analysis.

Pembelajaran dilakukan secara bertahap melalui teori, praktik langsung, latihan mandiri, evaluasi pemahaman, dan dokumentasi GitHub.

Materi mencakup pengenalan Python, proses eksekusi program, syntax, variables, data types, operators, control flow, functions, dan konsep fundamental lainnya sesuai roadmap Python for Data Analysis.

Tujuan utama phase ini adalah membangun kemampuan memahami, menulis, menjalankan, dan melakukan debugging kode Python secara mandiri sebelum mempelajari library untuk analisis data.


## 2. Introduction to Python Programming

### 2.1 What Is Python?

Python merupakan high-level, general-purpose programming language yang dirancang dengan syntax relatif mudah dibaca dan dipahami manusia.

#### High-Level Programming Language

High-level berarti bahasa pemrograman memiliki tingkat abstraksi yang tinggi dari instruksi mesin dan detail pengelolaan hardware.

Karakteristik ini memungkinkan programmer lebih fokus pada logika program daripada pengelolaan instruksi mesin secara langsung.

#### General-Purpose Programming Language

General-purpose berarti bahasa pemrograman dapat digunakan untuk berbagai kebutuhan, seperti:

- Data Analysis
- Machine Learning
- Web Development
- Automation

Dalam pembelajaran Python for Data Analysis, Python digunakan sebagai fondasi untuk melakukan data processing, data manipulation, dan data analysis.

#### Kesimpulan

High-level menjelaskan tingkat abstraksi bahasa pemrograman, sedangkan general-purpose menjelaskan luasnya bidang penggunaan bahasa tersebut.


### 2.2 How Python Works

Python merupakan programming language yang umumnya dijalankan menggunakan interpreter.

CPython, sebagai implementasi Python yang paling umum digunakan, melibatkan proses compilation dan interpretation dalam menjalankan program.

#### Python Execution Process

Alur eksekusi program Python secara sederhana:

1. **Source Code (.py)**

   Programmer menulis instruksi Python dalam file dengan ekstensi `.py`.

2. **Compilation**

   CPython melakukan parsing dan compilation terhadap source code untuk menghasilkan bytecode.

   Pada tahap ini, compiler juga dapat melakukan optimasi tertentu, seperti constant folding.

3. **Python Bytecode**

   Bytecode merupakan representasi instruksi internal Python yang akan dijalankan oleh Python Virtual Machine.

   Bytecode berbeda dari machine code karena tidak dieksekusi langsung oleh prosesor.

4. **Python Virtual Machine (PVM)**

   PVM merupakan bagian dari runtime CPython yang menjalankan instruksi bytecode.

   Proses ini memungkinkan instruksi Python menghasilkan operasi yang dijalankan oleh komputer.

5. **Program Output**

   Jika program memiliki instruksi untuk menampilkan hasil, output dapat ditampilkan melalui terminal atau media lainnya.

#### Compilation vs Interpretation

Compilation merupakan proses penerjemahan source code menjadi representasi lain, seperti bytecode.

Interpretation merupakan proses menjalankan instruksi program melalui interpreter atau runtime.

CPython menggunakan kedua mekanisme tersebut.

#### Kesimpulan

Python tidak hanya menjalankan source code secara langsung tanpa compilation.

Pada CPython, source code dikompilasi menjadi bytecode, kemudian bytecode dijalankan melalui Python Virtual Machine.

### 2.3 Python Bytecode Inspection

#### Tujuan Praktik

Mengamati bytecode yang dihasilkan CPython menggunakan modul `dis` (Disassembler) dari Python Standard Library.

Environment yang digunakan:

- Python 3.15.2
- Virtual Environment: `.venv`
- Terminal: Git Bash
- Repository: `python-data-analysis-learning`

#### Experiment 01 — Constant Folding

Source code yang dianalisis:

```python
print(10 + 20)
```

Perintah terminal:

```bash
python -c "import dis; dis.dis('print(10 + 20)')"
```

Actual output:

```text
0           RESUME                   0

1           LOAD_NAME                0 (print)
            PUSH_NULL
            LOAD_SMALL_INT          30
            CALL                     1
            RETURN_VALUE
```

#### Analisis Hasil

Hasil bytecode menunjukkan bahwa ekspresi `10 + 20` telah disederhanakan menjadi `30`.

Proses ini disebut **Constant Folding**, yaitu optimasi compiler terhadap ekspresi yang seluruh operand-nya merupakan nilai konstan.

Instruksi `LOAD_SMALL_INT 30` menunjukkan bahwa CPython memuat nilai integer `30` tanpa perlu menjalankan operasi penjumlahan tersebut ketika bytecode dieksekusi.

#### Kesimpulan Experiment 01

CPython dapat melakukan optimasi selama compilation.

Eksperimen ini membuktikan bahwa source code tidak selalu diterjemahkan menjadi instruksi bytecode yang identik dengan setiap operasi yang ditulis programmer.

#### Experiment 02 — Variable Addition

Eksperimen ini bertujuan untuk mengamati bagaimana CPython menghasilkan bytecode ketika operasi penjumlahan menggunakan variabel.

Source code yang dianalisis:

```python
a = 10
b = 20
print(a + b)
```

Perintah terminal:

```bash
python -c "import dis; dis.dis('a = 10\nb = 20\nprint(a + b)')"
```

Actual output pada Python 3.15.2:

```text
0           RESUME                   0

1           LOAD_SMALL_INT          10
            STORE_NAME               0 (a)

2           LOAD_SMALL_INT          20
            STORE_NAME               1 (b)

3           LOAD_NAME                2 (print)
            PUSH_NULL
            LOAD_NAME                0 (a)
            LOAD_NAME                1 (b)
            BINARY_OP                0 (+)
            CALL                     1
            POP_TOP
            LOAD_COMMON_CONSTANT     7 (None)
            RETURN_VALUE
```

#### Analisis Experiment 02

Berdasarkan hasil bytecode, terdapat beberapa instruksi penting:

1. `LOAD_SMALL_INT` digunakan untuk memuat nilai integer 10 dan 20.
2. `STORE_NAME` digunakan untuk menyimpan nilai pada variabel `a` dan `b`.
3. `LOAD_NAME` digunakan untuk mengambil nilai variabel ketika dibutuhkan.
4. `BINARY_OP (+)` menunjukkan bahwa operasi penjumlahan dilakukan saat runtime.
5. `CALL` digunakan untuk memanggil fungsi `print()`.

Berbeda dari Experiment 01, CPython tidak melakukan constant folding terhadap ekspresi `a + b`.

Meskipun nilai awal variabel telah ditentukan, compiler tetap menghasilkan instruksi untuk mengambil nilai variabel dan melakukan penjumlahan ketika program dieksekusi.

#### Comparison — Constant Folding vs Variable Addition

| Aspek | Constant Folding | Variable Addition |
|---|---|---|
| Source code | `print(10 + 20)` | `a = 10; b = 20; print(a + b)` |
| Operasi | Ekspresi konstan | Ekspresi menggunakan variabel |
| Bytecode utama | `LOAD_SMALL_INT 30` | `LOAD_NAME` dan `BINARY_OP (+)` |
| Waktu penjumlahan | Compilation | Runtime |
| Hasil program | 30 | 30 |

#### Kesimpulan Experiment 02

Hasil eksperimen menunjukkan bahwa CPython dapat menghasilkan instruksi bytecode yang berbeda meskipun dua program memberikan output yang sama.

Constant folding memungkinkan compiler menyederhanakan ekspresi konstan, sedangkan variable addition memerlukan pengambilan nilai variabel dan operasi penjumlahan saat runtime.

Pemahaman ini membantu menjelaskan perbedaan antara compilation, optimization, dan execution dalam Python.

## 01.1.3 — Python Syntax Fundamentals

### A. Konsep Dasar
Python syntax adalah seperangkat aturan yang menentukan bagaimana
kode Python harus ditulis agar dapat dipahami oleh interpreter.

Konsep dasar yang telah dipelajari:

1. **Syntax**: Aturan penulisan kode Python.
2. **Indentation**: Penggunaan spasi untuk menentukan blok kode,
   misalnya pada statement `if`.
3. **Variable Assignment**: Mengikat nama variabel ke suatu nilai
   menggunakan operator `=`.
4. **Variable Reassignment**: Mengikat ulang nama variabel ke nilai
   yang baru.
5. **Comments**: Catatan pada source code menggunakan simbol `#`
   yang tidak dieksekusi sebagai instruksi Python.
6. **SyntaxError**: Error ketika kode melanggar aturan syntax Python.
7. **Runtime Error**: Error yang terjadi ketika program sedang
   dieksekusi, contohnya `ZeroDivisionError`.

### B. Praktik dan Hasil Pengujian

#### 1. Variable Assignment dan Reassignment

```python
nilai = 5
print("Nilai awal:", nilai)

nilai = nilai + 10
print("Nilai setelah reassignment:", nilai)
```

Output:

```text
Nilai awal: 5
Nilai setelah reassignment: 15
```

**Hasil analisis:**

Variabel `nilai` awalnya mengacu pada integer `5`.
Statement `nilai = nilai + 10` menghitung nilai baru,
kemudian mengikat ulang variabel `nilai` ke integer `15`.

#### 2. Python Comments

```python
angka = 20
# angka = 50

print("Nilai angka:", angka)

# print("Baris ini tidak dieksekusi")
```

Output:

```text
Nilai angka: 20
```

**Hasil analisis:**

Baris yang diawali `#` merupakan komentar dan tidak
dieksekusi oleh Python. Oleh karena itu, nilai `angka`
tetap `20`.

#### 3. Python Indentation

```python
angka = 10

if angka > 5:
    print("Kondisi pertama terpenuhi")
    print("Masih di dalam if")

print("Di luar if")
```

Output:

```text
Kondisi pertama terpenuhi
Masih di dalam if
Di luar if
```

**Hasil analisis:**

Python menggunakan indentation untuk menentukan blok kode.

Ketika kondisi `if` bernilai `True`, statement di dalam blok
dieksekusi. Statement di luar blok tetap dieksekusi.

Jika kondisi bernilai `False`, statement di dalam blok
dilewati, tetapi statement di luar blok tetap dieksekusi.

#### 4. Syntax Error dan Runtime Error

**Syntax Error**

```python
if True:
print("Hello")
```

Kode tersebut menghasilkan `IndentationError` karena
statement di dalam blok `if` tidak memiliki indentation.

**Runtime Error**

```python
print("Program dimulai")
hasil = 10 / 0
print("Program selesai")
```

Output:

```text
Program dimulai
ZeroDivisionError: division by zero
```

**Hasil analisis:**

- `SyntaxError` terjadi ketika kode melanggar aturan syntax Python.
- `IndentationError` merupakan turunan dari `SyntaxError`.
- `ZeroDivisionError` terjadi ketika program mencoba melakukan
  pembagian dengan nol.
- Pada runtime error yang tidak ditangani, statement sebelum
  error dapat dieksekusi, sedangkan statement setelah error
  tidak dijalankan.

## Lesson 01.1.4 — Variables and Data Types

### 1. Variables and Dynamic Typing
**Variables**

Variable adalah nama yang digunakan untuk merujuk suatu objek atau nilai dalam Python. Variable dibuat menggunakan assignment operator (`=`).

```python
stok = 100
nama_produk = "Beras"
```

**Dynamic Typing**

Python merupakan bahasa pemrograman dengan sistem *Dynamic Typing*, yaitu tipe data ditentukan berdasarkan objek yang dirujuk saat program berjalan (*runtime*), tanpa perlu mendeklarasikan tipe variabel secara eksplisit.

```python
nilai = 100
print(type(nilai))  # <class 'int'>

nilai = "Seratus"
print(type(nilai))  # <class 'str'>
```

**Key Takeaways**

- Variable merupakan nama yang merujuk pada objek.
- Assignment (`=`) mengikat nama variabel ke objek.
- Reassignment dapat mengubah objek yang dirujuk variabel.
- Python menentukan tipe data objek saat runtime.
- `print()` menampilkan nilai yang dirujuk variabel ketika fungsi tersebut dipanggil.

### 2. Python Built-in Data Types
Python menyediakan berbagai *Built-in Data Types* untuk merepresentasikan jenis data yang berbeda.

| Data Type | Description | Example |
|---|---|---|
| `int` | Bilangan bulat (*Integer*) | `100`, `-5`, `0` |
| `float` | Bilangan floating-point | `10.5`, `0.0`, `-2.5` |
| `str` | Urutan karakter (*String*) | `"Python"`, `"100"` |
| `bool` | Nilai Boolean | `True`, `False` |

**Example:**

```python
stok = 100
harga = 12500.50
nama_produk = "Beras"
tersedia = True
```

**Key Takeaways**

- `int` digunakan untuk merepresentasikan bilangan bulat.
- `float` digunakan untuk merepresentasikan bilangan floating-point.
- `str` digunakan untuk merepresentasikan teks.
- `bool` digunakan untuk merepresentasikan nilai kebenaran.
- Nilai `100` dan `"100"` memiliki tipe data berbeda meskipun terlihat serupa.
- Pemilihan tipe data yang tepat penting untuk memastikan operasi dan analisis data menghasilkan informasi yang sesuai.

### 3. Type Inspection with type()
Fungsi bawaan Python `type()` digunakan untuk mengetahui tipe data suatu objek.

**Syntax:**

```python
type(object)
```

**Example:**

```python
stok = 100
harga = 12500.50
nama_produk = "Beras"
tersedia = True

print(type(stok))
print(type(harga))
print(type(nama_produk))
print(type(tersedia))
```

**Expected Output:**

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

**Key Takeaways**

- `type()` digunakan untuk memeriksa tipe data objek.
- `type()` mengembalikan objek tipe, bukan string biasa.
- `print(type(variable))` menampilkan representasi tipe data objek yang dirujuk variabel.
- Pemeriksaan tipe data membantu proses debugging dan data validation.
- Dalam Python yang menggunakan Dynamic Typing, tipe objek yang dirujuk variabel dapat berbeda setelah reassignment.

**Catatan Penting**

ada sebuah perbedaan seperti berikut:

```python
angka = 100

print(type(angka))
print(type(angka) == int)
```

**Expected Output:**
```text
<class 'int'>
True
```

### 4. Type Conversion
**Type Conversion**

Type Conversion adalah proses mengonversi suatu nilai dari satu tipe data ke tipe data lainnya.

Python menyediakan beberapa built-in functions untuk melakukan konversi tipe data, antara lain:

| Function | Purpose | Example |
|---|---|---|
| `int()` | Mengonversi nilai menjadi integer | `int("100")` → `100` |
| `float()` | Mengonversi nilai menjadi floating-point | `float("10.5")` → `10.5` |
| `str()` | Mengonversi nilai menjadi string | `str(100)` → `"100"` |
| `bool()` | Mengonversi nilai berdasarkan aturan truth value testing | `bool(0)` → `False` |

**Important Concepts**

- Type Conversion memungkinkan nilai digunakan dalam operasi yang membutuhkan tipe data tertentu.
- Tidak semua nilai dapat dikonversi ke setiap tipe data.
- Konversi yang tidak valid dapat menghasilkan error, seperti `ValueError`.
- Konversi tidak otomatis mengubah objek asli yang dirujuk oleh variabel.
- Hasil konversi dapat disimpan menggunakan variable assignment.

**Example:**

```python
stok_text = "100"
stok_integer = int(stok_text)

print(stok_text, type(stok_text))
print(stok_integer, type(stok_integer))
```

**Expected Output:**

```text
100 <class 'str'>
100 <class 'int'>
```

**Key Takeaway**

Memahami Type Conversion penting dalam Data Analysis karena data yang diperoleh dari berbagai sumber belum tentu memiliki tipe data yang sesuai untuk proses perhitungan dan analisis.

#### 4.1 int()
**Integer Type Conversion — `int()`**

Fungsi `int()` digunakan untuk mengonversi nilai yang sesuai menjadi tipe data integer (`int`).

**Syntax:**

```python
int(value)
```

**Example 1 — String to Integer**

```python
stok = "15000"
hasil = int(stok)

print(hasil)
print(type(hasil))
```

**Expected Output:**

```text
15000
<class 'int'>
```

**Example 2 — String Repetition vs Numeric Multiplication**

```python
stok = "15000"

print(stok * 3)
print(int(stok) * 3)
```

**Expected Output:**

```text
150001500015000
45000
```

**Example 3 — Invalid Conversion**

```python
int("12500.50")
```

**Result:**

`ValueError`, karena string `"12500.50"` bukan representasi integer yang valid untuk konversi langsung menggunakan `int()`.

**Key Takeaways**

- `int()` dapat mengonversi string berisi representasi bilangan bulat menjadi integer.
- String dan integer memiliki perilaku operasi yang berbeda.
- Operator `*` pada string dan integer menghasilkan operasi yang berbeda ketika dikombinasikan dengan integer.
- `int()` tidak dapat langsung mengonversi string desimal seperti `"12500.50"`.
- Konversi tipe data penting sebelum melakukan perhitungan numerik.

#### 4.2 float()
**Float Type Conversion — `float()`**

Fungsi `float()` digunakan untuk mengonversi nilai yang sesuai menjadi tipe data floating-point (`float`).

**Syntax:**

```python
float(value)
```

**Example 1 — String to Float**

```python
harga = "12500.50"
harga_float = float(harga)

print(harga_float)
print(type(harga_float))
```

**Expected Output:**

```text
12500.5
<class 'float'>
```

**Example 2 — Numeric Calculation**

```python
harga = "12500.50"

total_harga = float(harga) * 2

print(total_harga)
print(type(total_harga))
```

**Expected Output:**

```text
25001.0
<class 'float'>
```

**Example 3 — Integer to Float**

```python
stok = 100

print(float(stok))
```

**Expected Output:**

```text
100.0
```

**Key Takeaways**

- `float()` dapat mengonversi string numerik yang valid menjadi floating-point.
- `float()` juga dapat mengonversi integer menjadi floating-point.
- Nilai bertipe `float` dapat digunakan untuk perhitungan numerik.
- Konversi `float()` tidak otomatis mengubah tipe data variabel asal.
- Floating-point memiliki keterbatasan presisi karena representasi bilangan dalam komputer. Hal ini penting diperhatikan dalam perhitungan keuangan dan

#### 4.3 str()
**String Type Conversion — `str()`**

Fungsi `str()` digunakan untuk mengonversi suatu objek menjadi representasi string (`str`).

**Syntax:**

```python
str(object)
```

**Example 1 — Integer to String**

```python
stok = 100

stok_string = str(stok)

print(stok_string)
print(type(stok_string))
```

**Expected Output:**

```text
100
<class 'str'>
```

**Example 2 — Numeric Addition vs String Concatenation**

```python
stok_awal = 100
stok_masuk = 50

hasil_a = stok_awal + stok_masuk
hasil_b = str(stok_awal) + str(stok_masuk)

print(hasil_a, type(hasil_a))
print(hasil_b, type(hasil_b))
```

**Expected Output:**

```text
150 <class 'int'>
10050 <class 'str'>
```

**Explanation:**

- `hasil_a` menggunakan operasi penjumlahan numerik (*Numeric Addition*).
- `hasil_b` menggunakan penggabungan string (*String Concatenation*).
- Operator `+` memiliki perilaku berbeda tergantung tipe data operand.
- Konversi menggunakan `str()` tidak mengubah tipe data variabel asal.

**Example 3 — Boolean to String**

```python
tersedia = True

print(str(tersedia))
print(type(str(tersedia)))
```

**Expected Output:**

```text
True
<class 'str'>
```

**Key Takeaways**

- `str()` menghasilkan representasi string dari suatu objek.
- Angka yang dikonversi menjadi string tidak lagi diperlakukan sebagai nilai numerik dalam operasi `+`.
- Operator `+` pada dua string melakukan concatenation, bukan penjumlahan.
- String dapat digunakan untuk menyusun teks, label, dan informasi laporan.
- Dalam Data Analysis, penting membedakan data numerik dengan data yang hanya terlihat seperti angka tetapi disimpan sebagai string.

#### 4.4 bool()
**Boolean Type Conversion — `bool()`**

Fungsi `bool()` digunakan untuk mengonversi suatu nilai menjadi Boolean (`True` atau `False`) berdasarkan aturan *Truth Value Testing* dalam Python.

**Syntax:**

```python
bool(value)
```

**1. Numeric Truthiness**

Untuk tipe data numerik, nilai nol dianggap `False`, sedangkan nilai selain nol dianggap `True`, termasuk angka negatif.

```python
print(bool(0))
print(bool(25))
print(bool(-10))
print(bool(0.0))
```

**Expected Output:**

```text
False
True
True
False
```

**2. String Truthiness**

Untuk tipe data string, Python memeriksa apakah string tersebut kosong atau tidak.

```python
print(bool(""))
print(bool("False"))
print(bool("0"))
print(bool(" "))
```

**Expected Output:**

```text
False
True
True
True
```

String `"False"` menghasilkan `True` karena berisi karakter. Python tidak menafsirkan teks tersebut sebagai nilai Boolean `False`.

**3. Boolean vs Business Logic**

Hasil konversi Boolean tidak selalu sama dengan kondisi yang ingin diperiksa dalam suatu proses bisnis.

Contoh pada manajemen persediaan:

```python
stok = -5

print(bool(stok))
print(stok > 0)
```

**Expected Output:**

```text
True
False
```

**Explanation:**

- `bool(stok)` menghasilkan `True` karena `-5` bukan nol.
- `stok > 0` menghasilkan `False` karena `-5` tidak lebih besar dari nol.
- Untuk memeriksa ketersediaan stok positif, ekspresi `stok > 0` lebih sesuai daripada `bool(stok)`.
- Stok negatif dapat menjadi indikasi masalah pencatatan yang memerlukan pemeriksaan lebih lanjut.

**4. Type Conversion Does Not Change the Original Variable**

```python
stok = -5

print(bool(stok))
print(stok)
print(type(stok))
```

**Expected Output:**

```text
True
-5
<class 'int'>
```

**Key Takeaways**

- `bool()` menghasilkan `True` atau `False` berdasarkan aturan Truth Value Testing.
- Nilai numerik nol dianggap `False`, sedangkan nilai numerik selain nol dianggap `True`.
- String kosong dianggap `False`, sedangkan string tidak kosong dianggap `True`.
- *Truthiness* berbeda dari aturan bisnis (*Business Logic*).
- Konversi menggunakan `bool()` tidak otomatis mengubah nilai maupun tipe data variabel asal.
- Pemahaman Boolean penting dalam conditional statements, data validation, dan data analysis.

**Learning Status:** Theory and evaluation completed. Hands-on Boolean practice pending.

### 5. Practice and Experiments
**Practice and Experiments — Variables, Data Types, and Type Conversion**

**Practice File:** `practice/02_python_data_types.py`

**Objective:**

Memahami penggunaan variabel, tipe data dasar, pemeriksaan tipe data, serta konversi nilai menggunakan Python.

**Experiments Completed:**

| Experiment | Concept | Status |
|---|---|---|
| 1 | Integer (`int`) and Float (`float`) | Completed |
| 2 | Variable Assignment and Reassignment | Completed |
| 3 | Dynamic Typing | Completed |
| 4 | Type Inspection using `type()` | Completed |
| 5 | Integer Conversion using `int()` | Completed |
| 6 | Float Conversion using `float()` | Completed |
| 7 | String Conversion using `str()` | Completed |
| 8 | Boolean Conversion using `bool()` | Pending |

**Validated Experiment — Numeric Addition vs String Concatenation**

```python id="qk7s9a"
stok_awal = 100
stok_masuk = 50

hasil_a = stok_awal + stok_masuk
hasil_b = str(stok_awal) + str(stok_masuk)

print(hasil_a, type(hasil_a))
print(hasil_b, type(hasil_b))
```

**Actual Output:**

```text id="e2n6jw"
150 <class 'int'>
10050 <class 'str'>
```

**Observation:**

Penjumlahan dua integer menghasilkan nilai numerik, sedangkan penggabungan dua string menghasilkan concatenation.

**Next Practice:**

Melakukan eksperimen `bool()` terhadap nilai numerik, string kosong, string tidak kosong, serta membandingkan hasil *Truthiness* dengan *Business Logic*.

**Learning Status:** In Progress — Boolean hands-on practice pending.

### 6. Evaluation and Key Takeaways
**Evaluation — Variables and Data Types**

Evaluasi dilakukan melalui pertanyaan konseptual, prediksi output, serta eksperimen langsung menggunakan Python.

**Concepts Evaluated:**

| Topic | Evaluation Result |
|---|---|
| Variable Assignment and Reassignment | Passed |
| Dynamic Typing | Passed |
| Basic Data Types (`int`, `float`, `str`, `bool`) | Passed |
| Type Inspection using `type()` | Passed |
| Integer Conversion using `int()` | Passed |
| Float Conversion using `float()` | Passed |
| String Conversion using `str()` | Passed |
| Numeric Truthiness | Passed |
| String Truthiness | Passed |
| Comparison Operators (`>`, `>=`) | Passed |
| Boolean Hands-on Practice | Pending |

**Key Takeaways**

1. Python menggunakan Dynamic Typing, sehingga tipe data tidak perlu dideklarasikan secara eksplisit ketika membuat variabel.
2. Variable Assignment mengikat nama variabel ke objek, sedangkan Reassignment dapat mengubah objek yang dirujuk.
3. Fungsi `type()` digunakan untuk memeriksa tipe data suatu objek.
4. Fungsi `int()`, `float()`, `str()`, dan `bool()` digunakan untuk melakukan Type Conversion.
5. Operator yang sama dapat menghasilkan perilaku berbeda tergantung tipe data operand.
6. Boolean Truthiness mengikuti aturan bahasa Python dan tidak selalu sama dengan Business Logic.
7. Prediksi output perlu diverifikasi melalui eksekusi kode agar pemahaman teori dapat diuji secara langsung.
8. Dokumentasi pembelajaran perlu membedakan Expected Output dan Actual Output.

**Current Learning Status**

- Phase 01 — Python Programming Fundamentals: In Progress
- Lesson 01.1.4 — Variables and Data Types: Completed
- Theory and Conceptual Evaluation: Completed
- Boolean Hands-on Practice: COMPLETED
- Final Lesson Evaluation: PASSED

### Final Evaluation — Lesson 01.1.4
**Status:** COMPLETED  
**Evaluation Date:** 2026-11-05

#### Topics Evaluated

- Variables, Assignment, and Reassignment
- Dynamic Typing and Object References
- Built-in Data Types: `int`, `float`, `str`, and `bool`
- Type Conversion and Type Inspection
- String Repetition vs Numeric Multiplication
- Boolean Truthiness and Comparison Operators
- Basic Inventory Availability Logic

#### Evaluation Findings

1. Successfully predicted Python outputs involving variables, data types, and Boolean expressions.
2. Demonstrated understanding of the difference between type conversion and variable reassignment after corrective exercises.
3. Distinguished string repetition from numeric multiplication.
4. Correctly applied comparison operators to inventory availability and demand fulfillment.
5. Identified arithmetic accuracy as an area requiring continued practice.

#### Code Validation

- Syntax Validation: PASSED
- Runtime Execution: PASSED
- Full Output Verification: NOT PERFORMED

#### Key Takeaways

Python variables reference objects, and reassignment can change which object a variable references. Type conversion produces a value of the requested type without automatically modifying the original variable.

Boolean truthiness and comparison operations serve different purposes. Business decisions should use explicit conditions that reflect the intended business rules.

**Final Evaluation Result: PASSED**

**Lesson Status: COMPLETED — Pending GitHub Commit**

---

## Lesson 01.1.5 — Python Operators and Expressions

**Status:** IN PROGRESS
**Learning Method:** Theory → Intensive Practice → Exercises → Evaluation → Documentation

### 01.1.5.1 — Operators and Operands

**Status:** COMPLETED

#### Theory Summary

**Operator** adalah simbol atau kata kunci (*keyword*) yang digunakan untuk melakukan suatu operasi terhadap satu atau lebih operand.

**Operand** adalah nilai (*value*), variabel (*variable*), atau ekspresi (*expression*) yang menjadi objek dari operasi yang dilakukan oleh operator.

**Expression** adalah kombinasi nilai, variabel, dan operator yang dievaluasi oleh Python untuk menghasilkan suatu nilai (*result*).

#### Example

```python
a = 12
b = 4

result = a / b
print(result)
```

#### Code Example

```python
a = 12
b = 4

result = a / b
print(result)
print(type(result))
```

#### Expected Output

```text
3.0
<class 'float'>
```

#### Key Takeaways

- Operator `/` digunakan untuk melakukan True Division.
- Variabel `a` dan `b` merupakan operand dalam ekspresi `a / b`.
- Ekspresi `a / b` dievaluasi oleh Python untuk menghasilkan suatu nilai.
- Pada contoh tersebut, hasil pembagian adalah `3.0` dengan tipe data `float`, meskipun kedua operand bertipe `int`.

### 01.1.5.2 — Floor Division (`//`)

**Status:** COMPLETED

#### Theory Summary

**Floor Division** adalah operasi pembagian menggunakan operator `//` yang menghasilkan hasil bagi dengan pembulatan ke bawah (*floor*), yaitu menuju negatif tak hingga (*negative infinity*).

Floor Division berbeda dengan **True Division (`/`)** dan **Truncation (`int()`)**.

- **True Division (`/`)** menghasilkan nilai pembagian dalam bentuk `float` untuk operand numerik biasa.
- **Floor Division (`//`)** menghasilkan hasil pembagian yang dibulatkan ke bawah.
- **Truncation (`int()`)** menghilangkan bagian desimal dari nilai numerik hingga mendekati nol (*toward zero*).

Perbedaan Floor Division dan Truncation menjadi penting ketika hasil pembagian bernilai negatif.

#### Experiment — Floor Division vs Truncation

**Objective:** Memahami perbedaan hasil True Division, Floor Division, dan Truncation ketika menggunakan bilangan negatif.

**Code:**

```python
a = -11
b = 4

print(a / b)
print(a // b)
print(int(a / b))
```

**Validated Output:**

```text
-2.75
-3
-2
```

#### Experiment Findings

1. True Division (`/`) menghasilkan `-2.75` dengan tipe data `float`.
2. Floor Division (`//`) menghasilkan `-3` karena Python melakukan pembulatan ke bawah menuju negatif tak hingga.
3. Truncation menggunakan `int()` menghasilkan `-2` karena bagian desimal dihilangkan menuju nol.
4. Floor Division dan Truncation dapat menghasilkan nilai berbeda ketika hasil pembagian bernilai negatif.

**Validation Status:** PASSED

### 01.1.5.3 — Modulo Operator (`%`)

**Status:** COMPLETED

#### Theory Summary

**Modulo Operator (`%`)** adalah operator aritmetika Python yang digunakan untuk memperoleh sisa hasil pembagian (*remainder*) dari dua operand.

Modulo memiliki hubungan matematis dengan **Floor Division (`//`)**, yang dapat dinyatakan melalui persamaan:

`a = (a // b) * b + (a % b)`

Keterangan:
- `a` adalah bilangan yang dibagi (*dividend*).
- `b` adalah bilangan pembagi (*divisor*).
- `a // b` adalah hasil Floor Division (*quotient*).
- `a % b` adalah sisa pembagian (*remainder*).

Dalam Python, ketika hasil Modulo tidak sama dengan nol, tanda hasilnya mengikuti tanda pembagi (*divisor*).

Dengan demikian, Modulo dapat menghasilkan nilai positif maupun negatif, bergantung pada tanda pembaginya.

#### Experiment 03 — Positive Modulo

**Objective:** Memahami hubungan antara Floor Division (`//`) dan Modulo (`%`) menggunakan bilangan positif.

**Code:**

```python
a = 29
b = 8

print(a // b)
print(a % b)
print((a // b) * b + (a % b))
```

**Validated Output:**

```text
3
5
29
```

#### Experiment Findings

1. Floor Division (`29 // 8`) menghasilkan `3`.
2. Modulo (`29 % 8`) menghasilkan sisa pembagian sebesar `5`.
3. Persamaan `29 = (3 * 8) + 5` membuktikan hubungan matematis antara Floor Division dan Modulo.
4. Hasil eksperimen sesuai dengan prediksi dan berhasil divalidasi menggunakan Python Interactive Shell.

**Validation Status:** PASSED

#### Experiment 04 — Negative Modulo

**Objective:** Memahami perilaku Floor Division dan Modulo ketika dividend bernilai negatif.

**Code:**

```python
a = -23
b = 6

print(a % b)
print(a // b)
print((a // b) * b + (a % b))
```

**Validated Output:**

```text
1
-4
-23
```

#### Experiment Findings

1. Floor Division (`-23 // 6`) menghasilkan `-4` karena pembulatan dilakukan menuju negatif tak hingga.
2. Modulo (`-23 % 6`) menghasilkan `1` karena pembaginya bernilai positif.
3. Persamaan `-23 = (-4 * 6) + 1` membuktikan hubungan antara Floor Division dan Modulo.
4. Hasil eksperimen sesuai dengan prediksi dan telah divalidasi melalui Python Interactive Shell.

**Validation Status:** PASSED

#### Final Evaluation — Negative Divisor

**Objective:** Memahami perilaku Floor Division dan Modulo ketika divisor bernilai negatif.

**Code:**

```python
a = 17
b = -5

print(a // b)
print(a % b)
```

**Predicted Output:**

```text
-4
-3
```

#### Mathematical Verification

Floor Division:

17 / -5 = -3.4

Karena Floor Division menggunakan pembulatan menuju negatif tak hingga:

17 // -5 = -4

Modulo:

17 = (-4 * -5) + (-3)

17 = 20 - 3

17 = 17

#### Evaluation Findings

1. Floor Division menghasilkan `-4` karena menggunakan pembulatan ke bawah.
2. Modulo menghasilkan `-3` karena pembaginya bernilai negatif.
3. Hubungan matematis antara Floor Division dan Modulo berhasil dibuktikan.
4. Prediksi hasil operasi sudah benar berdasarkan evaluasi matematis.

**Mathematical Validation:** PASSED

**Runtime Validation:** PASSED

**Final Evaluation Result:** PASSED

---

### 01.1.5.4 — Comparison Operators

#### Learning Objectives

1. Memahami konsep dasar Comparison Operators dalam Python.
2. Memahami hasil operasi perbandingan dalam bentuk Boolean.
3. Memahami perbedaan Equality dan Identity.
4. Menerapkan Comparison Operators dalam aturan bisnis.
5. Melakukan Boundary Testing terhadap kondisi persediaan.
6. Mengimplementasikan perbandingan menggunakan Loop, Nested List, dan Nested Loop.

#### Theory Summary

Comparison Operators merupakan operator yang digunakan untuk membandingkan dua operand. Pada perbandingan nilai numerik standar, hasil operasi berupa Boolean (`True` atau `False`).

| Operator | Description |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

#### Experiment — Equality Operator

**Objective:** Memahami perbandingan kesamaan nilai antara dua operand.

**Code Example:**

```python
a = 10
b = 10
c = 20

print(a == b)
print(a == c)
```

**Expected Output:**

```text
True
False
```

#### Experiment Findings

1. Operator `==` membandingkan kesamaan nilai.
2. Jika kedua operand memiliki nilai yang sama, hasilnya adalah `True`.
3. Jika kedua operand memiliki nilai berbeda, hasilnya adalah `False`.
4. Operator `==` berbeda dengan operator assignment (`=`).

#### Experiment — Equality vs Identity

**Objective:** Memahami perbedaan perbandingan nilai dan identitas objek.

**Code Example:**

```python
a = [10, 20]
b = [10, 20]
c = a

print(a == b)
print(a is b)
print(a is c)
```

**Expected Output:**

```text
True
False
True
```

#### Experiment Findings

1. Operator `==` membandingkan kesamaan nilai atau isi objek.
2. Operator `is` membandingkan identitas objek.
3. Dua objek dapat memiliki nilai yang sama tetapi identitas yang berbeda.
4. Assignment `c = a` membuat kedua variabel merujuk pada objek yang sama.
5. Operator `is` termasuk Identity Operators, bukan operator perbandingan nilai.

#### Experiment — Not Equal Operator

**Objective:** Memahami perbandingan ketidaksamaan nilai.

**Code Example:**

```python
a = 10
b = 20

print(a != b)
print(a != 10)
```

**Expected Output:**

```text
True
False
```

#### Experiment Findings

1. Operator `!=` menghasilkan `True` ketika kedua nilai berbeda.
2. Operator `!=` menghasilkan `False` ketika kedua nilai sama.
3. Pada perbandingan numerik standar, operator `!=` merupakan kebalikan dari operator `==`.

#### Experiment — Greater Than Operator

**Objective:** Memahami perbandingan nilai yang lebih besar.

**Code Example:**

```python
current_stock = 25
minimum_stock = 20

print(current_stock > minimum_stock)
print(20 > minimum_stock)
```

**Expected Output:**

```text
True
False
```

#### Experiment Findings

1. Operator `>` menghasilkan `True` apabila operand sebelah kiri lebih besar daripada operand sebelah kanan.
2. Kondisi dengan nilai yang sama menghasilkan `False`.
3. Operator ini dapat digunakan untuk membandingkan nilai aktual dengan batas tertentu.

#### Experiment — Less Than Operator

**Objective:** Memahami perbandingan nilai yang lebih kecil.

**Code Example:**

```python
current_stock = 15
minimum_stock = 20

print(current_stock < minimum_stock)
print(20 < minimum_stock)
```

**Expected Output:**

```text
True
False
```

#### Experiment Findings

1. Operator `<` menghasilkan `True` apabila operand sebelah kiri lebih kecil daripada operand sebelah kanan.
2. Kondisi dengan nilai yang sama menghasilkan `False`.
3. Operator ini dapat digunakan untuk mengidentifikasi persediaan di bawah batas minimum.

#### Experiment — Greater Than or Equal To Operator

**Objective:** Memahami perbandingan yang mencakup kondisi lebih besar dan kondisi sama dengan.

**Code Example:**

```python
minimum_stock = 20

print(19 >= minimum_stock)
print(20 >= minimum_stock)
print(21 >= minimum_stock)
```

**Expected Output:**

```text
False
True
True
```

#### Experiment Findings

1. Operator `>=` mencakup kondisi lebih besar dan sama dengan.
2. Nilai yang tepat berada pada batas perbandingan menghasilkan `True`.
3. Pemilihan operator `>` atau `>=` harus disesuaikan dengan aturan bisnis.

**Runtime Validation:** PASSED

#### Experiment — Less Than or Equal To Operator

**Objective:** Memahami perbandingan yang mencakup kondisi lebih kecil dan kondisi sama dengan.

**Code Example:**

```python
minimum_stock = 20

print(19 <= minimum_stock)
print(20 <= minimum_stock)
print(21 <= minimum_stock)
```

**Expected Output:**

```text
True
True
False
```

#### Experiment Findings

1. Operator `<=` mencakup kondisi lebih kecil dan sama dengan.
2. Nilai yang tepat berada pada batas perbandingan menghasilkan `True`.
3. Operator ini dapat digunakan untuk mengidentifikasi kebutuhan replenishment ketika persediaan mencapai atau berada di bawah batas minimum.

**Runtime Validation:** PASSED

#### Boolean Result Review

Comparison Operators dapat menghasilkan nilai Boolean yang digunakan sebagai dasar pengambilan keputusan dalam program.

**Code Example:**

```python
current_stock = 20
minimum_stock = 20

result = current_stock <= minimum_stock

print(result)
print(type(result))
```

**Expected Output:**

```text
True
<class 'bool'>
```

#### Key Takeaways

1. Hasil perbandingan numerik standar merupakan Boolean.
2. Nilai Boolean dapat disimpan dalam variabel.
3. Nilai Boolean dapat digunakan untuk merepresentasikan kondisi bisnis.
4. Comparison Operators merupakan salah satu dasar Conditional Statements dan Logical Expressions.

#### Final Evaluation — Comparison Operators & Business Rules

**Objective:** Menerapkan Comparison Operators untuk mengevaluasi kondisi persediaan berdasarkan aturan bisnis.

**Business Parameters:**

| Parameter | Value |
|---|---:|
| Minimum Stock | 20 |
| Maximum Stock | 100 |

**Business Rules:**

| Business Condition | Expression |
|---|---|
| Replenishment Alert | `current_stock <= minimum_stock` |
| Overstock Alert | `current_stock > maximum_stock` |
| At Maximum Capacity | `current_stock == maximum_stock` |

**Code:**

```python
current_stock = 20
minimum_stock = 20
maximum_stock = 100

print(current_stock <= minimum_stock)
print(current_stock > maximum_stock)
print(current_stock == maximum_stock)
```

**Expected Output:**

```text
True
False
False
```

#### Evaluation Findings

1. Replenishment Alert bernilai `True` karena persediaan berada tepat pada batas minimum.
2. Overstock Alert bernilai `False` karena persediaan tidak melebihi kapasitas maksimum.
3. At Maximum Capacity bernilai `False` karena persediaan belum mencapai kapasitas maksimum.
4. Pemilihan Comparison Operators harus didasarkan pada definisi aturan bisnis.

#### Boundary Testing

**Objective:** Menguji ketepatan aturan bisnis pada nilai di bawah, tepat pada, dan di atas batas perbandingan.

**Test Parameters:**

```python
minimum_stock = 20
maximum_stock = 100

stock_values = [19, 20, 21, 99, 100, 101]
```

**Boundary Testing Results:**

| Current Stock | Replenishment Alert | Overstock Alert | At Maximum Capacity |
|---:|---|---|---|
| 19 | True | False | False |
| 20 | True | False | False |
| 21 | False | False | False |
| 99 | False | False | False |
| 100 | False | False | True |
| 101 | False | True | False |

#### Boundary Testing Findings

1. Replenishment Alert aktif ketika persediaan berada di bawah atau tepat pada batas minimum.
2. Overstock Alert hanya aktif ketika persediaan melebihi batas maksimum.
3. At Maximum Capacity hanya aktif ketika persediaan tepat pada batas maksimum.
4. Persediaan yang berada tepat pada kapasitas maksimum tidak dikategorikan sebagai Overstock.
5. Boundary Testing membantu mengidentifikasi kesalahan pemilihan operator pada nilai batas.

**Boundary Testing Status:** PASSED

#### Step 22 — Final Runtime Validation

**Objective:** Memvalidasi seluruh kondisi Boundary Testing secara otomatis menggunakan `for` loop.

**Code:**

```python
minimum_stock = 20
maximum_stock = 100

stock_values = [19, 20, 21, 99, 100, 101]

for stock in stock_values:
    print("Current Stock:", stock)
    print("Replenishment Alert:", stock <= minimum_stock)
    print("Overstock Alert:", stock > maximum_stock)
    print("At Maximum Capacity:", stock == maximum_stock)
    print()
```

#### Runtime Validation Findings

1. Program melakukan enam iterasi berdasarkan jumlah elemen pada `stock_values`.
2. Setiap iterasi mengevaluasi tiga aturan bisnis.
3. Program menghasilkan 18 hasil evaluasi Boolean.
4. Hasil Runtime Validation sesuai dengan hasil Boundary Testing.
5. Penggunaan Loop mengurangi kebutuhan penulisan perbandingan secara berulang.

**Runtime Validation Status:** PASSED

#### Additional Runtime Experiment — Nested Loop

**Objective:** Mengembangkan implementasi Comparison Operators menggunakan Nested List dan Nested Loop untuk merepresentasikan beberapa kondisi bisnis secara terstruktur.

**Code:**

```python
minimum_stock = 20
maximum_stock = 100

stock_values = [19, 20, 21, 99, 100, 101]

for stock in stock_values:
    print("Current Stock:", stock)

    alerts = [
        ["Replenishment Alert", stock <= minimum_stock],
        ["Overstock Alert", stock > maximum_stock],
        ["At Maximum Capacity", stock == maximum_stock]
    ]

    for alert in alerts:
        print(alert[0] + ":", alert[1])
        print()
```

#### Nested List Structure

Setiap elemen pada `alerts` merupakan sebuah List yang terdiri dari dua elemen:

| Index | Description | Data Type |
|---|---|---|
| 0 | Alert Name | `str` |
| 1 | Comparison Result | `bool` |

Sebagai contoh, ketika `stock = 19`, struktur data `alerts` adalah:

```python
[
    ["Replenishment Alert", True],
    ["Overstock Alert", False],
    ["At Maximum Capacity", False]
]
```

#### Nested Loop Execution

1. Outer Loop melakukan iterasi terhadap setiap nilai persediaan.
2. List `alerts` dibentuk kembali pada setiap iterasi Outer Loop.
3. Setiap elemen `alerts` menyimpan nama kondisi bisnis dan hasil perbandingan.
4. Inner Loop melakukan iterasi terhadap setiap elemen `alerts`.
5. `alert[0]` mengakses nama kondisi bisnis.
6. `alert[1]` mengakses hasil perbandingan dalam bentuk Boolean.

| Component | Total Iterations |
|---|---:|
| Outer Loop | 6 |
| Inner Loop per Outer Iteration | 3 |
| Total Inner Loop Iterations | 18 |

#### Additional Experiment — Nested List Indexing and Length

**Objective:** Memahami struktur setiap elemen pada Nested List melalui Indexing dan fungsi `len()`.

**Code:**

```python
minimum_stock = 20
maximum_stock = 100

stock_values = [19, 20, 21, 99, 100, 101]

for stock in stock_values:
    print("Current Stock:", stock)

    alerts = [
        ["Replenishment Alert", stock <= minimum_stock],
        ["Overstock Alert", stock > maximum_stock],
        ["At Maximum Capacity", stock == maximum_stock]
    ]

    for alert in alerts:
        print("Alert:", alert)
        print("Length:", len(alert))
        print("Index 0:", alert[0])
        print("Index 1:", alert[1])
        print()
```

**Validated Output — Current Stock: 19:**

```text
Current Stock: 19
Alert: ['Replenishment Alert', True]
Length: 2
Index 0: Replenishment Alert
Index 1: True

Alert: ['Overstock Alert', False]
Length: 2
Index 0: Overstock Alert
Index 1: False

Alert: ['At Maximum Capacity', False]
Length: 2
Index 0: At Maximum Capacity
Index 1: False
```

#### Additional Experiment Findings

1. Setiap elemen `alert` memiliki panjang dua elemen.
2. Index `0` menyimpan nama kondisi bisnis.
3. Index `1` menyimpan hasil evaluasi Comparison Operators.
4. Nested Loop memungkinkan program mengakses setiap kondisi bisnis secara terstruktur.
5. Comparison Operators dapat dikombinasikan dengan List, Nested List, dan Loop untuk mendukung pengolahan data.
6. Implementasi ini merupakan dasar pengembangan logika analisis persediaan menggunakan Python.

**Additional Runtime Validation:** PASSED

#### Key Learning Outcomes

1. Memahami enam Comparison Operators utama dalam Python.
2. Memahami perbedaan Equality dan Identity.
3. Memahami hasil perbandingan dalam bentuk Boolean.
4. Memahami pentingnya pemilihan operator berdasarkan aturan bisnis.
5. Memahami konsep Boundary Testing.
6. Menerapkan Comparison Operators dalam Inventory Business Rules.
7. Mengimplementasikan Runtime Validation menggunakan Loop.
8. Mengembangkan struktur evaluasi menggunakan Nested List dan Nested Loop.

#### Final Evaluation Status

| Evaluation Component | Status |
|---|---|
| Comparison Operators Theory | PASSED |
| Practical Exercises | PASSED |
| Final Evaluation | PASSED |
| Boundary Testing | PASSED |
| Final Runtime Validation | PASSED |
| Additional Runtime Experiment | PASSED |
| GitHub Documentation | IN PROGRESS |

**Final Evaluation Result:** PASSED

**Lesson Status:** IN PROGRESS — GitHub Documentation

**Next Lesson:** 01.1.5.5 — Logical Operators

#### 1.2.1 Compilation and Interpretation

#### 1.2.3 Constant Folding vs Variable Addition

#### 1.2.4 Evaluation and Lessons Learned