A. JUDUL PROGRAM : Program Implementasi Struktur Data Dasar Python 

B. Deskripsi singkat : Kode ini adalah program sederhana untuk membuat sistem antrian pasien di rumah sakit menggunakan Python. Program ini memakai struktur data single linked list, yaitu setiap data pasien disimpan dalam sebuah node yang berisi nama, keluhan, dan penunjuk ke data pasien berikutnya.
 
Program ini bekerja seperti antrian pada umumnya, yaitu pasien yang pertama mendaftar akan dipanggil lebih dulu atau menggunakan prinsip FIFO (First In, First Out). Di dalam program, pengguna bisa mendaftarkan pasien baru, memanggil pasien berikutnya, melihat daftar antrian yang sedang menunggu, dan keluar dari sistem.

C. Source code 

<img width="468" height="221" alt="image" src="https://github.com/user-attachments/assets/767d2fef-5466-45b2-8940-62cee6e16bf8" />
<img width="468" height="235" alt="image" src="https://github.com/user-attachments/assets/8d516b0c-e5a0-4b01-ba23-aba2cc7b6b81" />
<img width="468" height="262" alt="image" src="https://github.com/user-attachments/assets/e070ea92-c53d-4915-91ea-6e49ac078a1a" />


BAGIAN 1. CLASS NODE

class Node: adalah bagian yang digunakan untuk membuat satu data pasien dalam antrian. Bisa dibilang, setiap pasien yang mendaftar akan dibuat sebagai satu node. def __init__(self, nama, keluhan): adalah fungsi awal yang otomatis berjalan ketika node baru dibuat. self.nama = nama digunakan untuk menyimpan nama pasien. self.keluhan = keluhan digunakan untuk menyimpan keluhan pasien. Lalu self.next = None digunakan untuk menunjuk ke node berikutnya. Awalnya bernilai Nonekarena saat pasien baru dibuat, dia belum terhubung dengan pasien lain di antrian.

BAGIAN 2. CLASS ANTRIAN RUMAH SAKIT

class AntrianRumahSakit: adalah class utama yang dipakai untuk mengatur sistem antrian pasien. Di bagian ini, program menggunakan konsep linked list, lebih tepatnya single linked list, karena setiap node hanya punya satu penunjuk ke node berikutnya. def __init__(self): adalah fungsi awal untuk class antrian yang otomatis berjalan saat objek antrian dibuat. self.head = None digunakan untuk menandai pasien paling depan dalam antrian, sedangkan self.tail = None digunakan untuk menandai pasien paling belakang. Di awal, keduanya bernilai None karena belum ada pasien yang masuk ke antrian.

BAGIAN 3. DAFTAR PASIEN BARU

def daftar_pasien(self, nama, keluhan): adalah method yang digunakan untuk menambahkan pasien baru ke dalam antrian. new_node = Node(nama, keluhan) berarti program membuat node baru yang berisi nama dan keluhan pasien. Setelah itu, if self.head is None: digunakan untuk mengecek apakah antrian masih kosong atau belum. Kalau masih kosong, maka self.head = new_node membuat pasien baru menjadi pasien pertama, dan self.tail = new_node juga membuat pasien tersebut menjadi pasien terakhir, karena memang baru ada satu pasien. Tapi kalau antrian sudah ada isinya, bagian else: akan dijalankan. self.tail.next = new_node artinya pasien terakhir yang lama akan disambungkan ke pasien baru. Setelah itu, self.tail = new_nodedigunakan untuk memperbarui posisi tail agar menunjuk ke pasien yang baru masuk. Terakhir, print(f"✅ {nama} berhasil mendaftar. Keluhan: {keluhan}") hanya untuk menampilkan pesan bahwa pasien berhasil didaftarkan.

BAGIAN 4. PANGGIL PASIEN

def panggil_pasien(self): adalah method untuk memanggil pasien yang berada di antrian paling depan. if self.head is None:digunakan untuk mengecek apakah antrian kosong. Kalau kosong, program akan menampilkan print("⚠️ Antrian pasien kosong"), yang berarti tidak ada pasien yang bisa dipanggil. Kalau antrian tidak kosong, program masuk ke bagian else:. nama = self.head.nama digunakan untuk mengambil nama pasien paling depan, dan keluhan = self.head.keluhan digunakan untuk mengambil keluhannya. Setelah itu, self.head = self.head.next membuat posisi head berpindah ke pasien berikutnya. Jadi pasien yang tadi dipanggil sudah dianggap keluar dari antrian. Kemudian if self.head is None: mengecek apakah setelah pasien dipanggil ternyata antrian menjadi kosong. Kalau iya, self.tail = None juga dikosongkan supaya data antrian benar-benar bersih. Terakhir, print(f"🔔 Memanggil: {nama} | Keluhan: {keluhan} — Silakan masuk ke ruang dokter") digunakan untuk menampilkan pasien yang sedang dipanggil.

BAGIAN 5. TAMPILKAN ANTRIAN

def tampilkan_antrian(self): adalah method untuk menampilkan daftar pasien yang masih menunggu. if self.head is None:digunakan untuk mengecek apakah antrian kosong. Kalau kosong, program menampilkan print("Antrian kosong"), lalu returndigunakan supaya fungsi berhenti dan tidak lanjut ke proses berikutnya. Kalau antrian tidak kosong, current = self.headdigunakan sebagai variabel bantu untuk mulai membaca data dari pasien paling depan. nomor = 1 digunakan untuk memberi nomor urut antrian. print(" Daftar Antrian Pasien:") menampilkan judul daftar antrian. Lalu while current: berarti selama masih ada node pasien, program akan terus menampilkan datanya. print(f" {nomor}. {current.nama} - {current.keluhan}")menampilkan nomor antrian, nama pasien, dan keluhannya. Setelah itu, current = current.next digunakan untuk pindah ke pasien berikutnya, dan nomor += 1 digunakan untuk menaikkan nomor antrian.

BAGIAN 6. FUNGSI MAIN

def main(): adalah fungsi utama dari program ini. Di dalamnya ada antrian = AntrianRumahSakit(), yang berarti kita membuat objek antrian baru dari class AntrianRumahSakit. Setelah itu, while True: digunakan supaya menu program terus muncul berulang-ulang sampai pengguna memilih keluar. Bagian print() digunakan untuk menampilkan menu seperti daftar pasien baru, panggil pasien berikutnya, lihat antrian, dan keluar dari program. Lalu pilih = input("Pilih: ") digunakan untuk mengambil input dari pengguna, yaitu menu mana yang ingin dijalankan.

BAGIAN 7. PILIHAN MENU

Pada bagian ini, program mengecek pilihan yang dimasukkan oleh pengguna. if pilih == "1": berarti jika pengguna memilih angka 1, maka program akan meminta nama pasien dengan nama = input("Nama pasien: ") dan keluhan pasien dengan keluhan = input("Keluhan: "). Setelah itu, antrian.daftar_pasien(nama, keluhan) dipanggil untuk memasukkan pasien ke dalam antrian. elif pilih == "2": digunakan jika pengguna ingin memanggil pasien berikutnya, lalu program menjalankan antrian.panggil_pasien(). elif pilih == "3": digunakan untuk melihat daftar antrian, lalu program menjalankan antrian.tampilkan_antrian(). elif pilih == "4":digunakan untuk keluar dari program. Program akan menampilkan print("Sistem antrian ditutup."), lalu break digunakan untuk menghentikan perulangan. Kalau pengguna memasukkan pilihan selain 1 sampai 4, maka bagian else: akan dijalankan dan program menampilkan print("Pilihan tidak valid").

BAGIAN 8. MENJALANKAN PROGRAM

if __name__ == "__main__": digunakan untuk memastikan bahwa fungsi main() hanya dijalankan kalau file Python ini dijalankan secara langsung. Jadi kalau file ini diimpor ke file Python lain, program tidak langsung berjalan otomatis. Terakhir, main() digunakan untuk memulai seluruh program antrian rumah sakit. Secara keseluruhan, program ini menerapkan konsep linked list untuk membuat sistem antrian sederhana, di mana pasien yang pertama masuk akan menjadi pasien pertama yang dipanggil, sesuai prinsip FIFO atau First In, First Out.

D. Output program 

 <img width="366" height="144" alt="image" src="https://github.com/user-attachments/assets/f0296bb5-8675-44ee-ac5d-097eb0482c87" />

<img width="468" height="95" alt="image" src="https://github.com/user-attachments/assets/187ce513-576c-48fd-8dc7-b4984016fcca" />

<img width="468" height="107" alt="image" src="https://github.com/user-attachments/assets/f295bb67-cfed-41e1-89ab-d6df9804520f" />
 
<img width="468" height="107" alt="image" src="https://github.com/user-attachments/assets/f9239af8-8b77-4cfb-b3f5-4424430d8e3d" />
 
<img width="468" height="95" alt="image" src="https://github.com/user-attachments/assets/5ead067e-923b-470d-b1bc-30aabffce119" />

Program akan menampilkan opsi 1-4 setiap kali dijalankan dan user akan memilih angka tersebut untuk menggunakan fitur yang disediakan, output akan berubah sesuai dengan opsi yang dipilih

PROGRAM MULAI :

Pilih fitur sesuai opsi yang tertera

Jika pilih 1:
Program akan menjalankan menu daftar pasien baru. Pertama, program meminta pengguna memasukkan nama pasien melalui nama = input("Nama pasien: "). Setelah itu, program meminta pengguna memasukkan keluhan pasien melalui keluhan = input("Keluhan: "). Jika nama dan keluhan sudah diisi, program akan menjalankan antrian.daftar_pasien(nama, keluhan), yaitu memasukkan pasien baru ke dalam antrian.

Jika pilih 2:
Program akan menjalankan menu panggil pasien berikutnya. Pada bagian ini, program memanggil fungsi antrian.panggil_pasien(). Fungsi ini akan mengambil pasien yang berada di posisi paling depan dalam antrian. Jika ada pasien, maka pasien tersebut akan dipanggil dan keluar dari antrian. Tetapi jika antrian kosong, program akan menampilkan pesan bahwa antrian pasien kosong.

Jika pilih 3:
Program akan menjalankan menu lihat antrian. Program memanggil fungsi antrian.tampilkan_antrian(), yang tugasnya menampilkan semua pasien yang masih menunggu. Data yang ditampilkan berupa nomor urut, nama pasien, dan keluhan pasien. Jika belum ada pasien yang mendaftar, program akan menampilkan pesan bahwa antrian kosong.

Jika pilih 4:
Program akan menjalankan menu keluar dari sistem. Program menampilkan pesan Sistem antrian ditutup., lalu menjalankan break untuk menghentikan perulangan menu. Setelah itu, program selesai dijalankan.

Jika pilihan selain 1 sampai 4:
Program akan masuk ke bagian else, lalu menampilkan pesan Pilihan tidak valid. Artinya, pengguna memasukkan pilihan yang tidak tersedia di menu, sehingga program meminta pengguna memilih ulang.

E.Video Penjelasan
https://youtu.be/JwFM1Xd497I?si=sIsUq-QDkstwTkCQ
