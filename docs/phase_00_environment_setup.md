
# Phase 00 — Python Environment Setup

## 1. Gambaran Umum (Overview)
Pada Phase 00, saya mempersiapkan lingkungan pengembangan (*development environment*) untuk mendukung pembelajaran Python for Data Analysis.

Fokus utama fase ini adalah memahami instalasi Python, penggunaan Python Interpreter, pengelolaan package menggunakan pip, pembuatan Virtual Environment, serta konfigurasi Visual Studio Code (VS Code).

Saya juga melakukan pengujian untuk memastikan bahwa Python dapat menjalankan program melalui terminal dan file `.py`.

Tujuan dari fase ini bukan hanya menyelesaikan instalasi, tetapi juga memahami fungsi setiap komponen agar mampu mengidentifikasi dan menyelesaikan kendala konfigurasi secara mandiri.

## 2. Development Environment (Lingkungan Pengembangan)
Berikut adalah perangkat lunak dan komponen yang digunakan selama Phase 00.

| Komponen | Konfigurasi |
|---|---|
| Sistem operasi | Windows 64-bit |
| Python | 3.15.2 |
| Package Manager | pip 26.2.2 |
| Code Editor | Visual Studio Code |
| Python Extension | Python (Microsoft) |
| Terminal | Git Bash dan PowerShell |
| Version Control | Git |
| Repository | `python-data-analysis-learning` |
| Virtual Environment | `.venv` |
| Library yang diuji | Pandas 3.1.0 dan NumPy 2.5.4 |

Seluruh pengujian utama dilakukan pada direktori repository `python-data-analysis-learning` dengan menggunakan Virtual Environment yang terpisah dari instalasi Python global.

## 3. Python Installation & Validation
Pada tahap ini, saya melakukan pemeriksaan instalasi Python melalui Windows Command Prompt dan Git Bash.

### 3.1 Memeriksa Versi Python

Perintah yang digunakan:

```bash
python --version
```

Hasil pengujian:

```text
Python 3.15.2
```

Hasil tersebut menunjukkan bahwa Python sudah terinstal dan dapat diakses melalui terminal.

### 3.2 Memeriksa Lokasi Python Interpreter

Untuk mengetahui lokasi Python Interpreter yang terdeteksi oleh Windows, saya menjalankan:

```bash
where.exe python
```

Hasil pengujian:

```text
C:\Users\lenovo\AppData\Local\Programs\Python\Python315\python.exe
C:\Users\lenovo\AppData\Local\Microsoft\WindowsApps\python.exe
```

Lokasi pertama merupakan instalasi Python yang digunakan. Sementara itu, lokasi pada `WindowsApps` berkaitan dengan mekanisme *App Execution Alias* Windows.

### 3.3 Memahami Python Interpreter

Python Interpreter merupakan program yang menjalankan instruksi Python.

Saya juga menggunakan perintah berikut untuk mengetahui interpreter yang sedang digunakan:

```bash
python -c "import sys; print(sys.executable)"
```

Perintah tersebut membantu membedakan penggunaan Python global dengan Python yang berada di dalam Virtual Environment.

### 3.4 Kesimpulan Validasi

Berdasarkan hasil pemeriksaan, Python 3.15.2 telah terinstal dan dapat dijalankan melalui terminal.

Saya juga memahami bahwa lokasi Python Interpreter dapat berbeda bergantung pada konfigurasi environment yang sedang aktif.

## 4. Python Package Manager (pip)

### 4.1 Mengenal pip

`pip` merupakan Package Manager yang digunakan untuk menginstal, memperbarui, dan mengelola package Python.

Package memungkinkan saya menggunakan fungsi atau library tambahan tanpa harus membuat seluruh komponennya dari awal.

### 4.2 Memeriksa Versi pip

Perintah yang digunakan:

```bash
python -m pip --version
```

Hasil pemeriksaan menunjukkan bahwa pip versi **26.2.2** telah tersedia.

### 4.3 Perbedaan pip dan python -m pip

Kedua perintah berikut dapat digunakan untuk menjalankan pip:

```bash
pip --version
```

```bash
python -m pip --version
```

Perbedaannya terletak pada cara pemanggilan pip.

- `pip` menjalankan executable pip yang ditemukan melalui konfigurasi `PATH`.
- `python -m pip` menjalankan modul pip menggunakan Python Interpreter yang dipanggil melalui perintah `python`.

Saya memilih menggunakan `python -m pip` untuk mengurangi risiko menjalankan pip dari instalasi Python yang berbeda.

### 4.4 Mengenal Dependency

Dalam pengelolaan package, saya mempelajari dua jenis dependency:

**Direct dependency:** Package yang secara langsung dibutuhkan oleh package tertentu.

**Transitive dependency:** Package yang dibutuhkan oleh dependency lainnya.

Sebagai contoh, ketika menginstal Pandas, pip juga menginstal NumPy, python-dateutil, dan tzdata. Package `six` ikut terinstal sebagai dependency dari python-dateutil.

### 4.5 Memahami Dry Run

Saya juga mempelajari penggunaan opsi `--dry-run`.

Contoh:

```bash
python -m pip install --dry-run pandas
```

Opsi tersebut digunakan untuk melihat rencana instalasi tanpa benar-benar memasang package.

### 4.6 Kesimpulan

Saya memahami bahwa Package Manager membantu mengelola library dan dependency Python. Penggunaan `python -m pip` juga membantu memastikan bahwa pip dijalankan melalui interpreter yang dipilih.

## 5. Virtual Environment (.venv)

### 5.1 Mengenal Virtual Environment

Virtual Environment merupakan lingkungan Python terisolasi yang digunakan untuk mengelola package dan dependency pada suatu proyek.

Saya menggunakan Virtual Environment agar package yang diinstal untuk pembelajaran Python for Data Analysis tidak tercampur dengan package pada instalasi Python global.

Virtual Environment yang digunakan dalam repository ini bernama `.venv`.

### 5.2 Membuat Virtual Environment

Saya membuat Virtual Environment menggunakan modul standar Python `venv`.

Perintah:

```bash
python -m venv .venv
```

Perintah tersebut membuat direktori `.venv` yang berisi Python Interpreter dan komponen pendukung lingkungan virtual.

### 5.3 Mengaktifkan Virtual Environment

Pada Git Bash, saya menggunakan:

```bash
source .venv/Scripts/activate
```

Setelah aktivasi berhasil, terminal menampilkan indikator:

```text
(.venv)
```

Indikator tersebut membantu mengenali bahwa Virtual Environment sedang aktif.

### 5.4 Memvalidasi Python Interpreter

Untuk memastikan interpreter yang digunakan, saya menjalankan:

```bash
python -c "import sys; print(sys.executable)"
```

Hasil ketika Virtual Environment aktif:

```text
C:\Users\lenovo\python-data-analysis-learning\.venv\Scripts\python.exe
```

Hasil ini berbeda dengan lokasi Python global:

```text
C:\Users\lenovo\AppData\Local\Programs\Python\Python315\python.exe
```

Dengan membandingkan kedua lokasi tersebut, saya dapat memastikan interpreter yang digunakan dalam terminal.

### 5.5 Memeriksa Environment Variable

Pada Git Bash, saya juga menggunakan:

```bash
echo "$VIRTUAL_ENV"
```

Ketika `.venv` aktif, hasilnya menunjukkan direktori Virtual Environment:

```text
/c/Users/lenovo/python-data-analysis-learning/.venv
```

### 5.6 Mengabaikan Virtual Environment dari Git

Direktori `.venv` tidak perlu dimasukkan ke repository Git karena berisi file environment lokal dan package yang dapat diinstal kembali.

Saya memvalidasi aturan `.gitignore` menggunakan:

```bash
git check-ignore -v .venv/pyvenv.cfg
```

Hasil pemeriksaan:

```text
.gitignore:155:.venv    .venv/pyvenv.cfg
```

Hasil tersebut menunjukkan bahwa file dalam `.venv` telah tercakup dalam aturan pengabaian Git.

### 5.7 Kesimpulan

Saya berhasil membuat, mengaktifkan, dan memvalidasi Virtual Environment.

Saya juga memahami bahwa memilih interpreter di VS Code dan mengaktifkan environment melalui terminal merupakan dua mekanisme yang berkaitan, tetapi tidak selalu identik.

Keberhasilan aktivasi dapat diverifikasi dengan memeriksa lokasi interpreter menggunakan `sys.executable`.

## 6. Package Installation & Validation Python

### 6.1 Instalasi Pandas

Pada tahap ini, saya menginstal Pandas sebagai salah satu library utama untuk pembelajaran Python for Data Analysis.

Instalasi dilakukan melalui Virtual Environment `.venv` menggunakan perintah:

```bash
python -m pip install pandas
```

Hasil instalasi menunjukkan bahwa package berikut berhasil terpasang:

| Package | Versi |
|---|---|
| pandas | 3.1.0 |
| numpy | 2.5.4 |
| python-dateutil | 3.0.0 |
| six | 1.17.0 |
| tzdata | 2026.6 |

NumPy, python-dateutil, dan tzdata terinstal sebagai dependency Pandas, sedangkan six merupakan dependency dari python-dateutil.

### 6.2 Memeriksa Informasi Package

Untuk memeriksa metadata Pandas, saya menggunakan:

```bash
python -m pip show pandas
```

Hasil pemeriksaan menunjukkan bahwa Pandas versi 3.1.0 terinstal di dalam direktori:

```text
C:\Users\lenovo\python-data-analysis-learning\.venv\Lib\site-packages
```

Lokasi tersebut memastikan bahwa Pandas terinstal pada Virtual Environment proyek.

### 6.3 Memvalidasi Import Pandas

Saya kemudian menguji apakah Pandas dapat diimpor melalui Python Interpreter:

```bash
python -c "import pandas; print(pandas.__version__)"
```

Hasil:

```text
3.1.0
```

Pengujian ini menunjukkan bahwa Pandas dapat diimpor tanpa menghasilkan error.

### 6.4 Pengujian Fungsional Sederhana

Untuk melakukan pengujian lebih lanjut, saya membuat sebuah Pandas Series:

```bash
python -c "import pandas as pd; data = pd.Series([10, 20, 30]); print(data)"
```

Hasil:

```text
0    10
1    20
2    30
dtype: int64
```

Pengujian tersebut menunjukkan bahwa Pandas berhasil membuat dan menampilkan Series sederhana dengan tipe data integer 64-bit.

### 6.5 Kesimpulan

Saya berhasil menginstal dan memvalidasi Pandas di dalam Virtual Environment.

Saya juga memahami perbedaan antara pemeriksaan metadata package menggunakan `pip show`, pengujian import, dan pengujian fungsional sederhana.

Pengujian ini memastikan bahwa fungsi dasar Pandas yang dicoba dapat berjalan, tetapi belum mencakup pengujian seluruh fitur Pandas.

## 7. VS Code Configuration

### 7.1 Instalasi Python Extension

Saya menggunakan Visual Studio Code (VS Code) sebagai Code Editor untuk pembelajaran Python.

Untuk mendukung pengembangan Python, saya menginstal Python Extension dari Microsoft.

Extension tersebut menyediakan dukungan seperti pemilihan Python Interpreter, menjalankan program Python, dan integrasi dengan fitur debugging.

### 7.2 Memilih Python Interpreter

Melalui Command Palette, saya menjalankan:

`Python: Select Interpreter`

Kemudian memilih interpreter:

`.venv (3.15.2) — ./.venv/Scripts/python.exe`

Tujuannya adalah agar VS Code menggunakan Python Interpreter yang berada di dalam Virtual Environment proyek.

### 7.3 Konfigurasi Terminal

Saya memeriksa dua pengaturan berikut:

| Pengaturan | Nilai |
|---|---|
| Python: Terminal Activate Environment | Aktif |
| Python Environments: Terminal Auto Activation Type | `command` |

Pengaturan tersebut mendukung proses aktivasi Virtual Environment ketika terminal baru dibuka melalui VS Code.

### 7.4 Perbedaan Git Bash Standalone dan Integrated Terminal

Selama pengujian, saya menemukan bahwa Git Bash yang dibuka secara terpisah masih menggunakan Python global.

Namun, ketika membuka Git Bash melalui Integrated Terminal VS Code, perintah aktivasi Virtual Environment dijalankan secara otomatis:

```bash
source /C/Users/lenovo/python-data-analysis-learning/.venv/Scripts/activate
```

Saya memvalidasi interpreter menggunakan:

```bash
python -c "import sys; print(sys.executable)"
```

Hasilnya menunjukkan lokasi interpreter di dalam `.venv`.

Dari pengujian tersebut, saya memahami bahwa konfigurasi terminal pada VS Code tidak otomatis berlaku untuk aplikasi Git Bash yang dijalankan secara terpisah.

### 7.5 Pengujian PowerShell Integrated Terminal

Selain Git Bash, saya juga menguji PowerShell melalui Integrated Terminal VS Code.

Virtual Environment diaktifkan menggunakan skrip `Activate.ps1`.

Pengujian `sys.executable` menunjukkan bahwa PowerShell juga berhasil menggunakan interpreter dari `.venv`.

### 7.6 Terminal Shell Integration dan Python Debugger

Saya menemukan informasi terminal mengenai Shell Integration serta kontribusi extension Git, Python, dan Python Debugger.

Terdapat pemberitahuan bahwa Python Debugger ingin melakukan *relaunch terminal* agar fitur debugging tambahan dapat digunakan.

Pemberitahuan tersebut bukan error instalasi Python. Karena interpreter dan Virtual Environment sudah berfungsi, saya tidak melakukan perubahan konfigurasi tambahan.

### 7.7 Kesimpulan

Saya berhasil mengonfigurasi VS Code untuk menggunakan Virtual Environment proyek.

Saya juga memahami bahwa pemilihan interpreter pada Code Editor dan aktivasi environment pada terminal merupakan mekanisme yang berbeda, meskipun keduanya dapat mengarah ke interpreter Python yang sama.

## 8. Python Script Execution

### 8.1 Membuat File Python

Setelah menyelesaikan konfigurasi environment, saya membuat file `hello.py` pada direktori utama repository.

File tersebut digunakan untuk menguji apakah Python dapat menjalankan instruksi yang ditulis melalui VS Code.

Kode awal yang saya gunakan:

```python
print("Hello, Python!")
print("saya sedang belajar Python for Data Analysis")
```

### 8.2 Menjalankan Program

Saya menjalankan file melalui Git Bash Integrated Terminal menggunakan perintah:

```bash
python hello.py
```

Hasil pengujian:

```text
Hello, Python!
saya sedang belajar Python for Data Analysis
```

Program berhasil dijalankan tanpa error.

### 8.3 Memahami Fungsi print()

Melalui praktik ini, saya mempelajari bahwa fungsi `print()` digunakan untuk menampilkan nilai atau hasil evaluasi ekspresi ke standard output.

Saya juga melakukan eksperimen dengan operasi matematika:

```python
print(10 + 20)
```

Hasil:

```text
30
```

Dari eksperimen tersebut, saya memahami bahwa Python mengevaluasi ekspresi `10 + 20` terlebih dahulu, kemudian fungsi `print()` menampilkan hasilnya.

### 8.4 Mengenal Perbedaan Integer dan String

Saya mulai mempelajari perbedaan antara nilai numerik dan teks.

Contohnya:

```python
print(10 + 20)
print("10 + 20")
```

Kode pertama melakukan operasi penjumlahan, sedangkan kode kedua menampilkan teks.

Pembahasan Data Types dan Operators akan dipelajari lebih mendalam pada Phase 01 — Python Programming Fundamentals.

### 8.5 Kesimpulan

Saya berhasil membuat, menyimpan, dan menjalankan file Python `.py` menggunakan VS Code.

Pengujian ini menjadi validasi akhir bahwa Python Interpreter, Virtual Environment, dan Integrated Terminal telah siap digunakan untuk pembelajaran berikutnya.

## 9. Troubleshooting & Lessons Learned

Selama Phase 00, saya menemukan beberapa kondisi yang membantu saya memahami hubungan antara Python Interpreter, Virtual Environment, terminal, dan konfigurasi VS Code.

### 9.1 Python Global Masih Digunakan pada Git Bash

**Kondisi:**

Ketika membuka Git Bash secara terpisah dari VS Code, perintah berikut masih menunjukkan lokasi Python global:

```bash id="1sf3tk"
python -c "import sys; print(sys.executable)"
```

Hasil:

```text id="gxt7je"
C:\Users\lenovo\AppData\Local\Programs\Python\Python315\python.exe
```

**Pemeriksaan:**

Saya membandingkan hasil tersebut dengan interpreter yang digunakan setelah mengaktifkan Virtual Environment secara manual.

```bash id="0cfu8t"
source .venv/Scripts/activate
```

Setelah aktivasi, `sys.executable` menunjukkan lokasi Python di dalam `.venv`.

**Kesimpulan:**

Git Bash standalone tidak otomatis menggunakan Virtual Environment hanya karena terminal berada di direktori proyek.

### 9.2 Aktivasi Otomatis pada VS Code

**Kondisi:**

Awalnya saya menduga terdapat masalah pada konfigurasi aktivasi otomatis Virtual Environment.

**Pemeriksaan:**

Saya memeriksa pengaturan Python Extension dan memastikan bahwa `Terminal Activate Environment` telah aktif.

Kemudian saya melakukan pengujian menggunakan Git Bash Integrated Terminal di VS Code.

**Hasil:**

VS Code menjalankan perintah aktivasi Virtual Environment, dan `sys.executable` menunjukkan interpreter di dalam `.venv`.

**Kesimpulan:**

Aktivasi otomatis pada VS Code berhasil. Perbedaan hasil pengujian sebelumnya disebabkan oleh penggunaan lingkungan terminal yang berbeda.

### 9.3 Notifikasi Python Debugger

**Kondisi:**

Pada PowerShell Integrated Terminal, terdapat pemberitahuan bahwa Python Debugger ingin melakukan relaunch terminal.

**Analisis:**

Pemberitahuan tersebut berkaitan dengan integrasi fitur debugging, bukan kegagalan instalasi Python.

Karena Python Interpreter dan Virtual Environment telah berfungsi, saya tidak melakukan perubahan konfigurasi tambahan.

### 9.4 Pembelajaran Penting

Beberapa hal yang saya pelajari dari proses troubleshooting:

1. Memeriksa kondisi sistem sebelum mengubah konfigurasi.
2. Mengubah satu variabel pada satu waktu agar penyebab masalah lebih mudah diidentifikasi.
3. Membedakan working directory dengan Python Interpreter yang sedang digunakan.
4. Menggunakan `sys.executable` untuk memvalidasi interpreter.
5. Membedakan Git Bash standalone dengan Integrated Terminal VS Code.
6. Memahami bahwa tidak semua notifikasi merupakan error yang harus segera diperbaiki.

### 9.5 Kesimpulan

Melalui proses troubleshooting, saya belajar bahwa keberhasilan konfigurasi tidak cukup dinilai dari tampilan terminal saja.

Saya perlu melakukan pengujian yang sesuai untuk memastikan bahwa komponen yang digunakan benar-benar bekerja sebagaimana diharapkan.

## 10. Final Validation & Checkpoint

### 10.1 Ringkasan Hasil Validasi

Pada akhir Phase 00, saya melakukan evaluasi terhadap seluruh komponen development environment yang telah dikonfigurasi.

| Komponen | Hasil |
|---|---|
| Python 3.15.2 | Berhasil diinstal dan dijalankan |
| pip 26.2.2 | Berhasil divalidasi |
| Virtual Environment `.venv` | Berhasil dibuat dan diaktifkan |
| Python Interpreter | Berhasil divalidasi melalui `sys.executable` |
| Pandas 3.1.0 | Berhasil diinstal dan diimpor |
| Pandas Series | Berhasil dibuat dan ditampilkan |
| VS Code Python Extension | Berhasil dikonfigurasi |
| Git Bash Integrated Terminal | Berhasil menggunakan `.venv` |
| PowerShell Integrated Terminal | Berhasil menggunakan `.venv` |
| `.gitignore` | Berhasil mengabaikan direktori `.venv` |
| Eksekusi file `hello.py` | Berhasil tanpa error |

### 10.2 Kompetensi yang Dipelajari

Setelah menyelesaikan Phase 00, saya telah mempelajari dasar-dasar:

1. Instalasi dan validasi Python.
2. Penggunaan Python Interpreter.
3. Pengelolaan package menggunakan pip.
4. Pembuatan dan aktivasi Virtual Environment.
5. Perbedaan Python global dengan Python dalam `.venv`.
6. Konfigurasi Python Extension pada VS Code.
7. Penggunaan Git Bash dan PowerShell Integrated Terminal.
8. Validasi package melalui metadata, import, dan pengujian fungsional.
9. Menjalankan file Python `.py`.
10. Troubleshooting dasar pada development environment.

### 10.3 Status Phase 00

**Status: Seluruh pengujian teknis utama berhasil.**

Development environment telah siap digunakan untuk pembelajaran Python for Data Analysis.

Penyelesaian administratif Phase 00 dilakukan melalui pemeriksaan dokumentasi dan sinkronisasi repository GitHub.

### 10.4 Rencana Pembelajaran Berikutnya

Tahap berikutnya adalah:

**Phase 01 — Python Programming Fundamentals**

Fokus pembelajaran akan mencakup dasar-dasar sintaks Python, Variables, Data Types, Operators, Control Flow, Functions, dan materi lain sesuai roadmap pembelajaran.

Proses pembelajaran akan tetap menggunakan pendekatan teori, praktik mandiri, latihan, dan evaluasi pemahaman.

### 10.5 Refleksi Pembelajaran

Phase 00 membantu saya memahami bahwa menyiapkan development environment bukan hanya tentang menginstal aplikasi.

Saya juga perlu memahami hubungan antara Python Interpreter, Package Manager, Virtual Environment, Code Editor, dan terminal.

Pemahaman tersebut menjadi fondasi agar saya dapat belajar Python secara lebih mandiri dan sistematis.