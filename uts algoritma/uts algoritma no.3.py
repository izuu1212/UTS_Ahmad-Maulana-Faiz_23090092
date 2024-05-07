def hitung_total_harga(harga_barang):
    total = sum(harga_barang)
    return total

jumlah_barang = int(input("Masukkan jumlah barang: "))

harga_barang = []

for i in range(jumlah_barang):
    harga = float(input("Masukkan harga barang ke-{}: ".format(i+1)))
    harga_barang.append(harga)

total_harga = hitung_total_harga(harga_barang)

print("Total harga belanjaan dari {} barang adalah: Rp {:.2f}".format(jumlah_barang, total_harga))
