A. Judul Program : Program Pengelola Data Pasien Rumah Sakit Menggunakan Hash Map Separate Chaining

B. Deskripsi singkat:

Program ini digunakan untuk menyimpan dan mengelola data pasien rumah sakit berdasarkan ID pasien. Data yang disimpan meliputi ID pasien, nama pasien, umur, diagnosa, dan nama dokter yang menangani pasien tersebut.

Struktur data yang digunakan adalah Hash Map dengan metode Separate Chaining. Metode ini dipilih karena data pasien dapat bertambah, dicari, diubah, dan dihapus sewaktu-waktu. Jika terjadi collision atau tabrakan indeks, data pasien tidak akan menimpa data lain, tetapi disimpan dalam linked list pada slot hash table yang sama.

Pada program ini, ID pasien digunakan sebagai key, sedangkan data lengkap pasien digunakan sebagai value. Fungsi hash akan mengubah ID pasien menjadi indeks tabel menggunakan operasi modulo. Apabila beberapa ID pasien menghasilkan indeks yang sama, maka node pasien baru akan dimasukkan ke rantai linked list pada indeks tersebut.

C. Source code
<img width="759" height="776" alt="Screenshot 2026-06-08 at 23 16 33" src="https://github.com/user-attachments/assets/46e7f52e-fd00-48da-9b7d-3c8053f9ee51" />

<img width="759" height="776" alt="Screenshot 2026-06-08 at 23 16 52" src="https://github.com/user-attachments/assets/e47a0b75-c0f7-49c9-a310-798080c6df50" />

<img width="759" height="799" alt="Screenshot 2026-06-08 at 23 17 58" src="https://github.com/user-attachments/assets/96b1a05c-7d84-45ad-853a-6d9e18d73dec" />

<img width="759" height="812" alt="Screenshot 2026-06-08 at 23 18 19" src="https://github.com/user-attachments/assets/dc52911f-817b-4ac5-8711-e6a5626fc726" />

<img width="759" height="796" alt="Screenshot 2026-06-08 at 23 18 59" src="https://github.com/user-attachments/assets/f2b7a36d-0682-45d9-ae61-e58434e1c6d7" />

<img width="759" height="796" alt="Screenshot 2026-06-08 at 23 19 28" src="https://github.com/user-attachments/assets/e029f190-fd8a-45b2-aee7-12a879f825ae" />

<img width="759" height="613" alt="Screenshot 2026-06-08 at 23 19 46" src="https://github.com/user-attachments/assets/0acf9a51-971c-4497-b62d-cf365cf73153" />


Class Pasien adalah pendeklarasian kelas yang berfungsi untuk menyimpan data lengkap seorang pasien. Di dalam class ini terdapat fungsi `__init__(self, id_pasien, nama, umur, diagnosa, dokter)`, yaitu konstruktor yang otomatis dijalankan ketika objek pasien dibuat. Parameter `id_pasien` digunakan sebagai nomor identitas pasien, `nama` digunakan untuk menyimpan nama pasien, `umur` digunakan untuk menyimpan umur pasien, `diagnosa` digunakan untuk menyimpan penyakit atau keluhan pasien, dan `dokter` digunakan untuk menyimpan nama dokter yang menangani pasien.

Class Node adalah pendeklarasian kelas yang digunakan untuk membentuk satu simpul pada linked list di dalam hash table. Setiap node memiliki `key`, `value`, dan `next`. Atribut `key` berisi ID pasien, atribut `value` berisi objek Pasien, sedangkan atribut `next` digunakan sebagai penghubung menuju node berikutnya jika terjadi collision pada indeks yang sama.

Class HashMapPasien adalah class utama yang digunakan untuk mengelola seluruh data pasien dalam bentuk hash map. Pada fungsi `__init__(self, size=10)`, program membuat tabel hash dengan ukuran awal 10 slot. Sintaks `self.table = [None] * self.size` digunakan untuk membuat list kosong yang nantinya akan menampung node pasien. Atribut `self.jumlah_data` digunakan untuk menghitung jumlah pasien yang tersimpan.

Def `hash_function` adalah fungsi yang digunakan untuk mengubah ID pasien menjadi indeks hash table. Rumus yang digunakan adalah `(key % self.size + self.size) % self.size`. Dengan rumus ini, ID pasien akan dipetakan ke indeks antara 0 sampai ukuran tabel dikurangi 1.

Def `insert` adalah fungsi yang digunakan untuk menambahkan data pasien baru ke dalam hash map. Program terlebih dahulu menghitung indeks menggunakan fungsi hash. Setelah itu, program menelusuri linked list pada indeks tersebut untuk memastikan ID pasien belum tersimpan. Jika ID sudah ada, fungsi mengembalikan `False` agar data tidak diduplikasi. Jika belum ada, program membuat node baru dan memasukkannya ke bagian awal linked list pada slot tersebut.

Def `search` adalah fungsi yang digunakan untuk mencari data pasien berdasarkan ID pasien. Program menghitung indeks dari ID pasien, kemudian menelusuri linked list pada slot tersebut. Jika key yang dicari sama dengan key pada node, maka program mengembalikan data pasien. Jika pencarian sampai akhir linked list dan data tidak ditemukan, maka fungsi mengembalikan `None`.

Def `update` adalah fungsi yang digunakan untuk mengubah data pasien. Program mencari pasien terlebih dahulu menggunakan fungsi `search`. Jika pasien tidak ditemukan, fungsi mengembalikan `False`. Jika pasien ditemukan, nama, umur, diagnosa, dan dokter akan diganti dengan data baru, lalu fungsi mengembalikan `True`.

Def `remove_key` adalah fungsi yang digunakan untuk menghapus data pasien berdasarkan ID pasien. Program mencari node pasien pada linked list di indeks hasil hash. Jika node berada di awal rantai, maka slot tabel langsung diarahkan ke node berikutnya. Jika node berada di tengah atau akhir rantai, maka node sebelumnya diarahkan ke node setelah node yang dihapus. Setelah data berhasil dihapus, jumlah data pasien dikurangi satu.

Def `get_all_patients` adalah fungsi yang digunakan untuk mengambil seluruh data pasien dari hash table. Program memeriksa setiap slot tabel, lalu menelusuri linked list pada slot tersebut. Semua data pasien dimasukkan ke dalam list, kemudian diurutkan berdasarkan ID pasien agar tampilan lebih rapi.

Def `count_collision_slots` adalah fungsi yang digunakan untuk menghitung jumlah slot yang mengalami collision. Sebuah slot dianggap mengalami collision apabila panjang linked list pada slot tersebut lebih dari satu node. Fungsi ini berguna untuk melihat apakah distribusi data pada hash table masih baik.

Def `load_factor` adalah fungsi yang digunakan untuk menghitung perbandingan antara jumlah data pasien dan ukuran tabel. Load factor dapat digunakan untuk melihat tingkat kepadatan hash table. Semakin besar load factor, semakin besar kemungkinan collision terjadi.

Def `display_table` adalah fungsi yang digunakan untuk menampilkan isi hash table secara langsung. Setiap indeks tabel ditampilkan dari 0 sampai 9. Jika sebuah slot kosong, program menampilkan `NONE`. Jika sebuah slot berisi data pasien, program menampilkan ID dan nama pasien dalam bentuk rantai linked list.

Def `baca_id` adalah fungsi yang digunakan untuk membaca input ID pasien. Fungsi ini memastikan ID pasien berupa bilangan bulat dan lebih besar dari 0. Jika input tidak valid, program menampilkan pesan kesalahan dan mengembalikan `None`.

Def `baca_umur` adalah fungsi yang digunakan untuk membaca input umur pasien. Fungsi ini memastikan umur berupa bilangan bulat dan berada pada rentang 0 sampai 120. Jika input tidak valid, program tidak melanjutkan proses penyimpanan data.

Def `baca_teks` adalah fungsi yang digunakan untuk membaca input teks seperti nama pasien, diagnosa, dan nama dokter. Fungsi ini memastikan data teks tidak kosong. Jika user hanya menekan enter tanpa mengisi data, program menampilkan pesan kesalahan.

Def `input_data_pasien` adalah fungsi yang digunakan untuk membaca seluruh data pasien. Fungsi ini memanggil `baca_teks` untuk nama, diagnosa, dan dokter, serta memanggil `baca_umur` untuk umur. Jika semua input valid, fungsi mengembalikan objek Pasien baru.

Def `tampilkan_pasien` adalah fungsi yang digunakan untuk menampilkan detail satu pasien. Data yang ditampilkan adalah ID pasien, nama, umur, diagnosa, dan dokter.

Def `tampilkan_daftar_pasien` adalah fungsi yang digunakan untuk menampilkan seluruh pasien yang tersimpan. Jika data pasien masih kosong, program menampilkan pesan bahwa data pasien masih kosong. Jika terdapat data, setiap pasien akan ditampilkan dengan pembatas agar lebih mudah dibaca.

Def `tampilkan_menu` adalah fungsi yang digunakan untuk menampilkan daftar fitur program. Menu yang tersedia adalah tambah data pasien, cari data pasien, ubah data pasien, hapus data pasien, tampilkan semua pasien, tampilkan isi hash table, tampilkan statistik hash map, dan keluar.

Def `main` adalah fungsi utama tempat program dijalankan. Pada awal fungsi, program membuat objek `HashMapPasien`. Setelah itu, program menjalankan perulangan `while True` agar menu terus tampil sampai user memilih menu keluar. Setiap pilihan menu akan menjalankan fungsi yang sesuai.

Pada menu 1, program meminta ID pasien dan data lengkap pasien. Jika ID belum tersimpan, data pasien akan dimasukkan ke hash map. Jika ID sudah ada, program menolak penyimpanan agar tidak terjadi duplikasi data.

Pada menu 2, program meminta ID pasien yang ingin dicari. Jika data ditemukan, detail pasien akan ditampilkan. Jika tidak ditemukan, program menampilkan pesan bahwa data pasien tidak tersedia.

Pada menu 3, program meminta ID pasien yang ingin diubah. Jika data ditemukan, user diminta memasukkan data baru. Setelah itu, data lama akan diganti dengan data baru.

Pada menu 4, program meminta ID pasien yang ingin dihapus. Jika data ditemukan, node pasien akan dihapus dari linked list pada slot hash table. Jika data tidak ditemukan, program menampilkan pesan bahwa data pasien tidak tersedia.

Pada menu 5, program menampilkan semua pasien yang tersimpan. Data ditampilkan secara terurut berdasarkan ID pasien agar lebih mudah diperiksa.

Pada menu 6, program menampilkan bentuk hash table secara langsung. Menu ini memperlihatkan bagaimana data pasien disimpan di dalam slot hash table dan bagaimana collision ditangani menggunakan linked list.

Pada menu 7, program menampilkan statistik hash map, yaitu jumlah pasien, ukuran tabel, load factor, dan jumlah slot yang mengalami collision.

Pada menu 8, program menampilkan pesan penutup dan menjalankan `break` untuk menghentikan perulangan, sehingga program selesai.

Terakhir terdapat sintaks `if __name__ == "__main__":` dan `main()`, yang berarti fungsi utama hanya dijalankan ketika file Python dieksekusi secara langsung.

D. Output Program

menu

<img width="332" height="149" alt="Screenshot 2026-06-08 at 23 21 23" src="https://github.com/user-attachments/assets/e5ed06b2-8d38-499f-a73b-b7f467ef22ae" />

1. Tambah data pasien
<img width="340" height="114" alt="Screenshot 2026-06-08 at 23 21 50" src="https://github.com/user-attachments/assets/c2ee7951-ff89-499a-ac1d-8faf708cc266" />
<img width="340" height="100" alt="Screenshot 2026-06-08 at 23 24 51" src="https://github.com/user-attachments/assets/1583d4b0-8a55-473f-a0ed-9a740d12bff2" />
<img width="340" height="100" alt="Screenshot 2026-06-08 at 23 24 40" src="https://github.com/user-attachments/assets/da31cdb1-8725-4632-b679-aa3ca0211952" />

2. Cari data pasien
<img width="340" height="138" alt="Screenshot 2026-06-08 at 23 25 12" src="https://github.com/user-attachments/assets/ac6e264d-90b7-43df-985f-8ca99c96afd7" />

3. Ubah data pasien
<img width="340" height="111" alt="Screenshot 2026-06-08 at 23 26 09" src="https://github.com/user-attachments/assets/13d50fd0-0ac8-4bbf-99a6-ccb0b36b49b1" />

4. Hapus data pasien
<img width="340" height="46" alt="Screenshot 2026-06-08 at 23 26 32" src="https://github.com/user-attachments/assets/1e18f7ab-2f7e-45b0-9118-bf3de0f759db" />

5. Tampilkan semua pasien
<img width="340" height="218" alt="Screenshot 2026-06-08 at 23 26 56" src="https://github.com/user-attachments/assets/9d5e3d25-127b-416b-8f9f-8713a2010eaf" />

6. Tampilkan isi hash table
<img width="340" height="187" alt="Screenshot 2026-06-08 at 23 27 18" src="https://github.com/user-attachments/assets/afacb382-1688-4bfe-8350-a5e355c1dd30" />

7. Tampilkan statistik hash map
<img width="340" height="78" alt="Screenshot 2026-06-08 at 23 27 41" src="https://github.com/user-attachments/assets/53358b7b-47bc-489f-8db8-11c0ace2d10e" />

8. Keluar
<img width="340" height="33" alt="Screenshot 2026-06-08 at 23 28 16" src="https://github.com/user-attachments/assets/635d35ff-bb24-4374-9d6d-a192f8ffd437" />

E. Link Youtube
https://youtu.be/w2Mc6JPQLyo


