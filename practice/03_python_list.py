# # Python Lists
# # Practice 01 — Creating and Appending Elements

# numbers = []

# for x in range(3, 8):
#     numbers.append(x)

# print(numbers)

# # Practice 02

# numbers = []

# for x in range(2, 6):
#     numbers.append(x**2)

# print(numbers)

# # Practice 03

# numbers = []

# for x in range(5):
#     numbers.append(x**3)

# print(numbers)
# # karena tidak dalam satu blok maka print() di eksekusi satu kali setelah loop selesai

# # Practice 04 — Observing List Changes

# numbers = []

# for x in range(3, 8):
#     numbers.append(x)
#     print(numbers)
# # karena print() di dalam satu blok maka dieksekusi setiap iterasi, yaitu 5 kali iterasi
# """"
# Jadi, indentasi dalam python bukan sekedar untuk merapikan kode, tetapi untuk menentukan
# instruksi mana yang termasuk dalam suatu blok
# """

# # Practice 05

# numbers = []

# for x in range(1, 4):
#     numbers.append(x)
#     print(x)

# print(numbers)

# # Practice 06
# numbers = []

# for x in range(1, 4):
#     print(x)

# print(numbers)

# # Practice 07

# numbers = []

# for x in range(5):
#     numbers.append(x**3)

# print(numbers[3])

# # Practice 08

# numbers = []

# for x in range(10):
#     numbers.append(x**3)

# print(numbers)
# print(numbers[1:8:2])

# # Practice 09

# numbers = [5, 10, 15, 20, 25]

# selected = numbers[2:5]

# numbers = [100, 200, 300]

# print(selected)
# print(numbers)

# # Practice 10

# numbers = [5, 10, 15, 20, 25]

# print(numbers)

# numbers[1] = 50

# print(numbers)

# # Practice 11

# numbers = [10, 20, 30, 40, 50]

# selected = numbers

# numbers[2] = 100

# print(selected)
# print(numbers)

# # Practice 12
# # Assigment Vs Copy

# numbers = [10, 20, 30, 40]

# selected = numbers.copy()

# numbers[1] = 200

# print(selected)
# print(numbers)

# #Practice 13
# #.append Vs .extend

# numbers = [5, 10]

# numbers.append([15, 20])
# numbers.extend([25, 30])

# print(numbers)

# # #Practice 13.2
# # #percobaan untuk mendapatkan dua hasil yang berbeda -failed

# # numbers = [5, 10]

# # numbers.append([15, 20])

# # print(numbers)

# # numbers.extend([25, 30])

# # print(numbers)

# # # Practice 13.3
# # # percobaan untuk mendapatkan dua hasi yang berbeda -failed

# # numbers = [5, 10]

# # numbers.append([15, 20])

# # selected = numbers.copy()

# # numbers.extend([25, 30])

# # print(numbers)
# # print(selected)

# # Practice 13.4
# # percobaan untuk mendapatkan dua hasi yang berbeda -failed

# numbers = [5, 10]

# selected = numbers.copy()

# numbers.append([15, 20])
# selected.extend([25, 30])

# print(numbers)
# print(selected)

# # Practice 14
# # .insert()
# # tambahan sintax untuk mengetahui proses perubahan selected = numbers.copy()

# numbers = [10, 20, 30, 40]


# selected = numbers.copy()
# numbers.insert(1, 100)

# print(selected)
# print(numbers)

# # Practice 15
# # .remove

# numbers = [5, 10, 15, 10, 20, 25]

# numbers.remove(10)

# print(selected)
# print(numbers)

# # Practice 15.2
# # .remove menghapus seluruh nilai yang sama dengan looping (while)

# numbers = [5, 10, 15, 10, 20, 25]

# selected = numbers.copy()

# while 10 in numbers:
#     numbers.remove(10)

# print(selected)
# print(numbers)

# # Practice 15.3
# # .remove menghapus seluruh nilai yang sama dengan List Comprehension

# numbers = [5, 10, 15, 10, 20, 25]

# numbers = [x for x in numbers if x != 10]

# print(numbers)

# # Practice 16
# # .pop menghapus element berdasarkan indeks sekaligus mengembalikan element yang di hapus

# numbers = [10, 20, 30, 40]

# removed = numbers.pop(1)

# print(numbers)
# print(removed)

# # Practice 16.2

# numbers = [5, 10, 15, 20, 25]

# first_removed = numbers.pop()
# second_removed = numbers.pop()

# print(numbers)
# print(first_removed)
# print(second_removed)

# # Practice 17
# # .clear() yaitu menghapus seluruh
# #  elemen pada sebuah list, tanpa menghapus objek list itu sendiri

# numbers = [10, 20, 30, 40]

# selected = numbers.copy()

# numbers.clear()

# print(numbers)
# print(selected)

# # Practice 18
# # .index() berfungsi mencari posisi
# #  sebuah indeks dari kemunculan pertama suatu nilai di dalam list

# numbers = [5, 10, 15, 10, 20, 25]

# position = numbers.index(20)

# print(position)
# print(numbers)

# # Practice 19
# # .count() digunakan untuk menghitung 
# # berapa kali suatu nilai muncul di dalam sebuah list

# numbers = [5, 10, 15, 10, 20, 10, 25]

# total_a = numbers.count(10)
# total_b = numbers.count(30)

# print(total_a)
# print(total_b)
# print(numbers)

# # Practice 20
# # .sort() digunakan untuk mengurutkan 
# # elemen dalam sebuah list (ascending order)
# # reverse=True merupakan argument untuk methode .sort(), 
# # bukan pemanggilan methode .reverse()

# numbers = [35, 10, 50, 20, 40]

# selected = numbers.copy()

# numbers.sort()
# selected.sort(reverse=True)

# print(numbers)
# print(selected)

# # Practice 21
# # .reverse() digunakan untuk membalikkan
# #  urutan posisi elemen dalam sebuah list

# numbers = [25, 10, 40, 15, 30]

# selected = numbers.copy()

# numbers.reverse()
# selected.sort(reverse=True)

# print(numbers)
# print(selected)

# # Practice 22
# # .len() digunakan untuk mengtahui 
# # jumlah elemen dalam sebuah list, lalu menghitung elemen 
# # yang ada tingkat terluat list, bukan jumlah seluruh nilai di dalam list nested-list

# numbers = [5, 10, [15, 20], 25, 10]

# total_elements = len(numbers)
# total_tens = numbers.count(10)

# print(total_elements)
# print(total_tens)
# print(numbers)

# # Practice 23
# # in dan not in, in ini memeriksa 
# # apakah suatu nilai terdapat di dalam sebuah list 
# # not in sebaliknya yaitu memeriksa apakah suatu nilai tidak terdapat pada sebuah list

# numbers = [10, 20, [30, 40], 50]

# print(20 in numbers)
# print(30 in numbers)
# print([30, 40] in numbers)
# print(60 not in numbers)

# # Practice 24
# # del merupakan statment python yang 
# # dapat digunakan untuk menghapus sebuah elemen berdasarkan indeks

# numbers = [5, 10, 15, 20, 25, 30]

# selected = numbers.copy()

# del numbers[1:4]

# print(numbers)
# print(selected)

# # Practice 25
# # List Comprehension yaitu sintaks
# # python untuk membuat list baru dari sebuah iterable

# numbers = [x * 3 for x in range(1, 5)]

# print(numbers)

# Practice 26
# List Comprehension with conditional if 
# untuk memilih elemen tertentu sebelum dimasukkan ke list baru

# #for and .append()
# even_numbers = []

# for x in numbers:
#     if x % 2 == 0:
#         even_numbers.append(x)

# numbers = [5, 10, 15, 20, 25, 30]

# selected = [x for x in numbers if x > 15]

# print(selected)
# print(numbers)

# # Practice 26.2
# numbers = [5, 10, 15, 20, 25, 30]

# selected = [x * 2 for x in numbers if x > 15]

# print(selected)

# # Practice 26.3
# numbers = [5, 10, 15, 20, 25, 30, 35, 40]

# selected = [x * 2 for x in numbers if x >= 15 and x < 35]

# print(selected)
# print(numbers)

# # Practice 27
# # if-else didalam List Comprehension 
# # untuk menentukan nilai berdasarkan suatu kondisi

# numbers = [10, 15, 20, 25, 30]

# selected = [x * 2 if x >= 20 else x for x in numbers]

# print(selected)
# print(numbers)

# # Practice 28
# # Evaluasi Q36 — Independent Coding Exercise

# # mengambil nilai stock < 10
# stock = [5, 12, 8, 20, 3, 15, 10]

# low_stock = [x for x in stock if x < 10]

# print(low_stock)
# print(stock)

# # Practice 29
# # Nested List yaitu sebuah elemen list 
# # yang di dalam nya terdapat list lagi sebagai elemennya

# stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# print(stock[1][2])

# # Practice 29.2
# # mengubah elemen dalam Nested List yaitu menggunakan index assigment

# # Practice 30
# # iterasi pada nested list mempelajari 
# # bagaimana mengakses setiap inner list menggunakan perulangan for

# stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# for row in stock:
#     print(row)

# stock = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]

# for row in stock:
#     print(row[1])

# stock = [
#     [5, 10, 15],
#     [20, 25, 30],
#     [35, 40, 45]
# ]

# print(stock[1])
# for row in stock:
#     print(row[0])

# # Practice 31
# # Nested Loop pada Nested List berfungsi 
# # untuk mengakses seluruh nilai di dalam setiap inner list (perulangan di dalam perulangan)

# stock = [
#     [5, 10, 15],
#     [20, 25],
#     [30, 35, 40]
# ]

# for row in stock:
#     for value in row:
#         print(value)

# # Practice 32
# # Mengolah data dalam Nested List

# stock = [
#     [5, 10],
#     [15, 20],
#     [25, 30]
# ]

# for row in stock:
#     for value in row:
#         print(value)

# total_stock = 0

# for row in stock:
#     for value in row:
#         total_stock += value

# print(total_stock)

# stock = [
#     [5, 10],
#     [15, 20],
#     [25, 30]
# ]

# for row in stock:
#     total_stock = 0

#     for value in row:
#         total_stock += value

# print(total_stock)

# stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# for row in stock:
#     print(row)

# for value in row:
#     print(value)

# # dari sintaks di bawah ini menunjukkan 
# # bahwa indentasi dapat mempengaruhi output yang ditampilkan
# for row in stock:
#     print(row)

#     for value in row:
#         print(value)
# #############################################################
# for row in stock:
#     for value in row:
#         print(value)

# total_stock = 0

# for row in stock:
#     for value in row:
#         total_stock += value

# print(total_stock)

# for value in row:
#     print(value)

# for row in stock:
#     total_stock = 0

#     for value in row:
#         total_stock += value

# print(total_stock)

# # Practice 33
# # List Indexing, Slicing & Mutation

# numbers = [10, 20, 30, 40, 50]

# selected = numbers[1:4]

# selected[0] = 100
# numbers.append(60)

# print(numbers)
# print(selected)

# # Practice 34
# # Aliasing vs shallow copy

# numbers = [
#     [10, 20],
#     [30, 40]
# ]


# selected = numbers.copy()


# selected[0][1] = 100

# print(numbers)
# print(selected)

# # Practice 34.2
# # Aliasing vs shallow copy
# # Peletakan output print() sebelum terjadi mutation

# numbers = [
#     [10, 20],
#     [30, 40]
# ]


# selected = numbers.copy()

# print(numbers)

# selected[0][1] = 100

# print(selected)

# # Practice 34.2
# # Aliasing vs shallow copy
# # jadi indexing pada variable selected mempengaruhi 
# # mutation pada numbers seperti pada practice sebelumnya

# numbers = [
#     [10, 20],
#     [30, 40]
# ]

# selected = numbers.copy()

# selected[1] = [100, 200]

# print(numbers)
# print(selected)

# # Practice 34.3
# # pada practice ini selected[1] ini dapat merubah seluruh inner list

# numbers = [
#     [10, 20],
#     [30, 40]
# ]

# selected = numbers.copy()

# selected[1].append(50)

# print(numbers)
# print(selected)

# # Practice 34.4
# # pada practice ini selected.append() ini 
# # hanya menambahkan nilai baru dan tidak merubah nilai awal variable numbers

# numbers = [
#     [10, 20],
#     [30, 40]
# ]

# selected = numbers.copy()

# selected.append([50, 60])

# print(numbers)
# print(selected)

# # Practice 35
# # List Comprehension

# stock = [5, 12, 8, 20, 3, 15, 10]

# selected = [x * 2 for x in stock if x >= 10]

# print(selected)
# print(stock)

# # Practice 36
# # List Comprehension dengan Conditional Expression

# stock = [5, 12, 8, 20, 3, 15, 10]

# stock_status = [
#     "Low Stock" if x < 10 else "Available"
#     for x in stock
# ]

# print(stock)
# print(stock_status)

# # Practice 37
# # filtering and conditional expression

# stock = [5, 12, 8, 20, 3, 15, 10]

# result = [
#     "Critical" if x < 10 else "Normal"
#     for x in stock
#     if x <= 12
# ]

# print(result)

# # Practice 38
# # Nested List, Iteration, & Accumulator

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# total_stock = 0

# for warehouse in warehouse_stock:
#     for stock in warehouse:
#         total_stock += stock

# print(total_stock)

# # Practice 39
# # Accumulator with conditional filtering

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# total_stock = 0

# for warehouse in warehouse_stock:
#     for stock in warehouse:
#         if stock >= 20:
#             total_stock += stock

# print(total_stock)

# # Practice 40
# # Accumulator Scope & Reset

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# for warehouse in warehouse_stock:
#     total_stock = 0

#     for stock in warehouse:
#         total_stock += stock

#     print(total_stock)

# # Practice 40.1
# # dengan posisi print di dalam outer loop maka output nya juga berbeda

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# for warehouse in warehouse_stock:
#     total_stock = 0

#     for stock in warehouse:
#         total_stock += stock

# print(total_stock)

# # Practice 40.2
# # dengan posisi print di dalam inner loop maka output nya juga berbeda

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# for warehouse in warehouse_stock:
#     total_stock = 0

#     for stock in warehouse:
#         total_stock += stock

#         print(total_stock)

# # Practice 41
# # Accumulator and List .append()

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# warehouse_totals = []

# for warehouse in warehouse_stock:
#     total_stock = 0

#     for stock in warehouse:
#         total_stock += stock

#     warehouse_totals.append(total_stock)

# print(warehouse_totals)
# print(sum(warehouse_totals))

# # Practice 41
# # Accumulator and List .append()
# # perbedaan pada posisi warhouse_total.append()

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# warehouse_totals = []

# for warehouse in warehouse_stock:
#     total_stock = 0

#     for stock in warehouse:
#         total_stock += stock

#         warehouse_totals.append(total_stock)

# print(warehouse_totals)
# print(sum(warehouse_totals))

# # Practice 42
# # Debbuging and Logical Error

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# total_stock = 0

# for warehouse in warehouse_stock:
#     for stock in warehouse:
#         total_stock = stock

# print(total_stock)

# # Practice 42.1
# # penambahan total_stock_warehouse = warehouse agar 
# # dapat mengetahui proses eksekusi yang sedang berjalan
# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# total_stock = 0

# for warehouse in warehouse_stock:
#     total_stock_warehouse = warehouse
#     for stock in warehouse:
#         total_stock = stock

# print(total_stock_warehouse)
# print(total_stock)

# # Practice 43
# # Assigment vs Accumulation

# numbers = [10, 20, 30, 40]

# total = 0

# for number in numbers:
#     total += number

#     if number == 30:
#         total = 0

# print(total)

# # Practice 43.1
# # tambahan inisialisasi baru

# numbers = [10, 20, 30, 40]

# total_numbers = 0
# total = 0

# for number in numbers:
#     total_numbers += number

#     if number == 30:
#         total = 0

# print(total)

# # Practice 43.2

# numbers = [10, 20, 30, 40]

# total_numbers = 0
# total = 0

# for number in numbers:
#     total_numbers += number

#     if number == 30:
#         total = 0

# print(total_numbers)
# print(total)

# #Practice 43.3
# ''''
# Dari proses sebelumnya dengan proses accumulation
# total += number lalu setelah itu melewati proses filter
# if number == 20 jika pada memenuhi maka proses
# akan ditimpa dengan proses penjumlahan berikutnya
# akan tetapi tetapi jika number == 40 maka output
# yang di tampilkan menjadi 0 karena memenuhi kondisi True
# akan tetapi jika number tidak memenuhi kondisi didalam numbers
# maka output akan menghasilkan penjumlahan seluruh elemen
# '''
# numbers = [10, 20, 30, 40]

# total = 0

# for number in numbers:
#     total += number

#     if number == 20:
#         total = 0

# print(total)

# # Practice 43.4

# numbers = [10, 20, 30, 40]

# total = 0

# for number in numbers:
#     total += number

#     if number == 20:
#         total += 70

# print(total)

# # Practice 43.5
# '''
# karena kondisi if tidak ada di dalam list maka output 
# akan melakukan penjumlahan seluruh nya yang ada pada list
# '''
# numbers = [10, 20, 30, 40]

# total = 0

# for number in numbers:
#     total += number

#     if number == 50:
#         total = 10

# print(total)

# # Practice 44
# # memindahkan posisi if number dan total

# numbers = [10, 20, 30, 40]
# total = 0

# for number in numbers:
#     if number == 30:
#         total = 0

#     total += number

# print(total)

# # Practice 44.1
# # merubah total = 0 menjadi number = 0

# numbers = [10, 20, 30, 40]
# total = 0

# for number in numbers:
#     if number == 20:
#         number = 0

#     total += number

# print(total)

# # Practice 44.2
# # merubah nilai if number

# numbers = [10, 20, 30, 40]
# total = 0

# for number in numbers:
#     if number == 20:
#         total = 0

#     total += number

# print(total)

# # Practice 44.3
# # Debbuging

# numbers = [10, 20, 30, 40]
# total = 0

# for number in numbers:
#     print("Sebelum if:", number, total)

#     if number == 30:
#         total = 0

#     print("Setelah if:", number, total)

#     total += number

#     print("Setelah accumulation:", number, total)

# print(total)

# # Practice 45
# # Independent Debugging Practice

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# total_stock = 0

# for warehouse in warehouse_stock:
#     for stock in warehouse:
#         if stock >= 15:
#             total_stock = stock
# print(total_stock)

# # Practice 45.1
# '''
# dari sintaks di bawah hanya memindahkan posisi print(total_stock)
# dan sistem melakukan eksekusi inner loop dan mencari stock yang lebih
# dari sama dengan 15
# '''

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# total_stock = 0

# for warehouse in warehouse_stock:
#     for stock in warehouse:
#         if stock >= 15:
#             total_stock = stock
#             print(total_stock)

# # Practice 45.2
# '''
# penambahan print(warehouse) akan menghasilkan output
# setiap nested list dengan nilai yang diambil sesuai
# dengan kondisi if
# '''

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# total_stock = 0

# for warehouse in warehouse_stock:
#     print(warehouse)
#     for stock in warehouse:
#         if stock >= 15:
#             total_stock = stock
#             print(total_stock)

# # Practice 45.3
# '''
# merubah opertor yang ada pada total_stock = stock
# menjadi total_stock += stock maka hasil output menjadi 
# 140 karena hanya melakukan penjumlahan yang memiliki
# nilai lebih dari sama dengan 15
# '''

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# total_stock = 0

# for warehouse in warehouse_stock:
#     for stock in warehouse:
#         if stock >= 15:
#             # total_stock = stock
#             total_stock += stock
# print(total_stock)

# # Practice 45.4
# '''
# Mengubah posisi print(total_stock) pada inner loop
# output menjadi proses penjumlahan stock >= 15
# '''

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# total_stock = 0

# for warehouse in warehouse_stock:
#     for stock in warehouse:
#         if stock >= 15:
#             total_stock += stock
#             print(total_stock)

# # Practice 45.5
# '''
# seperti sebelumnya akan tetapi ini dengan
# operasi penjumlahan lihat output pada terminal
# '''

# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# total_stock = 0

# for warehouse in warehouse_stock:
#     print(warehouse)
#     for stock in warehouse:
#         if stock >= 15:
#             total_stock += stock
#             print(total_stock)

# Pactice 46
# Independent Coding Challenge

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

# Pactice 46.1
# Independent Coding Challenge
'''
menambahkan nama pada tiap nilai "Warehouse"
'''

warehouse_stock = [
    [10, 20, 30],
    [15, 25, 35],
    [5, 10, 15]
]


for index, warehouse in enumerate(warehouse_stock):
    total_stock = 0
    for stock in warehouse:
        total_stock += stock
            
    print("Warehouse", index + 1, ":", total_stock)

# Pactice 46.2
# Independent Coding Challenge
'''
menambahkan nama pada tiap nilai "Warehouse"
start=1 pada enumerate ini tidak merubah 
nilai list pada index hanya sebagai penanda
angak awal yang harus di mulai
'''

warehouse_stock = [
    [10, 20, 30],
    [15, 25, 35],
    [5, 10, 15]
]


for index, warehouse in enumerate(warehouse_stock, start=1):
    total_stock = 0
    for stock in warehouse:
        total_stock += stock
            
    print("Warehouse", index, ":", total_stock)

# Pactice 46.3
# Independent Coding Challenge
# menghilangkan index dalam penamaan warehouse
# index dan enumerate harus tetap digunakan sebagai
# Penomoran dan urutan idex

warehouse_stock = [
    [10, 20, 30],
    [15, 25, 35],
    [5, 10, 15]
]


for _, warehouse in enumerate(warehouse_stock, start=1):
    total_stock = 0
    for stock in warehouse:
        total_stock += stock
            
    print("Warehouse: ", total_stock)
    # print(total_stock)

# Practice 46.4

warehouse_names = [
    "Central Warehouse",
    "Urban Warehouse",
    "Regional Warehouse"
]

for index, name in enumerate(warehouse_names, start=1):
    print(index, name)

# Practice 46.5

warehouse_names = [
    "Central Warehouse",
    "Urban Warehouse",
    "Regional Warehouse"
]

warehouse_stock = [
    [10, 20, 30],
    [15, 25, 35],
    [5, 10, 15]
]



for index, warehouse in enumerate(warehouse_stock):
    total_stock = 0
    for stock in warehouse:
        total_stock += stock

    warehouse_name = warehouse_names[index]
    print(warehouse_name, ":", total_stock)


# # Practice 46
# # Failed
# warehouse_stock = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [5, 10, 15]
# ]

# stock_warehouse = 0

# for warehouse in warehouse_stock:
#     for stock in warehouse:
#         stock_warehouse += stock
#     print(stock_warehouse)