A. Judul Program : Mengurutkan Tingkat Konsumsi Daya Listrik Rumah Tangga
 

B. Deskripsi singkat : Program ini menggunakan Insertion Sort yang bekerja dengan mengambil satu elemen, kemudian membandingkannya mundur ke elemen-elemen sebelumnya sampai bertemu posisi yang pas. Dalam konteks program konsumsi daya listrik rumah tangga, algoritma ini digunain buat mengurutkan data pemakaian yang sudah masuk ke dalam list.
Di program ini, pengurutannya dibuat secara descending (dari konsumsi terbesar ke yang paling kecil). Mekanismenya, kalau ada nilai yang lebih besar dari elemen di depannya, elemen itu akan terus digeser ke kanan sampai si nilai baru nemuin tempat yang sesuai. Alasan saya menggunakan Insertion Sort karena logikanya gampang diikuti, implementasinya nggak ribet, dan performanya bagus selama jumlah datanya nggak terlalu banyak.


C. SOURCE CODE 
<img width="468" height="338" alt="image" src="https://github.com/user-attachments/assets/fe98e2c6-9eab-4c97-b3a9-4558db5dbbc7" />

Def insertion_sort
Pendeklarasian fungsi insertion_sort dengan parameter “daftar_konsumsi”, dimulai dengan Baris "for i dimulai dari 1 hingga panjang daftar konsumsi" berarti kita memulai dari elemen kedua, lalu membuat variabel kunci yang isinya daftar_konsumsi index I,membuat variabel j yang berisi “i – 1” bermaksud menandakan variabel j berada sebelum variabel i
Lalu membuat looping lagi dengan kondisi “ j >= 0 “ dan “ daftar_konsumsi[j] < kunci “ yang berarti jika nilai di sebelah kiri lebih kecil daripada kunci, maka nilai tersebut harus digeser ke kanan, dan sintaks “ < “ digunakan karena ingin mengurutkan data secara descending. 
Jika kondisi tersebut terpenuhi maka akan dijalankan “ daftar_konsumsi[j + 1] = daftar_konsumsi[j]” dan “ j -= 1 “ untuk menyesuaikan angkanya dan terakhir sintaks “         daftar_konsumsi[j + 1] = kunci “ guna menaruh nilai kunci ke posisi yang tepat

Def main
Fungsi main() digunakan sebagai tempat jalannya program utama, dimulai dengan print “ masukkan jumlah rumah tangga” untuk menginstruksikan user rumah yang ingin didata lalu “     jumlah = int(input()) “ agar user dapat memasukkan jumlah rumah tangga yang ingin didata 

Selanjutnya buat list kosong bernama daftar_konsumsi dengan sintaks “ daftar_konsumsi = [] “ dan lanjut dengan membuat looping dengan sintaks “ for i in range(jumlah): “, maksud dari parameter jumlah agar looping mengikuti angka yang diinputkan saat memasukkan jumlah rumah tangga yang ingin didata, setelahnya “ print(f"Masukkan konsumsi listrik rumah {i + 1} dalam kWh:") “, penggunaan f-string agar nilai variabel bisa dimasukkan ke dalam teks dan “i + 1” digunakan karena indeks Python dimulai dari 0, sedangkan untuk tampilan ke pengguna lebih enak dimulai dari 1, lalu pembuatan variabel “ konsumsi = float(input()) “ agar user bisa memasukkan besaran konsumsi daya yang dipakai pada sebuah rumah dengan tipe float supaya bisa menginput angka desimal, dan sintaks “ daftar_konsumsi.append(konsumsi) “ untuk ini memasukkan nilai konsumsi ke dalam list daftar_konsumsi.

Setelah itu data akan diurutkan dengan memanggil fungsi insertion yang sudah dibuat tadi menggunakan sintaks “ insertion_sort(daftar_konsumsi) “ agar data menjadi terurut dari terbesar ke terkecil

Lalu ada judul dari output dengan sintaks “ print("Konsumsi listrik setelah diurutkan dari terbesar ke terkecil:") “ looping dengan sintaks “ for konsumsi in daftar_konsumsi: “, untuk melakukan perulangan untuk menampilkan setiap nilai konsumsi listrik yang sudah diurutkan.
Dimana variabel konsumsi akan mengambil satu per satu isi dari daftar_konsumsi. Dan “ print(f"{konsumsi} kWh") untuk menampilkan data yang sudah di inputkan tadi

Terakhir ada “ if __name__ == "__main__": “ dan “ main() “ yang berarti program hanya akan menjalankan “ main() “ jika file ini dijalankan secara langsung tetapi kalau file ini di-import oleh file Python lain, maka main() tidak otomatis dijalankan.


D. Output 

<img width="468" height="45" alt="image" src="https://github.com/user-attachments/assets/df40dea6-da19-44fc-84d0-3bf01bf855ad" />

<img width="468" height="95" alt="image" src="https://github.com/user-attachments/assets/e02a64cb-0c4e-4d5b-89b4-5e478e067aaa" />
 
<img width="468" height="58" alt="image" src="https://github.com/user-attachments/assets/030e7c67-3c80-40ed-994d-232ddb739bb9" />

 
PROGRAM MULAI :

Program akan meminta user untuk memasukkan jumlah rumah tangga yang ingin diinputkan konsumsi listriknya, lalu program akan meminta user untuk memasukkan konsumsi listrik berulang sesuai dengan jumlah rumah tangga yang di inputkan, alhasil program akan memanggil fungsi insertion sort untuk mengurutkan data sesuai dengan alur pemrograman yang telah dibuat 


E. Video pembelajaran :
https://www.youtube.com/watch?v=I9Lq6U1T740
