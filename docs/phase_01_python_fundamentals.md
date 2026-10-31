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

#### 1.2.1 Compilation and Interpretation

#### 1.2.3 Constant Folding vs Variable Addition

#### 1.2.4 Evaluation and Lessons Learned