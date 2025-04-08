# perulangan (loop)

#for kondisi:
#    aksi JALANKAN AKSI

angka_list =[0,2,4,8,10] # ini adalah list
print(angka_list)

#angka = 0
#print(angka)
#angka += 1 # angka = angka + 1
#print(angka)
#angka += 1
# print(angka)

# for loop
for i in angka_list:
    print(f"i sekarang -> {i}")
print("loop berakhir \n")
for i in range(5):
    print(f"i sekarang -> {i}")
print("loop range berakhir \n")
for i in range(1,10):
    print(f"i sekarang -> {i}")
    print("loop range berakhir \n")
angka = 0 
while angka < 3: # kondisi
    angka += 1 # aksi 1
    print("*" * angka) #aksi 2

