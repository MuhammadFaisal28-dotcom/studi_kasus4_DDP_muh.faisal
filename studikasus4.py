buku = {
    "judul" : "bumi manusia",
    "penulis" : "Pramoedya Ananta Toer",
    "tahun_terbit" : 1980

}

while True:
    print("--menu--")
    print("1. tampilkan buku")
    print("2. tambahkan penerbit")
    print("3. ubah penulis")
    print("4. hapus data penerbit")
    print("5. keluar")

    pilih =input("pilih menu (1/2/3/4/5): ")

    if pilih == "1":
        print("--data buku--")
        print("judul        : ", buku["judul"])
        print("penulis      : ", buku["penulis"])
        print("tahun_terbit : ", buku["tahun_terbit"])
        
        if "penerbit" in buku:
            print("penerbit     :", buku["penerbit"])

    elif pilih == "2":
        buku["penerbit"] = input("masukkan penerbit: ")
        print("penerbit berhasil di tambahkan")
        
    elif pilih == "3":
        buku["penulis"] = input("masukkan penulis: ")
        print("penulis berhasil ditambahkan")

    elif pilih == "4":
        del buku ["penerbit"]
        print("penerbit berhasil di hapus")

    elif pilih == "5":
        print("terima kasi telah menggunakan program ini")
        break

    else:
        print("pilihan tidak tersedia, silahkan pilih ulang")

    