# Meminta pengguna memasukkan jumlah mahasiswa
daftar_belanjaan = int(input("Masukkan jumlah data  cutomer : "))

# Dictionary untuk menyimpan data
data_bel = {}

# Perulangan untuk input data setiap mahasiswa
for i in range():
    print(f"\ncutomer ke-{i+1}")
    nama_barang = input("Masukkan nama barang : ")                                      # str                                                                                                                                                                                                             
    harga_satuan_barang = input("Masukkan harga satuan barang : ")                                 # str
    jumlah_QTY = input("masukkan jumlah QTY: ")                                     # str
                                            

    # List untuk menyimpan tuple (mata kuliah, nilai)
    daftar_belanjaan = []

    jumlah_belanjaan = int(input("Masukkan jumlah belanjaan: "))                           # int
    for j in range(jumlah_belanjaan):
        nama_barang = input(f"  Nama barang ke-{j+1}: ")                                 # str
        harga_satuan_barang = float(input(f"  harga untuk {harga_satuan_barang}: "))        # float
        jumlah_QTY = input(f" jumlah QTY: ")    
        daftar_belanjaan.append((nama_barang, harga_satuan_barang))                                    # tuple dalam list

    # Simpan dalam dictionary
    daftar_belanjaan[daftar_belanjaan] = {
        "nama cutemer": nama_cutomer, 
        "tanggal belanjaan": tanggal_belanja,
        "nama barang": nama_barang,
        "harga barang": harga_satuan_barang,
    }

# Menampilkan hasil
print("\n=== Daftar Data cutomer dan data belanjaan ===")
for nama, info in data_cutomer.items():
    tanggal_belanja = info["tanggal belanja"]
    jumlah_barang = info["jumlah barang"]
    nama_barang = info["nama barang"]
    harga_satuan_barang = info["harga"]
    
    # Hitung rata-rata
    total_harga = sum(harga for _, harga in harga_satuan_barang)
    rata_rata = total_harga / len(harga_satuan_barang) if harga else 0

    print(f"\nNAMA CUTOMER    : {nama_cutomer}")
    print(f"TANGGAL BELANJAAN      : {tanggal_belanja}")
    print(f"NAMA BARANG   : {nama_barang}")
    print(f"HARGA BARANG   : {harga}")
    print("TOTAL    :")
    for barang, harga in harga_satuan_barang:
        print(f"  {barang} = {harga}")
    print(f"Rata-rata : {rata_rata:.2f}")