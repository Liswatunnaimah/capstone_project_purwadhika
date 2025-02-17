from tabulate import tabulate 

# Database awal dalam bentuk List of Dictionary
buku_database = [
    {"id": 101, "judul": "Mimpi Sejuta Dolar", "penulis": "Merry Riana", "penerbit": "Gramedia", "tahun": 2011, "dipinjam": 4, "status": "available"},
    {"id": 102, "judul": "Kisah Sukses dari Nol", "penulis": "Chairul Tanjung", "penerbit": "Gramedia", "tahun": 2012, "dipinjam": 3, "status": "available"},
    {"id": 103, "judul": "Manusia Setengah Salmon", "penulis": "Raditya Dika", "penerbit": "GagasMedia", "tahun": 2011, "dipinjam": 2,"status": "not available"},
    {"id": 104, "judul": "Hidup Sederhana", "penulis": "Desi Anwar", "penerbit": "Gramedia", "tahun": 2014, "dipinjam": 4, "status": "available"},
    {"id": 105, "judul": "Nanti Kita Cerita Tentang Hari Ini", "penulis": "Marchella FP", "penerbit": "KPG", "tahun": 2018, "dipinjam": 5, "status": "available"},
    {"id": 106, "judul": "You Do You", "penulis": "Fellexandro Ruby", "penerbit": "Bentang Pustaka", "tahun": 2020,  "dipinjam": 6, "status": "available"},
    {"id": 107, "judul": "Esok Lebih Baik", "penulis": "Rhenald Kasali", "penerbit": "Bentang Pustaka", "tahun": 2015, "dipinjam": 5, "status": "available"},
    {"id": 108, "judul": "Stop Overthinking", "penulis": "Nick Trenton", "penerbit": "Independently Published", "tahun": 2021, "dipinjam": 4, "status": "not available"},
    {"id": 109, "judul": "Mindset: The New Psychology of Success", "penulis": "Carol Dweck", "penerbit": "Ballantine Books", "tahun": 2006, "dipinjam": 6, "status": "available"},
    {"id": 110, "judul": "Grit", "penulis": "Angela Duckworth", "penerbit": "Scribner", "tahun": 2016,  "dipinjam": 7, "status": "available"},
    {"id": 111, "judul": "How To Think Like Sherlock Holmes", "penulis": "Maria Konnikova", "penerbit": "Viking", "tahun": 2013, "dipinjam": 5, "status": "available"},
    {"id": 112, "judul": "Awaken the Giant Within", "penulis": "Tony Robbins", "penerbit": "Free Press", "tahun": 1991, "dipinjam": 5, "status": "available"},
    {"id": 113, "judul": "Outliers", "penulis": "Malcolm Gladwell", "penerbit": "Little, Brown and Company", "tahun": 2008, "dipinjam": 10, "status": "available"},
    {"id": 114, "judul": "Kamu Gak Sendirian", "penulis": "Pidi Baiq", "penerbit": "Pastel Books", "tahun": 2019,  "dipinjam": 9, "status": "not available"},
    {"id": 115, "judul": "Menjadi Manusia Kuat", "penulis": "Yudi Latif", "penerbit": "Kompas", "tahun": 2015, "dipinjam": 8, "status": "not available"},
    {"id": 116, "judul": "Sapiens", "penulis": "Yuval Noah Harari", "penerbit": "Gramedia", "tahun": 2014, "dipinjam": 4, "status": "available"},
    {"id": 117, "judul": "Atomic Habits", "penulis": "James Clear", "penerbit": "Penguin", "tahun": 2018,  "dipinjam": 8, "status": "available"},
    {"id": 118, "judul": "Rich Dad Poor Dad", "penulis": "Robert T. Kiyosaki", "penerbit": "Warner Books", "tahun": 1997, "dipinjam": 8, "status": "not available"},
    {"id": 119, "judul": "Think and Grow Rich", "penulis": "Napoleon Hill", "penerbit": "Tribute Books", "tahun": 1937,  "dipinjam": 6, "status": "available"},
    {"id": 120, "judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "penerbit": "Bentang Pustaka", "tahun": 2005, "dipinjam": 8, "status": "available"},
    {"id": 121, "judul": "Bumi", "penulis": "Tere Liye", "penerbit": "Gramedia", "tahun": 2014, "dipinjam": 5, "status": "not available"},
    {"id": 122, "judul": "Hujan", "penulis": "Tere Liye", "penerbit": "Gramedia", "tahun": 2016, "dipinjam": 7, "status": "available"},
    {"id": 123, "judul": "Dilan: Dia adalah Dilanku Tahun 1990", "penulis": "Pidi Baiq", "penerbit": "Pastel Books", "tahun": 2014, "dipinjam": 6, "status": "available"},
    {"id": 124, "judul": "Filosofi Kopi", "penulis": "Dee Lestari", "penerbit": "Bentang Pustaka", "tahun": 2006, "dipinjam": 4, "status": "available"},
    {"id": 125, "judul": "Perahu Kertas", "penulis": "Dee Lestari", "penerbit": "Bentang Pustaka", "tahun": 2009, "dipinjam": 7, "status": "not available"},
    {"id": 126, "judul": "Sabtu Bersama Bapak", "penulis": "Adhitya Mulya", "penerbit": "GagasMedia", "tahun": 2014, "dipinjam": 5, "status": "available"},
    {"id": 127, "judul": "Rindu", "penulis": "Tere Liye", "penerbit": "Republika", "tahun": 2014, "dipinjam": 3, "status": "available"},
    {"id": 128, "judul": "Negeri 5 Menara", "penulis": "A. Fuadi", "penerbit": "Gramedia", "tahun": 2009, "dipinjam": 8, "status": "available"},
    {"id": 129, "judul": "Bidadari-Bidadari Surga", "penulis": "Tere Liye", "penerbit": "Republika", "tahun": 2008, "dipinjam": 6, "status": "not available"},
    {"id": 130, "judul": "Harry Potter and the Philosopher's Stone", "penulis": "J.K. Rowling", "penerbit": "Bloomsbury", "tahun": 1997, "dipinjam": 10, "status": "available"},
    {"id": 131, "judul": "The Lord of the Rings", "penulis": "J.R.R. Tolkien", "penerbit": "Allen & Unwin", "tahun": 1954, "dipinjam": 9, "status": "available"},
    {"id": 132, "judul": "The Catcher in the Rye", "penulis": "J.D. Salinger", "penerbit": "Little, Brown and Company", "tahun": 1951, "dipinjam": 8, "status": "available"},
    {"id": 133, "judul": "Pride and Prejudice", "penulis": "Jane Austen", "penerbit": "T. Egerton", "tahun": 1813, "dipinjam": 7, "status": "available"},
    {"id": 134, "judul": "To Kill a Mockingbird", "penulis": "Harper Lee", "penerbit": "J.B. Lippincott & Co.", "tahun": 1960, "dipinjam": 6, "status": "available"},
    {"id": 135, "judul": "Hujan Bulan Juni", "penulis": "Sapardi Djoko Damono", "penerbit": "Gramedia", "tahun": 1994, "dipinjam": 10, "status": "not available"},
    {"id": 136, "judul": "Surat Kecil untuk Tuhan", "penulis": "Agnes Davonar", "penerbit": "Inandra Published", "tahun": 2008, "dipinjam": 6, "status": "available"},
    {"id": 137, "judul": "Orang-orang Biasa", "penulis": "Andrea Hirata", "penerbit": "Bentang Pustaka", "tahun": 2019, "dipinjam": 7, "status": "available"},
    {"id": 138, "judul": "Mariposa", "penulis": "Luluk HF", "penerbit": "Coconut Books", "tahun": 2020, "dipinjam": 4, "status": "not available"},
    {"id": 139, "judul": "The Da Vinci Code", "penulis": "Dan Brown", "penerbit": "Doubleday", "tahun": 2003, "dipinjam": 4, "status": "available"},
    {"id": 140,"judul": "Angels and Demons", "penulis": "Dan Brown", "penerbit": "Pocket Books", "tahun": 2000, "dipinjam": 10, "status": "not available"},
    {"id": 141, "judul": "Inferno", "penulis": "Dan Brown", "penerbit": "Doubleday", "tahun": 2013, "dipinjam": 5, "status": "not available"},
    {"id": 142, "judul": "Gone Girl", "penulis": "Gillian Flynn", "penerbit": "Crown Publishing", "tahun": 2012, "dipinjam": 3, "status": "available"},
    {"id": 143, "judul": "Twilight", "penulis": "Stephenie Meyer", "penerbit": "Little, Brown and Company", "tahun": 2005, "dipinjam": 5, "status": "not available"},
    {"id": 144, "judul": "The Fault in Our Stars", "penulis": "John Green", "penerbit": "Dutton Books", "tahun": 2012, "dipinjam": 10, "status": "not available"},
    {"id": 145, "judul": "Looking for Alaska", "penulis": "John Green", "penerbit": "Dutton Books", "tahun": 2005, "dipinjam": 5, "status": "available"},
    {"id": 146, "judul": "A Thousand Splendid Suns", "penulis": "Khaled Hosseini", "penerbit": "Riverhead Books", "tahun": 2007, "dipinjam": 10, "status": "not available"},
    {"id": 147, "judul": "Eleanor Oliphant Is Completely Fine", "penulis": "Gail Honeyman", "penerbit": "HarperCollins", "tahun": 2017, "dipinjam": 7, "status": "available"},
    {"id": 148, "judul": "The Girl on the Train", "penulis": "Paula Hawkins", "penerbit": "Riverhead Books", "tahun": 2015, "dipinjam": 3, "status": "available"} 
]

# Main Menu
def tampilkan_menu():
    print("\nSISTEM MANAJEMEN PERPUSTAKAAN")
    print("=" * 40)
    print("1. Read Data (Lihat Koleksi Buku)")
    print("2. Create Data (Tambah Koleksi Buku)")
    print("3. Update Data (Ubah Data Buku)")
    print("4. Delete Data (Hapus Data Buku)")
    print("5. Manage Borrowing (Peminjaman/Pengembalian)")
    print("6. Exit (Keluar)")
    print("=" * 40)

# Read Data (Lihat Koleksi Buku)
def lihat_koleksi_buku():
    while True:
        print("\nSUB-MENU: Koleksi Buku di Perpustakaan Liswatun Naimah")
        print("1. Tampilkan Semua Buku")
        print("2. Cari Buku Berdasarkan ID")
        print("3. Filter Buku Berdasarkan Kolom Lain")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi (1-4): ").strip()

        if pilihan == "1":
            tampilkan_semua_buku()
        elif pilihan == "2":
            cari_buku_by_id()
        elif pilihan == "3":
            filter_buku()
        elif pilihan == "4":
            break
        else:
            print("Opsi tidak valid. Silakan pilih kembali.")

# Fungsi Menampilkan Semua Data Buku
def tampilkan_semua_buku():
    if not buku_database:
        print("\nTidak ada data buku yang tersedia.")
        return
    print("\nDaftar Buku:")
    print(tabulate(buku_database, headers="keys", tablefmt="grid"))

# Fungsi Mencari Buku Berdasarkan ID
def cari_buku_by_id():
    try:
        id_buku = int(input("Masukkan ID Buku: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for buku in buku_database:
        if buku["id"] == id_buku:
            print("\nBuku Ditemukan:")
            print(tabulate([buku], headers="keys", tablefmt="grid"))
            return
    print("Buku dengan ID tersebut tidak ditemukan.")

# Fungsi Memfilter Buku Berdasarkan Kolom Selain ID
def filter_buku():
    kolom = input("Masukkan kolom yang ingin difilter (judul/penulis/penerbit/tahun/status): ").strip().lower()
    if kolom not in ["judul", "penulis", "penerbit", "tahun", "status"]:
        print("Kolom tidak valid.")
        return

    nilai = input(f"Masukkan nilai untuk {kolom}: ").strip()
    if kolom == "tahun":
        try:
            nilai = int(nilai)
        except ValueError:
            print("Tahun harus berupa angka.")
            return

    hasil = [buku for buku in buku_database if str(buku[kolom]).lower() == str(nilai).lower()]
    if hasil:
        print("\nBuku yang cocok dengan filter:")
        print(tabulate(hasil, headers="keys", tablefmt="grid"))
    else:
        print("Tidak ada buku yang cocok dengan filter tersebut.")

# Create Data (Tambah Koleksi Buku)
def tambah_koleksi_buku():
    while True:
        print("\nSUB-MENU: Tambah Koleksi Buku")
        print("1. Tambah Buku Baru")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi (1-2): ").strip()
        
        if pilihan == "1":
            try:
                id_buku = int(input("Masukkan ID Buku: "))
            except ValueError:
                print("ID harus berupa angka.")
                continue

            # Cek apakah ID sudah ada di database
            if any(buku["id"] == id_buku for buku in buku_database):
                print("ID Buku sudah ada. Masukkan ID yang unik.")
                continue  # Kembali ke sub-menu

            judul = input("Masukkan Judul Buku: ").strip()
            penulis = input("Masukkan Nama Penulis: ").strip()
            penerbit = input("Masukkan Nama Penerbit: ").strip()
            
            try:
                tahun = int(input("Masukkan Tahun Terbit: "))
            except ValueError:
                print("Tahun harus berupa angka.")
                continue

            # Menampilkan konfirmasi data sebelum menyimpan
            buku_baru = {"id": id_buku, "judul": judul, "penulis": penulis, "penerbit": penerbit, "tahun": tahun, "status": "available"}
            print("\nData yang akan disimpan:")
            print(tabulate([buku_baru], headers="keys", tablefmt="grid"))

            konfirmasi = input("Apakah Anda yakin ingin menyimpan data ini? (y/n): ").strip().lower()
            if konfirmasi == "y":
                buku_database.append(buku_baru)
                print("\nBuku berhasil ditambahkan.")
            else:
                print("\nPenyimpanan dibatalkan.")
        
        elif pilihan == "2":
            break  # Kembali ke menu utama
        
        else:
            print("Opsi tidak valid. Silakan pilih kembali.")

# Update Data (Ubah Data Buku)
def update_data_buku():
    while True:
        print("\nSUB-MENU: Update Data Buku")
        print("1. Update Buku")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi (1-2): ").strip()
        
        if pilihan == "1":
            try:
                id_buku = int(input("Masukkan ID Buku yang ingin diperbarui: "))
            except ValueError:
                print("ID harus berupa angka.")
                continue

            # Pencarian Buku
            buku_ditemukan = None
            for buku in buku_database:
                if buku["id"] == id_buku:
                    buku_ditemukan = buku
                    break

            if not buku_ditemukan:
                print("Buku dengan ID tersebut tidak ditemukan.")
                continue  # Kembali ke sub-menu
            
            # Menampilkan Data Buku Sebelum Update
            print("\nData Buku Saat Ini:")
            print(tabulate([buku_ditemukan], headers="keys", tablefmt="grid"))

            konfirmasi = input("\nApakah Anda ingin melanjutkan update? (y/n): ").strip().lower()
            if konfirmasi != "y":
                print("\nUpdate dibatalkan.")
                continue  # Kembali ke sub-menu

            # User input nama kolom yang ingin diubah
            kolom_update = input("\nMasukkan nama kolom yang ingin diupdate (judul/penulis/penerbit/tahun/status): ").strip().lower()
            if kolom_update not in ["judul", "penulis", "penerbit", "tahun", "status"]:
                print("Kolom tidak valid. Silakan coba lagi.")
                continue

            nilai_baru = input(f"Masukkan {kolom_update} baru: ").strip()
            if kolom_update == "tahun":
                try:
                    nilai_baru = int(nilai_baru)
                except ValueError:
                    print("Tahun harus berupa angka.")
                    continue

            # Menampilkan Konfirmasi Sebelum Update
            print("\nData yang akan diperbarui:")
            buku_sementara = buku_ditemukan.copy()
            buku_sementara[kolom_update] = nilai_baru
            print(tabulate([buku_sementara], headers="keys", tablefmt="grid"))

            konfirmasi_update = input("\nApakah Anda yakin ingin memperbarui data ini? (y/n): ").strip().lower()
            if konfirmasi_update == "y":
                buku_ditemukan[kolom_update] = nilai_baru
                print("\nData berhasil diperbarui.")
            else:
                print("\nUpdate dibatalkan.")
        
        elif pilihan == "2":
            break  # Kembali ke menu utama
        
        else:
            print("Opsi tidak valid. Silakan pilih kembali.")

# Delete (Menghapus Data Buku)
def hapus_data_buku():
    while True:
        print("\nSUB-MENU: Hapus Data Buku")
        print("1. Hapus Buku")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi (1-2): ").strip()

        if pilihan == "1":
            try:
                id_buku = int(input("Masukkan ID Buku yang ingin dihapus: "))
            except ValueError:
                print("ID harus berupa angka.")
                continue

            # Pencarian Buku
            buku_ditemukan = None
            for buku in buku_database:
                if buku["id"] == id_buku:
                    buku_ditemukan = buku
                    break

            if not buku_ditemukan:
                print("Buku dengan ID tersebut tidak ditemukan.")
                continue  # Kembali ke sub-menu

            # Menampilkan Data Buku Sebelum Dihapus
            print("\nData Buku yang Akan Dihapus:")
            print(tabulate([buku_ditemukan], headers="keys", tablefmt="grid"))

            # Konfirmasi Penghapusan
            print("\nApakah Anda yakin ingin menghapus buku ini?")
            print("1. Iya, hapus buku")
            print("2. Tidak, kembali ke sub-menu delete")
            konfirmasi = input("Pilih opsi (1-2): ").strip()

            if konfirmasi == "1":
                buku_database.remove(buku_ditemukan)
                print("\nBuku berhasil dihapus.")
            elif konfirmasi == "2":
                print("\nPenghapusan dibatalkan.")
            else:
                print("Opsi tidak valid. Silakan pilih kembali.")

        elif pilihan == "2":
            break  # Kembali ke menu utama

        else:
            print("Opsi tidak valid. Silakan pilih kembali.")

# Fungsi Manajemen Peminjaman & Pengembalian
def kelola_peminjaman():
    while True:
        print("\nSUB-MENU: Manajemen Peminjaman & Pengembalian Buku")
        print("1. Pinjam Buku")
        print("2. Kembalikan Buku")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi (1-3): ").strip()

        if pilihan == "1":  # Opsi Peminjaman Buku
            try:
                id_buku = int(input("Masukkan ID Buku yang ingin dipinjam: "))
            except ValueError:
                print("ID harus berupa angka.")
                continue

            # Pencarian Buku
            buku_ditemukan = None
            for buku in buku_database:
                if buku["id"] == id_buku:
                    buku_ditemukan = buku
                    break

            if not buku_ditemukan:
                print("Buku dengan ID tersebut tidak ditemukan.")
                continue  # Kembali ke sub-menu

            if buku_ditemukan["status"] == "not available":
                print("Buku ini sudah dipinjam dan belum dikembalikan.")
                continue

            # Menampilkan Data Buku yang Akan Dipinjam
            print("\nBuku yang Akan Dipinjam:")
            print(tabulate([buku_ditemukan], headers="keys", tablefmt="grid"))

            # Konfirmasi Peminjaman
            print("\nApakah Anda yakin ingin meminjam buku ini?")
            print("1. Iya, pinjam buku")
            print("2. Tidak, kembali ke sub-menu peminjaman")
            konfirmasi = input("Pilih opsi (1-2): ").strip()

            if konfirmasi == "1":
                buku_ditemukan["status"] = "not available"
                if "dipinjam" in buku_ditemukan:
                    buku_ditemukan["dipinjam"] += 1
                else:
                    buku_ditemukan["dipinjam"] = 1
                print("\nBuku berhasil dipinjam.")
            elif konfirmasi == "2":
                print("\nPeminjaman dibatalkan.")
            else:
                print("Opsi tidak valid. Silakan pilih kembali.")

        elif pilihan == "2":  # Opsi Pengembalian Buku
            try:
                id_buku = int(input("Masukkan ID Buku yang ingin dikembalikan: "))
            except ValueError:
                print("ID harus berupa angka.")
                continue

            # Pencarian Buku
            buku_ditemukan = None
            for buku in buku_database:
                if buku["id"] == id_buku:
                    buku_ditemukan = buku
                    break

            if not buku_ditemukan:
                print("Buku dengan ID tersebut tidak ditemukan.")
                continue  # Kembali ke sub-menu

            if buku_ditemukan["status"] == "available":
                print("Buku ini tidak sedang dipinjam, sehingga tidak bisa dikembalikan.")
                continue

            # Menampilkan Data Buku yang Akan Dikembalikan
            print("\nBuku yang Akan Dikembalikan:")
            print(tabulate([buku_ditemukan], headers="keys", tablefmt="grid"))

            # Konfirmasi Pengembalian
            print("\nApakah Anda yakin ingin mengembalikan buku ini?")
            print("1. Iya, kembalikan buku")
            print("2. Tidak, kembali ke sub-menu pengembalian")
            konfirmasi = input("Pilih opsi (1-2): ").strip()

            if konfirmasi == "1":
                buku_ditemukan["status"] = "available"
                print("\nBuku berhasil dikembalikan.")
            elif konfirmasi == "2":
                print("\nPengembalian dibatalkan.")
            else:
                print("Opsi tidak valid. Silakan pilih kembali.")

        elif pilihan == "3":  # Kembali ke Menu Utama
            break

        else:
            print("Opsi tidak valid. Silakan pilih kembali.")

# Fungsi Utama untuk Menjalankan Program
def main():    
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-6): ").strip()

        if pilihan == "1":
            lihat_koleksi_buku()
        elif pilihan == "2":
            tambah_koleksi_buku()
        elif pilihan == "3":
            update_data_buku()
        elif pilihan == "4":
            hapus_data_buku()
        elif pilihan == "5":
            kelola_peminjaman()
        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan Sistem Perpustakaan.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()
