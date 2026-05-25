A. Judul Program : Program Pengelola Nilai Ujian Menggunakan Binary Search Tree (BST)

B. Deskripsi singkat:
Program ini digunakan untuk menyimpan dan mengelola kumpulan nilai ujian unik pada rentang 0 sampai 100. Pengguna dapat menambahkan nilai, mencari nilai tertentu, menampilkan nilai secara terurut, melihat urutan traversal, serta memperoleh nilai minimum, maksimum, jumlah, total, dan rata-rata.
Struktur data yang digunakan adalah Binary Search Tree (BST). Setiap nilai yang lebih kecil dari suatu node disimpan pada cabang kiri, sedangkan nilai yang lebih besar disimpan pada cabang kanan. Karena itu, traversal inorder dapat menghasilkan urutan nilai dari kecil ke besar.

C.Source code

<img width="679" height="801" alt="Screenshot 2026-05-25 at 14 31 39" src="https://github.com/user-attachments/assets/c9a9c9e4-fda0-40a3-a2f5-199eaedad504" />

<img width="679" height="776" alt="Screenshot 2026-05-25 at 14 30 31" src="https://github.com/user-attachments/assets/ad827a98-9dff-421c-b026-9043720acc46" />

<img width="679" height="792" alt="Screenshot 2026-05-25 at 14 33 22" src="https://github.com/user-attachments/assets/78c67fd8-8e26-4180-9cb7-49881ee1c34a" />

<img width="679" height="792" alt="Screenshot 2026-05-25 at 14 34 21" src="https://github.com/user-attachments/assets/1640c536-41d9-4efd-9297-8ab80151a5da" />

<img width="679" height="344" alt="Screenshot 2026-05-25 at 14 35 43" src="https://github.com/user-attachments/assets/eeb7b659-56cc-4847-8034-78faa50c0780" />

Class Node adalah pendeklarasian kelas yang berfungsi untuk membentuk satu simpul atau node pada Binary Search Tree. Di dalam kelas ini terdapat fungsi __init__(self, nilai), yaitu konstruktor yang otomatis dijalankan setiap kali node baru dibuat. Parameter nilai digunakan untuk menampung nilai ujian yang akan disimpan pada node. Sintaks self.nilai = nilai digunakan untuk menyimpan nilai tersebut, sedangkan self.left = None dan self.right = None digunakan untuk menyiapkan penghubung menuju anak kiri dan anak kanan. Nilai None berarti pada awalnya node belum memiliki anak.

Class BSTNilai adalah pendeklarasian kelas yang digunakan untuk mengelola seluruh struktur Binary Search Tree pada program. Di dalam fungsi __init__(self) terdapat sintaks self.root = None, yang berarti ketika objek BST pertama kali dibuat, pohon masih kosong karena belum memiliki node akar atau root. Root ini nantinya menjadi titik awal untuk proses penambahan, pencarian, dan traversal nilai.

Def _insert_node adalah pendeklarasian fungsi bantuan dengan parameter root dan nilai, dimana root digunakan untuk menampung node yang sedang diperiksa, sedangkan nilai digunakan untuk menampung nilai baru yang ingin dimasukkan oleh user. Dimulai dengan percabangan if root is None: yang berarti apabila posisi node yang sedang diperiksa masih kosong, maka program menjalankan sintaks return Node(nilai), True. Sintaks Node(nilai) digunakan untuk membuat node baru, sedangkan nilai True menjadi tanda bahwa nilai berhasil ditambahkan.

Selanjutnya terdapat percabangan if nilai < root.nilai: yang berarti program membandingkan nilai baru dengan nilai pada node saat ini. Jika nilai baru lebih kecil, maka sintaks root.left, berhasil = self._insert_node(root.left, nilai) dijalankan untuk memasukkan nilai ke cabang kiri. Fungsi memanggil dirinya sendiri sehingga proses ini disebut rekursi. Setelah itu, return root, berhasil mengembalikan node beserta status apakah penyisipan berhasil.

Kemudian terdapat percabangan if nilai > root.nilai: yang berarti jika nilai baru lebih besar dari nilai node saat ini, program bergerak ke cabang kanan melalui sintaks root.right, berhasil = self._insert_node(root.right, nilai). Jika nilai baru tidak lebih kecil dan tidak lebih besar, berarti nilai tersebut sama dengan data yang sudah ada. Oleh karena itu, sintaks return root, False digunakan sebagai tanda bahwa nilai duplikat tidak dimasukkan kembali.

Def insert adalah fungsi yang digunakan untuk memulai proses penambahan nilai dari akar pohon. Sintaks self.root, berhasil = self._insert_node(self.root, nilai) memanggil fungsi bantuan _insert_node dengan membawa root dan nilai input user. Hasil proses tersebut disimpan ke variabel berhasil, lalu dikembalikan dengan sintaks return berhasil agar program utama dapat menampilkan pesan berhasil ditambahkan atau data tidak diduplikasi.

Def _search_node adalah pendeklarasian fungsi bantuan untuk mencari nilai pada BST dengan parameter root dan nilai. Parameter root menunjukkan node yang sedang dibandingkan, sedangkan nilai merupakan nilai ujian yang dicari oleh user. Dimulai dengan sintaks if root is None: return False, yang berarti jika pencarian sudah sampai ke cabang kosong, maka nilai tidak ditemukan.

Selanjutnya terdapat percabangan if root.nilai == nilai: return True yang berarti apabila nilai pada node sama dengan nilai target, pencarian berhasil. Apabila target lebih kecil, sintaks return self._search_node(root.left, nilai) mengarahkan pencarian ke cabang kiri. Jika tidak, sintaks return self._search_node(root.right, nilai) mengarahkan pencarian ke cabang kanan. Dengan cara ini, pencarian pada BST tidak harus memeriksa seluruh data.

Def search adalah fungsi untuk memulai pencarian nilai dari node akar. Sintaks return self._search_node(self.root, nilai) digunakan untuk memanggil proses pencarian rekursif dan langsung mengembalikan hasil berupa True jika nilai ditemukan atau False jika nilai tidak ditemukan.

Def _inorder adalah fungsi traversal dengan parameter root dan hasil, dimana root adalah node yang sedang dikunjungi dan hasil adalah list untuk menampung urutan nilai. Dimulai dengan kondisi if root is not None: agar proses hanya dijalankan apabila node berisi data. Sintaks self._inorder(root.left, hasil) mengunjungi cabang kiri terlebih dahulu, kemudian hasil.append(root.nilai) memasukkan nilai node saat ini ke dalam list, lalu self._inorder(root.right, hasil) mengunjungi cabang kanan. Urutan kiri, akar, kanan ini menyebabkan nilai BST tampil dari yang terkecil sampai terbesar.

Def inorder digunakan untuk menyediakan hasil traversal inorder kepada user. Sintaks hasil = [] membuat list kosong sebagai tempat penyimpanan hasil, kemudian self._inorder(self.root, hasil) memulai traversal dari root. Terakhir, sintaks return hasil mengembalikan list nilai yang sudah terurut.

Def _preorder adalah fungsi traversal preorder. Pada fungsi ini, sintaks hasil.append(root.nilai) dijalankan terlebih dahulu untuk memasukkan nilai akar, setelah itu program mengunjungi cabang kiri menggunakan self._preorder(root.left, hasil) dan cabang kanan menggunakan self._preorder(root.right, hasil). Oleh karena itu, urutan preorder adalah akar, kiri, lalu kanan. Def preorder kemudian membuat list hasil, memanggil traversal dari root, dan mengembalikan hasil tersebut kepada program utama.

Def _postorder adalah fungsi traversal postorder. Fungsi ini terlebih dahulu menjalankan self._postorder(root.left, hasil) untuk mengunjungi cabang kiri, lalu self._postorder(root.right, hasil) untuk mengunjungi cabang kanan, dan terakhir menjalankan hasil.append(root.nilai) untuk memasukkan nilai akar. Dengan demikian, urutan postorder adalah kiri, kanan, lalu akar. Def postorder digunakan untuk memulai proses tersebut dari root dan mengembalikan list hasil traversal.

Def find_min adalah fungsi untuk mencari nilai minimum pada BST. Dimulai dengan sintaks if self.root is None: return None, yang berarti jika pohon belum memiliki data maka tidak ada nilai minimum. Jika pohon berisi data, sintaks current = self.root menyimpan node akar sebagai posisi awal. Selanjutnya dilakukan perulangan while current.left is not None: karena pada BST nilai yang lebih kecil selalu berada di sebelah kiri. Sintaks current = current.left terus memindahkan posisi sampai node paling kiri ditemukan, lalu return current.nilai mengembalikan nilai terkecil.

Def find_max adalah fungsi untuk mencari nilai maksimum dengan cara yang berlawanan dari nilai minimum. Jika pohon kosong, fungsi mengembalikan None. Jika berisi data, program memulai dari root melalui current = self.root, lalu menjalankan while current.right is not None: untuk bergerak terus ke node paling kanan. Setelah node kanan terakhir ditemukan, sintaks return current.nilai mengembalikan nilai terbesar.

Def _count_nodes adalah fungsi rekursif untuk menghitung jumlah data pada BST dengan parameter root. Sintaks if root is None: return 0 berarti cabang kosong tidak menambah jumlah data. Jika node berisi nilai, sintaks return 1 + self._count_nodes(root.left) + self._count_nodes(root.right) menghitung satu node yang sedang dikunjungi, lalu menambah jumlah node pada cabang kiri dan kanan. Def count_nodes kemudian memanggil fungsi ini dari root agar program memperoleh jumlah seluruh nilai yang tersimpan.

Def _sum_nodes adalah fungsi rekursif untuk menghitung total semua nilai ujian dengan parameter root. Apabila node kosong, sintaks return 0 dijalankan. Jika node berisi nilai, sintaks return root.nilai + self._sum_nodes(root.left) + self._sum_nodes(root.right) menjumlahkan nilai pada node saat ini dengan seluruh nilai pada cabang kiri dan kanan. Def sum_nodes digunakan untuk memulai penjumlahan dari root.

Def baca_nilai adalah pendeklarasian fungsi dengan parameter pesan, dimana parameter tersebut digunakan untuk menampilkan instruksi input kepada user. Di dalam fungsi ini terdapat sintaks nilai = int(input(pesan)). Fungsi input() digunakan untuk menerima masukan user, sedangkan int() digunakan untuk mengubah masukan tersebut menjadi bilangan bulat.

Proses input ditempatkan di dalam struktur try dan except ValueError. Jika user memasukkan teks yang tidak dapat diubah menjadi angka, bagian except dijalankan dan program menampilkan pesan Input tidak valid. Masukkan bilangan bulat. Setelah itu fungsi mengembalikan None agar input tersebut tidak diproses lebih lanjut.

Selanjutnya terdapat percabangan if nilai < 0 or nilai > 100: yang digunakan untuk memastikan nilai ujian hanya berada pada rentang 0 sampai 100. Operator or berarti kondisi dianggap benar jika salah satu syarat terpenuhi, yaitu nilai kurang dari nol atau lebih dari seratus. Jika tidak valid, program menampilkan pesan kesalahan dan mengembalikan None. Jika valid, sintaks return nilai mengembalikan nilai kepada bagian menu yang memanggil fungsi.

Def tampilkan_daftar adalah fungsi dengan parameter label dan daftar. Parameter label digunakan untuk menampung nama hasil yang ingin ditampilkan, seperti Nilai terurut, Preorder, atau Postorder, sedangkan parameter daftar digunakan untuk menampung list hasil traversal. Percabangan if daftar: berarti jika list berisi data, maka program menjalankan sintaks print(f"{label}: {' '.join(str(nilai) for nilai in daftar)}").

Pada sintaks tersebut, f-string digunakan agar nilai variabel label dan hasil traversal dapat dimasukkan ke dalam teks output. Fungsi str(nilai) mengubah setiap nilai angka menjadi teks, sedangkan ' '.join(...) menggabungkan seluruh nilai menggunakan spasi. Jika list kosong, bagian else menampilkan pesan Data nilai masih kosong.

Def tampilkan_menu adalah fungsi untuk menampilkan pilihan fitur yang dapat digunakan oleh user. Dimulai dengan sintaks print("\n=== PENGELOLA NILAI UJIAN DENGAN BST ===") untuk menampilkan judul program, dimana \n digunakan agar output berpindah ke baris baru sebelum judul dicetak. Kemudian beberapa sintaks print() digunakan untuk menampilkan menu 1 sampai 9, yaitu tambah nilai, cari nilai, traversal inorder, preorder, postorder, nilai minimum, nilai maksimum, statistik, dan keluar.

Def main adalah fungsi utama tempat jalannya program. Dimulai dengan sintaks bst = BSTNilai() yang membuat satu objek BST bernama bst sebagai tempat penyimpanan nilai selama program berjalan. Selanjutnya ada sintaks while True: yang digunakan agar program menampilkan menu secara berulang sampai user memilih menu keluar. Di dalam perulangan, sintaks tampilkan_menu() memanggil fungsi tampilan menu, lalu pilihan = input("Pilih menu: ") menyimpan pilihan user.

Pada percabangan if pilihan == "1":, program menjalankan fitur tambah nilai. Sintaks nilai = baca_nilai("Masukkan nilai (0-100): ") meminta dan memvalidasi input user. Jika nilai is not None, berarti input valid. Setelah itu, if bst.insert(nilai): digunakan untuk menambahkan nilai ke BST. Jika berhasil, program menampilkan pesan bahwa nilai berhasil ditambahkan. Jika fungsi insert mengembalikan False, program menampilkan pesan bahwa data sudah tersimpan dan tidak diduplikasi.

Pada bagian elif pilihan == "2":, program menjalankan fitur pencarian. Nilai target dibaca menggunakan fungsi baca_nilai, lalu sintaks if bst.search(nilai): memeriksa apakah nilai tersebut berada di dalam BST. Jika ditemukan, program mencetak pesan Nilai ... ditemukan dalam data. Jika tidak ditemukan, bagian else mencetak pesan bahwa nilai tidak ditemukan.

Pada menu 3, sintaks tampilkan_daftar("Nilai terurut", bst.inorder()) digunakan untuk menampilkan nilai dari kecil ke besar. Pada menu 4, sintaks tampilkan_daftar("Preorder", bst.preorder()) menampilkan urutan akar, kiri, kanan. Pada menu 5, sintaks tampilkan_daftar("Postorder", bst.postorder()) menampilkan urutan kiri, kanan, akar.

Pada menu 6, program membuat variabel minimum melalui sintaks minimum = bst.find_min(). Jika nilainya None, berarti data masih kosong. Jika terdapat data, program menampilkan nilai minimum menggunakan print(f"Nilai minimum: {minimum}"). Pada menu 7, proses yang sama dilakukan untuk nilai maksimum menggunakan fungsi bst.find_max() dan variabel maksimum.

Pada menu 8, program menjalankan perhitungan statistik. Sintaks jumlah = bst.count_nodes() digunakan untuk menghitung banyaknya nilai yang tersimpan. Jika jumlah == 0, program menampilkan pesan bahwa data masih kosong agar tidak melakukan pembagian dengan nol. Jika ada data, sintaks total = bst.sum_nodes() menghitung jumlah seluruh nilai dan rata_rata = total / jumlah menghitung nilai rata-rata. Output kemudian ditampilkan menggunakan f-string. Pada sintaks print(f"Rata-rata : {rata_rata:.2f}"), format :.2f digunakan agar hasil rata-rata ditampilkan dengan dua angka di belakang koma.

Pada menu 9, sintaks print("Program selesai. Terima kasih.") menampilkan pesan penutup dan break digunakan untuk menghentikan perulangan while True, sehingga program selesai. Jika user memasukkan pilihan selain menu yang tersedia, bagian else dijalankan untuk menampilkan pesan Menu tidak tersedia. Pilih angka 1 sampai 9.

Terakhir terdapat sintaks if __name__ == "__main__": dan main(), yang berarti fungsi utama hanya akan dijalankan ketika file Python ini dieksekusi secara langsung. Jika file ini di-import oleh file Python lain, maka menu program tidak otomatis dijalankan.

D.Output Program
dengan memasukkan 3 nilai 

ketika di run :

<img width="648" height="163" alt="Screenshot 2026-05-25 at 17 39 02" src="https://github.com/user-attachments/assets/d18556f2-4b50-49eb-aada-abe0184d2a0a" />

pilih 1:

<img width="648" height="576" alt="Screenshot 2026-05-25 at 17 40 21" src="https://github.com/user-attachments/assets/088fe983-31e5-4730-a026-9113af3491b5" />

pilih 2:

<img width="648" height="191" alt="Screenshot 2026-05-25 at 17 41 16" src="https://github.com/user-attachments/assets/55087b83-5cbc-4aba-8ce8-f88c81fcfdd7" />

pilih 3:

<img width="648" height="178" alt="Screenshot 2026-05-25 at 17 41 43" src="https://github.com/user-attachments/assets/ba7c6164-04ba-4975-9eec-2e75f8af1427" />

pilih 4:

<img width="648" height="178" alt="Screenshot 2026-05-25 at 17 42 08" src="https://github.com/user-attachments/assets/86ee5273-22e4-479c-ab9d-ac95c9351ca6" />

pilih 5:

<img width="648" height="178" alt="Screenshot 2026-05-25 at 17 42 42" src="https://github.com/user-attachments/assets/62f1ddee-a7b6-4f42-b172-23c85c2589e2" />

pilih 6:

<img width="648" height="178" alt="Screenshot 2026-05-25 at 17 43 06" src="https://github.com/user-attachments/assets/ff1d770b-33c9-4922-b96b-e6574dd0349f" />

pilih 7: 

<img width="648" height="178" alt="Screenshot 2026-05-25 at 17 43 23" src="https://github.com/user-attachments/assets/4ee4deeb-f052-42b9-8f5a-e45b26ae9b3d" />

pilih 8:

<img width="648" height="201" alt="Screenshot 2026-05-25 at 17 44 07" src="https://github.com/user-attachments/assets/56b7588a-ace5-431b-ad34-586b5df8f050" />

pilih 9:

<img width="648" height="175" alt="Screenshot 2026-05-25 at 17 44 49" src="https://github.com/user-attachments/assets/bb83cf2b-84ed-44b7-89c0-bbdf2a370565" />

