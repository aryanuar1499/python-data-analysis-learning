# MP01.2.2-Q4.1 — Accumulator Initialization Inside a For Loop
# Objective: Understand how accumulator initialization
# inside a loop affects the final total stock.
# posisi total_stock sebagai inisialisasi sangat berpengaruh

products = [
    ["P001", "Product A", 20],
    ["P002", "Product B", 35],
    ["P003", "Product C", 15]
]

total_stock = 0 #total_stock before for loop

for product in products:
    total_stock += product[2]

print(total_stock) #70, karena setiap nilai yang diambil tersimpan di total_stock

product = [
        ["P001", "Product A", 20],
        ["P002", "Product B", 35],
        ["P003", "Product C", 15]
]

for product in products:
    total_stock = 0 #total_stock after for loop
    total_stock += product[2]

print(total_stock) #15, di ambil dari iterasi ketiga, karena total_stock 
                   #tidak menyimpan nilai dan langsung mengubah 0 karena
                   #total_stock di eksekusi kembali

# MP01.2.2-Q5 — Total Stock Calculation Using Nested Lists

products = [
    ["P001", "Product A", 25],
    ["P002", "Product B", 40],
    ["P003", "Product C", 15],
    ["P004", "Product D", 30]
]

total_stock = 0

for product in products:
  total_stock += product[2]

print(total_stock)

# MP01.2.2-Q6 — Indentifying Low Stock Products
# Operator sangat mempengaruhi hasil output yang ditampilkan

products = [
    ["P001", "Product A", 25],
    ["P002", "Product B", 8],
    ["P003", "Product C", 10],
    ["P004", "Product D", 5]
]

minimum_stock = 10

for product in products:
  if product[2] < minimum_stock:
    print(product[1])

# MP01.2.2-Q7.2 — Conceptual Evaluation
# menghitung banyak produk yang mengalami low stock

products = [
    ["P001", "Product A", 25],
    ["P002", "Product B", 8],
    ["P003", "Product C", 10],
    ["P004", "Product D", 5]
]

minimum_stock = 10
low_stock_count = 0

for product in products:
   if product[2] < minimum_stock:
      low_stock_count += 1

print(low_stock_count)

# low_stock_count += 1 diganti dengan += product[2]
# untuk melihat output yang di hasilkan

products = [
    ["P001", "Product A", 25],
    ["P002", "Product B", 8],
    ["P003", "Product C", 10],
    ["P004", "Product D", 5]
]

minimum_stock = 10
low_stock_count = 0

for product in products:
   if product[2] < minimum_stock:
      low_stock_count += product[2]

print(low_stock_count) #13 karena penjumlahan dari
                       # stock produk B dan D

# MP01.2.2-Q7.3 — Independent Coding Practice

products = [
    ["P001", "Product A", 30],
    ["P002", "Product B", 7],
    ["P003", "Product C", 12],
    ["P004", "Product D", 4],
    ["P005", "Product E", 9]
]

minimum_stock = 10
low_stock_count = 0
low_stock_quantity = 0

for product in products:
  if product[2] < minimum_stock:
    low_stock_count += 1
    low_stock_quantity += product[2]
  #low_stock_quantity += product[2] #indentasi pada posisi ini akan menghasilkan output penjumlahan seluruh elemen stock
                                                                        
print(low_stock_count)
print(low_stock_quantity)

# MP01.2.2-Q8 — Collecting Low Stock Products into a New List

products = [
    ["P001", "Product A", 30],
    ["P002", "Product B", 7],
    ["P003", "Product C", 12],
    ["P004", "Product D", 4],
    ["P005", "Product E", 9]
]

minimum_stock = 10
low_stock_products = []

for product in products:
    if product[2] < minimum_stock:
        #low_stock_products.append(product[1])
        low_stock_products.append(product)

#print(low_stock_products)
#print(low_stock_products[1][2])
print(low_stock_products[2][1])

# MP01.2.2-Q8.4 — Independent Filtering Practice

products = [
    ["P001", "Product A", 15],
    ["P002", "Product B", 6],
    ["P003", "Product C", 25],
    ["P004", "Product D", 3],
    ["P005", "Product E", 10],
    ["P006", "Product F", 8]
]

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

products = [
    ["P001", "Product A", 15],
    ["P002", "Product B", 6],
    ["P003", "Product C", 25],
    ["P004", "Product D", 3],
    ["P005", "Product E", 10],
    ["P006", "Product F", 8]
]

minimum_stock = 10
low_stock_products = []
low_stock_count = 0
low_stock_quantity = 0

for product in products:
   if product[2] < minimum_stock:
      low_stock_products.append(product)
      low_stock_count += 1
      low_stock_quantity += product[2]

low_stock_products[0][2] = 100

print(products[1])
print(low_stock_products[0][2])

products = [
    ["P001", "Product A", 15],
    ["P002", "Product B", 6],
    ["P003", "Product C", 25],
    ["P004", "Product D", 3],
    ["P005", "Product E", 10],
    ["P006", "Product F", 8]
]

minimum_stock = 10
low_stock_products = []
low_stock_count = 0
low_stock_quantity = 0

for product in products:
   if product[2] < minimum_stock:
      low_stock_products.append(product.copy())
      low_stock_count += 1
      low_stock_quantity += product[2]

low_stock_products[0][2] = 100

print(products[1])
print(low_stock_products[0][2])