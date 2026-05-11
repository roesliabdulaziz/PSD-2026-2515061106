A. Judul Program
Program Pencarian Data Mahasiswa Berdasarkan NPM Menggunakan Sequential Search

B. Deskripsi Singkat
Program ini dibuat untuk mencari data mahasiswa berdasarkan NPM menggunakan algoritma Sequential Search. Sequential Search adalah algoritma pencarian yang dilakukan dengan cara mengecek data satu per satu dari indeks pertama sampai indeks terakhir.
Pada program ini, data mahasiswa disimpan dalam bentuk list yang berisi dictionary. Setiap dictionary memiliki data NPM, nama, dan kelas. Program akan meminta user memasukkan NPM yang ingin dicari, kemudian program akan membandingkan NPM tersebut dengan setiap data mahasiswa sampai data ditemukan atau sampai seluruh data selesai diperiksa.

C. Source Code
 
 

Def `sequential_search_mahasiswa` adalah Pendeklarasian fungsi `sequential_search_mahasiswa` dengan parameter `data_mahasiswa` dan `target_npm`, dimana `data_mahasiswa` digunakan untuk menampung seluruh data mahasiswa, sedangkan `target_npm` digunakan untuk menampung NPM yang ingin dicari oleh user. Dimulai dengan baris `for index in range(len(data_mahasiswa)):` yang berarti program melakukan perulangan dari indeks 0 sampai panjang data mahasiswa. Penggunaan `len(data_mahasiswa)` bertujuan agar jumlah perulangan mengikuti banyaknya data mahasiswa yang ada di dalam list.

Selanjutnya ada sintaks `print(f"Mengecek indeks ke-{index} dengan NPM {data_mahasiswa[index]['npm']}")` yang digunakan untuk menampilkan proses pencarian data. Penggunaan f-string bertujuan agar nilai variabel `index` dan NPM pada data mahasiswa bisa dimasukkan ke dalam teks output. Setelah itu ada percabangan `if data_mahasiswa[index]["npm"] == target_npm:` yang berarti program membandingkan NPM pada indeks yang sedang dicek dengan NPM yang dicari oleh user. Jika NPM tersebut sama, maka program menjalankan sintaks `return index` untuk mengembalikan indeks tempat data mahasiswa ditemukan.

Jika semua data sudah dicek tetapi NPM tidak ditemukan, maka akan dijalankan sintaks `return -1`. Nilai `-1` digunakan sebagai tanda bahwa data mahasiswa tidak ditemukan di dalam list.

Def `tampilkan_semua_data` Pendeklarasian fungsi `tampilkan_semua_data` dengan parameter `data_mahasiswa`, fungsi ini digunakan untuk menampilkan seluruh data mahasiswa sebelum proses pencarian dilakukan. Dimulai dengan sintaks `print("\nDaftar Data Mahasiswa:")` untuk menampilkan judul daftar data mahasiswa, dimana `\n` digunakan agar output berpindah ke baris baru. Lalu sintaks `print("-" * 60)` digunakan untuk membuat garis pembatas sebanyak 60 karakter agar tampilan output terlihat lebih rapi.

Selanjutnya ada sintaks `print(f"{'No':<5}{'NPM':<15}{'Nama':<20}{'Kelas':<10}")` untuk menampilkan header tabel yang berisi No, NPM, Nama, dan Kelas. Tanda `<5`, `<15`, `<20`, dan `<10` digunakan untuk mengatur lebar kolom supaya tampilan tabel menjadi sejajar. Setelah itu garis pembatas dicetak kembali menggunakan sintaks `print("-" * 60)`.

Lalu dibuat looping dengan sintaks `for i, mahasiswa in enumerate(data_mahasiswa, start=1):`, dimana `enumerate` digunakan untuk mengambil nomor urut dan isi data mahasiswa secara bersamaan. Parameter `start=1` digunakan agar nomor urut yang ditampilkan dimulai dari angka 1, bukan 0, karena indeks Python dimulai dari 0 sedangkan tampilan untuk user lebih mudah dibaca jika dimulai dari 1. Di dalam looping terdapat sintaks `print(f"{i:<5}{mahasiswa['npm']:<15}{mahasiswa['nama']:<20}{mahasiswa['kelas']:<10}")` yang digunakan untuk menampilkan nomor, NPM, nama, dan kelas dari setiap mahasiswa. Terakhir, `print("-" * 60)` digunakan lagi untuk menutup tabel dengan garis pembatas.

Def `main` Fungsi `main()` digunakan sebagai tempat jalannya program utama, dimulai dengan pembuatan variabel `data_mahasiswa` yang berisi list data mahasiswa. Di dalam list tersebut terdapat beberapa dictionary, contohnya `{"npm": "2365061001", "nama": "ghani jemping", "kelas": "A"}`. Setiap dictionary menyimpan satu data mahasiswa yang memiliki tiga key, yaitu `npm`, `nama`, dan `kelas`.

Selanjutnya ada sintaks `print(" PROGRAM PENCARIAN DATA MAHASISWA BERDASARKAN NPM")` untuk menampilkan judul program, lalu `print("              MENGGUNAKAN SEQUENTIAL SEARCH")` untuk menampilkan jenis algoritma yang digunakan, dan `print("======================================================")` untuk membuat garis pembatas agar tampilan program lebih rapi.

Setelah itu program memanggil fungsi `tampilkan_semua_data(data_mahasiswa)`. Pemanggilan fungsi ini bertujuan untuk menampilkan semua data mahasiswa yang tersedia sebelum user melakukan pencarian. Lalu terdapat sintaks `target_npm = input("\nMasukkan NPM mahasiswa yang ingin dicari: ")`, yang digunakan agar user bisa memasukkan NPM mahasiswa yang ingin dicari. Data input tersebut disimpan ke dalam variabel `target_npm`.

Selanjutnya ada sintaks `print("\nProses Sequential Search:")` untuk menampilkan keterangan bahwa proses pencarian akan dimulai. Setelah itu dibuat variabel `hasil_index` dengan sintaks `hasil_index = sequential_search_mahasiswa(data_mahasiswa, target_npm)`. Sintaks ini digunakan untuk memanggil fungsi `sequential_search_mahasiswa` dengan membawa data mahasiswa dan NPM target. Hasil pencarian akan disimpan ke dalam variabel `hasil_index`.

Lalu program menampilkan judul hasil pencarian dengan sintaks `print("\nHasil Pencarian:")`. Setelah itu terdapat percabangan `if hasil_index != -1:` yang berarti jika nilai `hasil_index` tidak sama dengan `-1`, maka data mahasiswa berhasil ditemukan. Jika kondisi tersebut benar, maka sintaks `mahasiswa = data_mahasiswa[hasil_index]` digunakan untuk mengambil data mahasiswa berdasarkan indeks yang ditemukan.

Kemudian program menampilkan hasil data mahasiswa dengan beberapa sintaks print, yaitu `print("Data mahasiswa ditemukan!")` untuk menampilkan pesan bahwa data ditemukan, `print(f"Indeks : {hasil_index}")` untuk menampilkan indeks data, `print(f"NPM    : {mahasiswa['npm']}")` untuk menampilkan NPM mahasiswa, `print(f"Nama   : {mahasiswa['nama']}")` untuk menampilkan nama mahasiswa, dan `print(f"Kelas  : {mahasiswa['kelas']}")` untuk menampilkan kelas mahasiswa.

Jika kondisi `hasil_index != -1` tidak terpenuhi, maka bagian `else` akan dijalankan. Di dalam bagian `else`, terdapat sintaks `print("Data mahasiswa tidak ditemukan.")` untuk menampilkan pesan bahwa data tidak ditemukan, lalu `print(f"NPM {target_npm} tidak terdapat dalam daftar mahasiswa.")` untuk menampilkan NPM yang dicari user dan menjelaskan bahwa NPM tersebut tidak ada pada daftar mahasiswa.

Terakhir ada sintaks `if __name__ == "__main__":` dan `main()` yang berarti program hanya akan menjalankan fungsi `main()` jika file Python ini dijalankan secara langsung. Tetapi jika file ini di-import oleh file Python lain, maka fungsi `main()` tidak akan otomatis dijalankan.
D. Output Program
 

Output ketika data ditemukan:
 




Output ketika data tidak ditemukan:
 

Program akan menampilkan data yang sudah tersimpan di dalam program dan meminta user untuk memasukkan NPM Mahasiswa yang ingin dicari, lalu program langsung akan mengecek satu persatu data yang ada di dalam program (selection sort) dan menampilkan hasilnya


E. Link YouTube
https://youtu.be/TAOPYXS0ReM


