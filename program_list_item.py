### PROGRAM LIST BELANJAAN 

## List
daftar_belanja = []

## Menambahkan Item ke List
def tambah_item ():
    nama = input("Masukan nama barang: ")
    jumlah = int(input("Jumlah: "))
    harga = int(input("Harga: "))
    
    list_item = {"Nama": nama, "Jumlah": jumlah, "Harga": harga}
    daftar_belanja.append(list_item)
    
    print("Item telah berhasil ditambahkan ^_^")
    MenuUtama ()

## Menampilkan Item dari List
def lihat_item():
    if not daftar_belanja:
        print("List belanjaan kosong!\n")
    else:
        print("\n== Daftar Item Belanja ==\n")
        for i, item in enumerate(daftar_belanja, start=1):
            print(f"{i}. Nama: {item['Nama']}, Jumlah: {item['Jumlah']}, Harga: {item['Harga']}")
        print()

    MenuUtama()

## Menghapus Item dari List
def hapus_item():
    lihat_item()
    if not daftar_belanja:
        MenuUtama()

    try:
        nomor_item = int(input("Masukkan nomor item yang akan dihapus: "))
        if 1 <= nomor_item <= len(daftar_belanja):
            del daftar_belanja[nomor_item - 1]
            print("Item berhasil dihapus!\n")
        else:
            print("Nomor item tidak valid!\n")
    except ValueError:
        print("Masukkan nomor yang valid!\n")

    MenuUtama()

## Menu Utama
def MenuUtama ():
    print("= = = PROGRAM LIST ITEM = = =\n")
    print("1. Tampilkan daftar item")
    print("2. Tambah item ke list")
    print("3. Hapus item dari list")
    print("99. keluar ?")
    
    pilihan = input("Masukan nomor: ")
    
    if pilihan == "1":
        lihat_item()
    elif pilihan == "2":
        tambah_item()
    elif pilihan == "3":
        hapus_item()
    elif pilihan == "99":
        print("List belanjaan anda telah tersimpan\n")
    else:
        print("Pilihan tidak tersedia, silahkan masukkan kembali !!\n")

## Memanggil MenuUtama
MenuUtama()

