from tabulate import tabulate 

# Perpustakaan Liswatun Naimah
# Ucapan Selamat Datang
def kata_sambutan():
    print("="*150)
    print("Selamat datang di Perpustakaan Liswatun Naimah!")
    print("Kami siap membantu Anda menemukan buku terbaik untuk dibaca.")
    print("Jangan ragu untuk mengeksplor koleksi kami!")
    print("="*150)

# Database awal dalam bentuk List of Dictionary
buku_database = [
    {"id": 101, "judul": "Mimpi Sejuta Dolar", "penulis": "Merry Riana", "penerbit": "Gramedia", "tahun": 2011, "status": "available"},
    {"id": 102, "judul": "Kisah Sukses dari Nol", "penulis": "Chairul Tanjung", "penerbit": "Gramedia", "tahun": 2012, "status": "available"},
    {"id": 103, "judul": "Manusia Setengah Salmon", "penulis": "Raditya Dika", "penerbit": "GagasMedia", "tahun": 2011, "status": "not available"},
    {"id": 104, "judul": "Hidup Sederhana", "penulis": "Desi Anwar", "penerbit": "Gramedia", "tahun": 2014, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 4, "status": "available"},
    {"id": 105, "judul": "Nanti Kita Cerita Tentang Hari Ini", "penulis": "Marchella FP", "penerbit": "KPG", "tahun": 2018, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 5, "status": "available"},
    {"id": 106, "judul": "You Do You", "penulis": "Fellexandro Ruby", "penerbit": "Bentang Pustaka", "tahun": 2020, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 6, "status": "available"},
    {"id": 107, "judul": "Esok Lebih Baik", "penulis": "Rhenald Kasali", "penerbit": "Bentang Pustaka", "tahun": 2015, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 5, "status": "available"},
    {"id": 108, "judul": "Stop Overthinking", "penulis": "Nick Trenton", "penerbit": "Independently Published", "tahun": 2021, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 4, "status": "not available"},
    {"id": 109, "judul": "Mindset: The New Psychology of Success", "penulis": "Carol Dweck", "penerbit": "Ballantine Books", "tahun": 2006, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 6, "status": "available"},
    {"id": 110, "judul": "Grit", "penulis": "Angela Duckworth", "penerbit": "Scribner", "tahun": 2016, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 7, "status": "available"},
    {"id": 111, "judul": "How To Think Like Sherlock Holmes", "penulis": "Maria Konnikova", "penerbit": "Viking", "tahun": 2013, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 5, "status": "available"},
    {"id": 112, "judul": "Awaken the Giant Within", "penulis": "Tony Robbins", "penerbit": "Free Press", "tahun": 1991, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 5, "status": "available"},
    {"id": 113, "judul": "Outliers", "penulis": "Malcolm Gladwell", "penerbit": "Little, Brown and Company", "tahun": 2008, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 10, "status": "available"},
    {"id": 114, "judul": "Kamu Gak Sendirian", "penulis": "Pidi Baiq", "penerbit": "Pastel Books", "tahun": 2019, "kota penerbitan": "Bandung", "negara penerbitan": "Indonesia", "dipinjam": 9, "status": "not available"},
    {"id": 115, "judul": "Menjadi Manusia Kuat", "penulis": "Yudi Latif", "penerbit": "Kompas", "tahun": 2015, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 8, "status": "not available"},
    {"id": 116, "judul": "Sapiens", "penulis": "Yuval Noah Harari", "penerbit": "Gramedia", "tahun": 2014, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 4, "status": "available"},
    {"id": 117, "judul": "Atomic Habits", "penulis": "James Clear", "penerbit": "Penguin", "tahun": 2018, "kota penerbitan": "London", "negara penerbitan": "UK", "dipinjam": 8, "status": "available"},
    {"id": 118, "judul": "Rich Dad Poor Dad", "penulis": "Robert T. Kiyosaki", "penerbit": "Warner Books", "tahun": 1997, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 8, "status": "not available"},
    {"id": 119, "judul": "Think and Grow Rich", "penulis": "Napoleon Hill", "penerbit": "Tribute Books", "tahun": 1937, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 6, "status": "available"},
    {"id": 120, "judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "penerbit": "Bentang Pustaka", "tahun": 2005, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 8, "status": "available"},
    {"id": 121, "judul": "Bumi", "penulis": "Tere Liye", "penerbit": "Gramedia", "tahun": 2014, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 5, "status": "not available"},
    {"id": 122, "judul": "Hujan", "penulis": "Tere Liye", "penerbit": "Gramedia", "tahun": 2016, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 7, "status": "available"},
    {"id": 123, "judul": "Dilan: Dia adalah Dilanku Tahun 1990", "penulis": "Pidi Baiq", "penerbit": "Pastel Books", "tahun": 2014, "kota penerbitan": "Bandung", "negara penerbitan": "Indonesia", "dipinjam": 6, "status": "available"},
    {"id": 124, "judul": "Filosofi Kopi", "penulis": "Dee Lestari", "penerbit": "Bentang Pustaka", "tahun": 2006, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 4, "status": "available"},
    {"id": 125, "judul": "Perahu Kertas", "penulis": "Dee Lestari", "penerbit": "Bentang Pustaka", "tahun": 2009, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 7, "status": "not available"},
    {"id": 126, "judul": "Sabtu Bersama Bapak", "penulis": "Adhitya Mulya", "penerbit": "GagasMedia", "tahun": 2014, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 5, "status": "available"},
    {"id": 127, "judul": "Rindu", "penulis": "Tere Liye", "penerbit": "Republika", "tahun": 2014, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 3, "status": "available"},
    {"id": 128, "judul": "Negeri 5 Menara", "penulis": "A. Fuadi", "penerbit": "Gramedia", "tahun": 2009, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 8, "status": "available"},
    {"id": 129, "judul": "Bidadari-Bidadari Surga", "penulis": "Tere Liye", "penerbit": "Republika", "tahun": 2008, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 6, "status": "not available"},
    {"id": 130, "judul": "Harry Potter and the Philosopher's Stone", "penulis": "J.K. Rowling", "penerbit": "Bloomsbury", "tahun": 1997, "kota penerbitan": "London", "negara penerbitan": "UK", "dipinjam": 10, "status": "available"},
    {"id": 131, "judul": "The Lord of the Rings", "penulis": "J.R.R. Tolkien", "penerbit": "Allen & Unwin", "tahun": 1954, "kota penerbitan": "London", "negara penerbitan": "UK", "dipinjam": 9, "status": "available"},
    {"id": 132, "judul": "The Catcher in the Rye", "penulis": "J.D. Salinger", "penerbit": "Little, Brown and Company", "tahun": 1951, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 8, "status": "available"},
    {"id": 133, "judul": "Pride and Prejudice", "penulis": "Jane Austen", "penerbit": "T. Egerton", "tahun": 1813, "kota penerbitan": "London", "negara penerbitan": "UK", "dipinjam": 7, "status": "available"},
    {"id": 134, "judul": "To Kill a Mockingbird", "penulis": "Harper Lee", "penerbit": "J.B. Lippincott & Co.", "tahun": 1960, "kota penerbitan": "Philadelphia", "negara penerbitan": "USA", "dipinjam": 6, "status": "available"},
    {"id": 135, "judul": "Hujan Bulan Juni", "penulis": "Sapardi Djoko Damono", "penerbit": "Gramedia", "tahun": 1994, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 10, "status": "not available"},
    {"id": 136, "judul": "Surat Kecil untuk Tuhan", "penulis": "Agnes Davonar", "penerbit": "Inandra Published", "tahun": 2008, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 6, "status": "available"},
    {"id": 137, "judul": "Orang-orang Biasa", "penulis": "Andrea Hirata", "penerbit": "Bentang Pustaka", "tahun": 2019, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 7, "status": "available"},
    {"id": 138, "judul": "Mariposa", "penulis": "Luluk HF", "penerbit": "Coconut Books", "tahun": 2020, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 4, "status": "not available"},
    {"id": 139, "judul": "The Da Vinci Code", "penulis": "Dan Brown", "penerbit": "Doubleday", "tahun": 2003, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 4, "status": "available"},
    {"id": 140,"judul": "Angels and Demons", "penulis": "Dan Brown", "penerbit": "Pocket Books", "tahun": 2000, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 10, "status": "not available"},
    {"id": 141, "judul": "Inferno", "penulis": "Dan Brown", "penerbit": "Doubleday", "tahun": 2013, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 5, "status": "not available"},
    {"id": 142, "judul": "Gone Girl", "penulis": "Gillian Flynn", "penerbit": "Crown Publishing", "tahun": 2012, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 3, "status": "available"},
    {"id": 143, "judul": "Twilight", "penulis": "Stephenie Meyer", "penerbit": "Little, Brown and Company", "tahun": 2005, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 5, "status": "not available"},
    {"id": 144, "judul": "The Fault in Our Stars", "penulis": "John Green", "penerbit": "Dutton Books", "tahun": 2012, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 10, "status": "not available"},
    {"id": 145, "judul": "Looking for Alaska", "penulis": "John Green", "penerbit": "Dutton Books", "tahun": 2005, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 5, "status": "available"},
    {"id": 146, "judul": "A Thousand Splendid Suns", "penulis": "Khaled Hosseini", "penerbit": "Riverhead Books", "tahun": 2007, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 10, "status": "not available"},
    {"id": 147, "judul": "Eleanor Oliphant Is Completely Fine", "penulis": "Gail Honeyman", "penerbit": "HarperCollins", "tahun": 2017, "kota penerbitan": "London", "negara penerbitan": "UK", "dipinjam": 7, "status": "available"},
    {"id": 148, "judul": "The Girl on the Train", "penulis": "Paula Hawkins", "penerbit": "Riverhead Books", "tahun": 2015, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 3, "status": "available"} 
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
        print("\nKoleksi Buku di Perpustakaan Liswatun Naimah")
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
    print("\nTambah Kolesi Buku")
    
    try:
        id_buku = int(input("Masukkan ID Buku: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    # Validasi ID tidak boleh duplikat
    for buku in buku_database:
        if buku["id"] == id_buku:
            print("ID Buku sudah ada. Masukkan ID yang unik.")
            return

    judul = input("Masukkan Judul Buku: ").strip()
    penulis = input("Masukkan Nama Penulis: ").strip()
    penerbit = input("Masukkan Nama Penerbit: ").strip()
    try:
        tahun = int(input("Masukkan Tahun Terbit: "))
    except ValueError:
        print("Tahun harus berupa angka.")
        return

    # Menyimpan Data Buku Baru
    buku_baru = {"id": id_buku, "judul": judul, "penulis": penulis, "penerbit": penerbit, "tahun": tahun, "status": "available"}
    buku_database.append(buku_baru)

    print("\nBuku berhasil ditambahkan.")
    tampilkan_semua_buku()

# Update Data (Ubah Data Buku)
def update_data_buku():
    print("\nUpdate Data Buku")
    try:
        id_buku = int(input("Masukkan ID Buku yang ingin diperbarui: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    # Pencarian Buku
    for buku in buku_database:
        if buku["id"] == id_buku:
            print("\nData Buku Saat Ini:")
            print(tabulate([buku], headers="keys", tablefmt="grid"))

            kolom_update = input("\nMasukkan kolom yang ingin diupdate (judul/penulis/penerbit/tahun): ").strip().lower()
            if kolom_update not in ["judul", "penulis", "penerbit", "tahun"]:
                print("Kolom tidak valid.")
                return

            nilai_baru = input(f"Masukkan {kolom_update} baru: ").strip()
            buku[kolom_update] = nilai_baru if kolom_update != "tahun" else int(nilai_baru)

            print("\nData buku berhasil diperbarui.")
            tampilkan_semua_buku()
            return

    print("Buku dengan ID tersebut tidak ditemukan.")

# Fungsi Menghapus Data Buku
def hapus_data_buku():
    print("\nHapus Data Buku")
    try:
        id_buku = int(input("Masukkan ID Buku yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for buku in buku_database:
        if buku["id"] == id_buku:
            print("\nData Buku yang akan dihapus:")
            print(tabulate([buku], headers="keys", tablefmt="grid"))
            konfirmasi = input("\nApakah Anda yakin ingin menghapus buku ini? (y/n): ").strip().lower()
            if konfirmasi == 'y':
                buku_database.remove(buku)
                print("\nBuku berhasil dihapus.")
                return
            else:
                print("\nPenghapusan dibatalkan.")
                return

    print("Buku dengan ID tersebut tidak ditemukan.")

# Fungsi Manajemen Peminjaman & Pengembalian
def kelola_peminjaman():
    print("\nPeminjaman/Pengembalian Buku")
    try:
        id_buku = int(input("Masukkan ID Buku yang ingin dipinjam/dikembalikan: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for buku in buku_database:
        if buku["id"] == id_buku:
            if buku["status"] == "available":
                buku["status"] = "not available"
                print("\nBuku berhasil dipinjam.")
            else:
                buku["status"] = "available"
                print("\nBuku berhasil dikembalikan.")
            return

    print("Buku dengan ID tersebut tidak ditemukan.")

# Fungsi Utama untuk Menjalankan Program
def main():
    kata_sambutan()
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
