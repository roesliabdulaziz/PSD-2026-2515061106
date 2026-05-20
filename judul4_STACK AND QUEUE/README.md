A. Judul Program :
Program Sistem Antrian Pasien Rumah Sakit Menggunakan Queue (Circular Array)


B. Deskripsi Singkat : 
Program ini dibuat untuk mengelola antrian pasien di rumah sakit menggunakan struktur data Queue berbasis Circular Array. Queue adalah struktur data yang menggunakan prinsip FIFO (First In, First Out), dimana elemen yang pertama kali masuk akan menjadi elemen pertama yang diproses. 
Pada program ini, data pasien disimpan dalam bentuk array (list) yang berisi dictionary. Setiap dictionary memiliki data nama dan keluhan pasien. Program akan meminta user memilih menu yang tersedia, seperti mendaftarkan pasien baru, memanggil pasien berikutnya, melihat pasien terdepan, menampilkan seluruh antrian, atau keluar dari program. Setiap operasi enqueue dan dequeue memiliki kompleksitas waktu O(1) karena akses data hanya dilakukan pada dua titik ujung yaitu front dan rear


C. Source Code  
  
<img width="468" height="420" alt="image" src="https://github.com/user-attachments/assets/e58170a4-2f63-4424-af8c-c9e6a6697d89" />

<img width="468" height="436" alt="image" src="https://github.com/user-attachments/assets/1b5a911c-cf29-4882-96a3-c427ae3385ac" />

<img width="468" height="436" alt="image" src="https://github.com/user-attachments/assets/bb7941d0-35f2-41c2-8e91-04c70c271c75" />

<img width="468" height="434" alt="image" src="https://github.com/user-attachments/assets/ca0187d5-d78f-4c5e-99ff-b7795fa0a0cf" />

<img width="468" height="278" alt="image" src="https://github.com/user-attachments/assets/827e9bf9-ed52-4292-855c-08a3132eaba0" />

Di baris pertama pendeklarasian kelas bernama QueueArray. Kelas ini merupakan blueprint untuk membuat objek antrian berbasis array melingkar (circular array). Seluruh operasi antrian seperti enqueue, dequeue, peek, dan display diimplementasikan di dalam kelas ini



def __init__(self, max_size=50): 

Selanjutnya ada pendeklarasian fungsi constructor __init__ dengan parameter self dan max_size=50. Parameter max_size=50 menentukan kapasitas maksimum antrian, dimana nilai default-nya adalah 50 slot. Fungsi ini otomatis dipanggil saat objek QueueArray pertama kali dibuat.

•	self.MAXN = max_size

Menyimpan nilai max_size ke dalam atribut self.MAXN. Atribut ini digunakan sebagai batas maksimum jumlah elemen yang bisa ditampung oleh antrian.

•	self.q = [None] * self.MAXN

Membuat list (array) berukuran MAXN yang seluruh elemennya berisi None. List ini berfungsi sebagai wadah penyimpanan data pasien. Penggunaan [None] * self.MAXN bertujuan untuk mengalokasikan slot memori sebanyak MAXN sejak awal program berjalan.

•	self.front_idx = -1

Menginisialisasi indeks elemen depan antrian dengan nilai -1. Nilai -1digunakan sebagai penanda bahwa antrian masih dalam keadaan kosong, belum ada elemen yang masuk.

•	self.rear_idx = -1

Menginisialisasi indeks elemen belakang antrian dengan nilai -1. Sama seperti front_idx, nilai -1 menandakan bahwa antrian masih kosong.



def is_empty(self):

Pendeklarasian fungsi is_empty dengan parameter self. Fungsi ini digunakan untuk memeriksa apakah antrian dalam keadaan kosong.

•	return self.front_idx == -1

Sintaks return self.front_idx == -1 akan mengembalikan nilai True jika front_idxbernilai -1 (antrian kosong), dan mengembalikan False jika front_idxmemiliki nilai lain (antrian ada isinya).



def is_full(self):

Pendeklarasian fungsi is_full dengan parameter self. Fungsi ini digunakan untuk memeriksa apakah antrian sudah penuh

•	return (self.rear_idx + 1) % self.MAXN == self.front_idx

menggunakan operasi modulo %karena ini adalah circular queue. Artinya, jika posisi satu langkah setelah rear_idx (secara melingkar) tepat sama dengan posisi front_idx, maka seluruh slot array sudah terisi dan antrian dinyatakan penuh. Fungsi mengembalikan True jika penuh dan False jika masih ada slot kosong.



def hitung_jumlah(self):

Pendeklarasian fungsi hitung_jumlah dengan parameter self. Fungsi ini digunakan untuk menghitung berapa banyak elemen (pasien) yang saat ini ada di dalam antrian.

•	if self.is_empty():
return 0

Percabangan pertama: jika antrian kosong (fungsi is_empty() mengembalikan True), maka langsung mengembalikan nilai 0 karena tidak ada elemen sama sekali.

•	if self.rear_idx >= self.front_idx:
            	return self.rear_idx - self.front_idx + 1

Percabangan kedua: jika rear_idx lebih besar atau sama dengan front_idx, maka jumlah elemen dihitung dengan rumus rear_idx - front_idx + 1. Ini adalah kondisi normal dimana data belum melingkar (wrap around).

•	else:
           		return self.MAXN - self.front_idx + self.rear_idx + 1

Jika rear_idx lebih kecil dari front_idx, berarti data sudah melingkar melewati ujung array. Maka jumlah elemen dihitung dengan rumus MAXN - front_idx + rear_idx + 1, yaitu sisa elemen dari front_idx sampai ujung array ditambah elemen dari awal array sampai rear_idx.



def daftar_pasien(self, nama, keluhan):

Pendeklarasian fungsi daftar_pasien dengan parameter self, nama, dan keluhan. Parameter nama digunakan untuk menampung nama pasien yang didaftarkan, sedangkan parameter keluhan digunakan untuk menampung keluhan medis pasien tersebut. Fungsi ini mengimplementasikan operasi EnQueue yaitu menambahkan elemen baru ke bagian belakang antrian

•	if self.is_full():
            print("Antrian penuh! Tidak dapat mendaftarkan pasien baru.")
            return

Percabangan untuk mengecek apakah antrian sudah penuh dengan memanggil fungsi is_full(). Jika antrian penuh, maka program mencetak pesan peringatan dan menjalankan return untuk keluar dari fungsi tanpa melakukan operasi apapun. Kondisi ini mencegah terjadinya overflow pada antrian

•	pasien = {'nama': nama, 'keluhan': keluhan}

Membuat sebuah dictionary bernama pasien yang berisi dua key yaitu 'nama'dan 'keluhan'. Dictionary ini menyimpan data satu pasien dalam satu kesatuan sehingga memudahkan pengelolaan data

•	if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0

Percabangan untuk mengecek apakah antrian masih kosong. Jika kosong (elemen pertama yang dimasukkan), maka front_idx dan rear_idx sama-sama diset ke 0, yang artinya elemen pertama ditempatkan di indeks 0 pada array

•	else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN

Jika antrian sudah memiliki elemen sebelumnya, maka rear_idx digeser maju satu posisi secara circular menggunakan operasi modulo % self.MAXN. Operasi modulo ini memastikan bahwa jika rear_idx sudah berada di posisi terakhir array (indeks MAXN-1), maka akan kembali ke indeks 0 (melingkar), bukan keluar dari batas array

•	self.q[self.rear_idx] = pasien

Menyimpan dictionary pasien ke dalam array self.q pada posisi rear_idx. Dengan demikian, data pasien baru selalu ditempatkan di bagian belakang antrian sesuai prinsip FIFO

•	 nomor_antrian = self.hitung_jumlah()

Memanggil fungsi hitung_jumlah() untuk mengetahui posisi antrian pasien yang baru saja didaftarkan. Hasilnya disimpan ke variabel nomor_antrian

•	print(f"Pasien berhasil didaftarkan!")
        	        print(f"  Nama          : {nama}")
        	        print(f"  Keluhan       : {keluhan}")
       	        print(f"  Nomor Antrian : {nomor_antrian}")

Menampilkan konfirmasi bahwa pendaftaran berhasil, beserta detail nama pasien, keluhan, dan nomor antrian. Penggunaan f-string bertujuan agar nilai variabel nama, keluhan, dan nomor_antrian bisa dimasukkan langsung ke dalam teks output.



def panggil_pasien(self):

Pendeklarasian fungsi panggil_pasien dengan parameter self. Fungsi ini mengimplementasikan operasi DeQueue yaitu menghapus elemen dari bagian depan antrian. Pasien yang pertama kali mendaftar akan menjadi pasien pertama yang dipanggil sesuai prinsip FIFO (First In, First Out)

•	if self.is_empty():
            	print("Antrian kosong! Tidak ada pasien yang menunggu.")
            	return

Percabangan untuk mengecek apakah antrian dalam keadaan kosong. Jika kosong, maka program mencetak pesan peringatan dan keluar dari fungsi menggunakan return. Kondisi ini mencegah terjadinya underflow pada antrian [[11]]

•	pasien = self.q[self.front_idx]

Mengambil data pasien yang berada di posisi paling depan antrian (front_idx) dan menyimpannya ke variabel pasien. Data ini berupa dictionary yang berisi nama dan keluhan pasien.

•	print(f"Memanggil pasien...")
        	        print(f"  Nama    : {pasien['nama']}")
                    print(f"  Keluhan : {pasien['keluhan']}")
                    print(f"Silakan menuju ruang pemeriksaan.")

Menampilkan informasi pasien yang sedang dipanggil. Penggunaan pasien['nama'] dan pasien['keluhan'] untuk mengakses value dari dictionary berdasarkan key-nya.

•	if self.front_idx == self.rear_idx:
           		self.front_idx = -1
            	self.rear_idx = -1

Percabangan untuk mengecek apakah hanya tersisa satu elemen dalam antrian (kondisi front_idx == rear_idx). Jika benar, setelah elemen tersebut dihapus maka antrian menjadi kosong, sehingga kedua indeks di-reset ke -1sebagai penanda antrian kosong.

•	else:
            	self.front_idx = (self.front_idx + 1) % self.MAXN

Jika masih ada elemen lain dalam antrian, maka front_idx digeser maju satu posisi secara circular menggunakan operasi modulo % self.MAXN. Dengan demikian, pasien berikutnya yang masuk lebih awal kini menjadi pasien terdepan.



def lihat_pasien_berikutnya(self):

Pendeklarasian fungsi lihat_pasien_berikutnya dengan parameter self. Fungsi ini mengimplementasikan operasi Peek yaitu melihat nilai elemen pada bagian depan antrian tanpa menghapusnya

•	if self.is_empty():
           		print("Antrian kosong! Tidak ada pasien yang menunggu.")
            	return

Percabangan untuk mengecek apakah antrian kosong. Jika kosong, cetak pesan peringatan dan keluar dari fungsi.

•	pasien = self.q[self.front_idx]

Mengambil data pasien yang berada di posisi paling depan (front_idx) tanpa menghapusnya dari antrian. Berbeda dengan panggil_pasien(), fungsi ini hanya membaca data tanpa mengubah posisi front_idx.

•	print(f"Pasien berikutnya yang akan dipanggil:")
        	        print(f"  Nama    : {pasien['nama']}")
        	        print(f"  Keluhan : {pasien['keluhan']}")

Menampilkan informasi pasien yang berada di posisi terdepan antrian. Data hanya ditampilkan tanpa dikeluarkan dari antrian.



def tampilkan_antrian(self):

Pendeklarasian fungsi tampilkan_antrian dengan parameter self. Fungsi ini digunakan untuk menampilkan seluruh data pasien yang sedang berada dalam antrian dari posisi depan ke belakang.

•	if self.is_empty():
            	print("Antrian kosong! Tidak ada pasien yang menunggu.")
            	return

Percabangan untuk mengecek apakah antrian kosong. Jika kosong, cetak pesan dan keluar.

•	print("Daftar Antrian Pasien Saat Ini:")
        	        print("-" * 50)

Menampilkan judul tabel daftar antrian. Sintaks print("-" * 50) digunakan untuk mencetak garis pembatas sepanjang 50 karakter agar tampilan tabel terlihat rapi

•	print(f"{'No':<5}{'Nama':<25}{'Keluhan':<20}")

Menampilkan header tabel yang berisi kolom No, Nama, dan Keluhan. Tanda <5, <25, dan <20 digunakan untuk mengatur lebar kolom (left-aligned) supaya tampilan tabel menjadi sejajar dan mudah dibaca.

•	print("-" * 50)

Mencetak garis pembatas kembali untuk memisahkan header dengan isi tabel.

•	i = self.front_idx
        	        idx = 1

Inisialisasi variabel i sebagai penunjuk posisi dalam array yang dimulai dari front_idx (elemen terdepan), dan variabel idx sebagai nomor urut tampilan yang dimulai dari angka 1

•	while True:

Membuat perulangan tak terbatas yang akan dihentikan secara manual menggunakan break ketika seluruh elemen sudah ditampilkan.

•	pasien = self.q[i]
                    print(f"{idx:<5}{pasien['nama']:<25}{pasien['keluhan']:<20}")

Mengambil data pasien pada posisi i dan menampilkan nomor urut, nama, serta keluhan pasien 
tersebut dalam format tabel yang rapi.

•	if i == self.rear_idx:
                	break

Percabangan untuk mengecek apakah posisi i sudah mencapai rear_idx(elemen terakhir). Jika benar, maka perulangan dihentikan dengan break karena semua elemen sudah ditampilkan.

•	i = (i + 1) % self.MAXN
                    idx += 1

Menggeser posisi i maju satu langkah secara circular menggunakan operasi modulo, dan menambah nomor urut idx sebesar 1 untuk elemen berikutnya.

•	print("-" * 50)
        	        print(f"Total pasien dalam antrian: {idx}")

Menutup tabel dengan garis pembatas dan menampilkan total jumlah pasien yang sedang menunggu dalam antrian.



def main():

Pendeklarasian fungsi main() yang digunakan sebagai tempat jalannya program utama. Fungsi ini berisi menu interaktif yang memungkinkan user memilih operasi yang ingin dilakukan

•	queue = QueueArray(max_size=50)

Membuat objek antrian baru dari kelas QueueArray dengan kapasitas maksimum 50 pasien. Objek ini disimpan ke variabel queue dan akan digunakan untuk seluruh operasi antrian selama program berjalan.

•	pilih = 0

Inisialisasi variabel pilih dengan nilai 0. Variabel ini digunakan untuk menyimpan pilihan menu yang dipilih oleh user.

•	while pilih != 5:

Membuat perulangan while yang akan terus berjalan selama user belum memilih menu nomor 5 (Keluar). Artinya setelah setiap operasi selesai, program akan kembali menampilkan menu dan menanyakan pilihan user lagi.

•	print("\n=== SISTEM ANTRIAN RUMAH SAKIT ===")
        print("1. Daftarkan Pasien Baru")
        print("2. Panggil Pasien Berikutnya")
        print("3. Lihat Pasien Berikutnya")
        print("4. Tampilkan Seluruh Antrian")
        print("5. Keluar")

Menampilkan menu utama program yang berisi 5 pilihan. Penggunaan \n pada baris pertama bertujuan agar output berpindah ke baris baru sehingga ada jarak antara hasil operasi sebelumnya dengan menu yang baru ditampilkan.

•	try:
            	pilih = int(input("Pilih menu: "))
        	        except ValueError:
            	print("Input tidak valid!")
                    continue

Meminta user memasukkan pilihan menu menggunakan input(), kemudian mengkonversi input tersebut menjadi integer dengan int(). Seluruh proses ini dibungkus dalam blok try-except untuk menangani error ValueError. Jika user memasukkan huruf atau karakter yang bukan angka, maka program akan mencetak pesan "Input tidak valid!" dan menjalankan continue untuk kembali ke awal perulangan while tanpa mengeksekusi kode di bawahnya.

•	if pilih == 1:
            	nama = input("Masukkan nama pasien: ")
            	keluhan = input("Masukkan keluhan: ")
            	queue.daftar_pasien(nama, keluhan)

Percabangan pertama: jika user memilih menu 1, maka program meminta input nama pasien dan keluhan pasien. Kedua input tersebut disimpan ke variabel nama dan keluhan, kemudian program memanggil fungsi daftar_pasien()pada objek queue dengan membawa kedua data tersebut sebagai argumen.

•	elif pilih == 2:
            	queue.panggil_pasien()

Percabangan kedua: jika user memilih menu 2, maka program memanggil fungsi panggil_pasien() untuk mengeluarkan pasien terdepan dari antrian dan menampilkan datanya

•	elif pilih == 3:
            	queue.lihat_pasien_berikutnya()

Percabangan ketiga: jika user memilih menu 3, maka program memanggil fungsi lihat_pasien_berikutnya() untuk melihat data pasien terdepan tanpa mengeluarkannya dari antrian.

•	elif pilih == 4:
            	queue.tampilkan_antrian()

Percabangan keempat: jika user memilih menu 4, maka program memanggil fungsi tampilkan_antrian() untuk menampilkan seluruh data pasien yang sedang menunggu dalam antrian.

•	elif pilih == 5:
            	print("Program selesai. Terima kasih!")

Percabangan kelima: jika user memilih menu 5, maka program mencetak pesan penutup. Setelah ini, kondisi while pilih != 5 tidak lagi terpenuhi sehingga perulangan berhenti dan program berakhir.

•	else:
            	print("Pilihan tidak valid!")

Jika user memasukkan angka selain 1 sampai 5, maka bagian else akan dijalankan dan menampilkan pesan bahwa pilihan tidak valid. Program kemudian kembali ke awal perulangan untuk menampilkan menu lagi.

•	if __name__ == "__main__":
        main()

Sintaks ini memastikan bahwa fungsi main() hanya akan dijalankan jika file P1ython ini dieksekusi secara langsung. Tetapi jika file ini di-import oleh file P1ython lain, maka fungsi main() tidak akan otomatis dijalankan. Variabel __name__secara otomatis bernilai "__main__" ketika file dijalankan langsung oleh interpreter P1ython.


 
D.Output Program
Dengan memasukkan 2 pasien ke antrian 

<img width="468" height="107" alt="image" src="https://github.com/user-attachments/assets/136bb09b-bae7-4715-93ff-42eb318481db" />
 

Pilih 1:
 
<img width="468" height="133" alt="image" src="https://github.com/user-attachments/assets/215c92e4-899f-4038-8a15-7870587fa954" />

Pilih 2:
 
<img width="468" height="109" alt="image" src="https://github.com/user-attachments/assets/a1aabc60-34e3-4819-addc-a128ee5a1e83" />

Pilih 3:

<img width="468" height="98" alt="image" src="https://github.com/user-attachments/assets/b967324d-1005-44f0-8d35-9d7c4240f19f" />
 
Pilih 4:  

<img width="468" height="120" alt="image" src="https://github.com/user-attachments/assets/4b3cb7ec-7573-4f3f-b8de-a5f56deaa585" />

Pilih 5:
 
<img width="468" height="45" alt="image" src="https://github.com/user-attachments/assets/17b5e65a-665f-4a19-9cf7-3072fd94597a" />

E. Link youtube 
 https://youtu.be/ppGht59pWCU
 


