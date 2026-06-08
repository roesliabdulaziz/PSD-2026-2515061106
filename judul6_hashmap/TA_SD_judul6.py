class Pasien:

    def __init__(self, id_pasien, nama, umur, diagnosa, dokter):
        self.id_pasien = id_pasien
        self.nama = nama
        self.umur = umur
        self.diagnosa = diagnosa
        self.dokter = dokter


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapPasien:

    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size
        self.jumlah_data = 0

    def hash_function(self, key):
        return (key % self.size + self.size) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return False
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.jumlah_data += 1
        return True

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def update(self, key, nama, umur, diagnosa, dokter):
        pasien = self.search(key)

        if pasien is None:
            return False

        pasien.nama = nama
        pasien.umur = umur
        pasien.diagnosa = diagnosa
        pasien.dokter = dokter
        return True

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        previous = None

        while current is not None:
            if current.key == key:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next

                self.jumlah_data -= 1
                return True

            previous = current
            current = current.next

        return False

    def get_all_patients(self):
        daftar = []

        for i in range(self.size):
            current = self.table[i]
            while current is not None:
                daftar.append(current.value)
                current = current.next

        return sorted(daftar, key=lambda pasien: pasien.id_pasien)

    def count_collision_slots(self):
        jumlah_collision = 0

        for i in range(self.size):
            current = self.table[i]
            panjang_rantai = 0

            while current is not None:
                panjang_rantai += 1
                current = current.next

            if panjang_rantai > 1:
                jumlah_collision += 1

        return jumlah_collision

    def load_factor(self):
        return self.jumlah_data / self.size

    def display_table(self):
        print("\nIsi Hash Table Pasien (Separate Chaining):")

        for i in range(self.size):
            print(f"{i}: ", end="")
            current = self.table[i]

            while current is not None:
                pasien = current.value
                print(f"[{pasien.id_pasien} - {pasien.nama}] -> ", end="")
                current = current.next

            print("NONE")


def baca_id(pesan):

    try:
        id_pasien = int(input(pesan))
    except ValueError:
        print("Input tidak valid. Masukkan ID pasien berupa bilangan bulat.")
        return None

    if id_pasien <= 0:
        print("ID pasien harus lebih besar dari 0.")
        return None

    return id_pasien


def baca_umur(pesan):

    try:
        umur = int(input(pesan))
    except ValueError:
        print("Input tidak valid. Masukkan umur berupa bilangan bulat.")
        return None

    if umur < 0 or umur > 120:
        print("Umur harus berada pada rentang 0 sampai 120.")
        return None

    return umur


def baca_teks(pesan):
    teks = input(pesan).strip()

    if teks == "":
        print("Data tidak boleh kosong.")
        return None

    return teks


def input_data_pasien(id_pasien):
    nama = baca_teks("Masukkan nama pasien: ")
    if nama is None:
        return None

    umur = baca_umur("Masukkan umur pasien: ")
    if umur is None:
        return None

    diagnosa = baca_teks("Masukkan diagnosa pasien: ")
    if diagnosa is None:
        return None

    dokter = baca_teks("Masukkan nama dokter: ")
    if dokter is None:
        return None

    return Pasien(id_pasien, nama, umur, diagnosa, dokter)


def tampilkan_pasien(pasien):
    print(f"ID Pasien : {pasien.id_pasien}")
    print(f"Nama      : {pasien.nama}")
    print(f"Umur      : {pasien.umur}")
    print(f"Diagnosa  : {pasien.diagnosa}")
    print(f"Dokter    : {pasien.dokter}")


def tampilkan_daftar_pasien(daftar_pasien):
    if not daftar_pasien:
        print("Data pasien masih kosong.")
        return

    print("\nDaftar Data Pasien:")

    for pasien in daftar_pasien:
        print("-" * 35)
        tampilkan_pasien(pasien)


def tampilkan_menu():
    print("\n=== PENGELOLA DATA PASIEN DENGAN HASH MAP ===")
    print("1. Tambah data pasien")
    print("2. Cari data pasien")
    print("3. Ubah data pasien")
    print("4. Hapus data pasien")
    print("5. Tampilkan semua pasien")
    print("6. Tampilkan isi hash table")
    print("7. Tampilkan statistik hash map")
    print("8. Keluar")


def main():
    hashmap = HashMapPasien()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            id_pasien = baca_id("Masukkan ID pasien: ")
            if id_pasien is not None:
                pasien = input_data_pasien(id_pasien)
                if pasien is not None:
                    if hashmap.insert(id_pasien, pasien):
                        print(f"Data pasien dengan ID {id_pasien} berhasil ditambahkan.")
                    else:
                        print(f"ID {id_pasien} sudah tersimpan, gunakan menu ubah data.")

        elif pilihan == "2":
            id_pasien = baca_id("Masukkan ID pasien yang dicari: ")
            if id_pasien is not None:
                pasien = hashmap.search(id_pasien)
                if pasien is not None:
                    print("\nData pasien ditemukan:")
                    tampilkan_pasien(pasien)
                else:
                    print(f"Data pasien dengan ID {id_pasien} tidak ditemukan.")

        elif pilihan == "3":
            id_pasien = baca_id("Masukkan ID pasien yang ingin diubah: ")
            if id_pasien is not None:
                if hashmap.search(id_pasien) is None:
                    print(f"Data pasien dengan ID {id_pasien} tidak ditemukan.")
                else:
                    pasien_baru = input_data_pasien(id_pasien)
                    if pasien_baru is not None:
                        hashmap.update(
                            id_pasien,
                            pasien_baru.nama,
                            pasien_baru.umur,
                            pasien_baru.diagnosa,
                            pasien_baru.dokter,
                        )
                        print(f"Data pasien dengan ID {id_pasien} berhasil diubah.")

        elif pilihan == "4":
            id_pasien = baca_id("Masukkan ID pasien yang ingin dihapus: ")
            if id_pasien is not None:
                if hashmap.remove_key(id_pasien):
                    print(f"Data pasien dengan ID {id_pasien} berhasil dihapus.")
                else:
                    print(f"Data pasien dengan ID {id_pasien} tidak ditemukan.")

        elif pilihan == "5":
            tampilkan_daftar_pasien(hashmap.get_all_patients())

        elif pilihan == "6":
            hashmap.display_table()

        elif pilihan == "7":
            print(f"Jumlah pasien        : {hashmap.jumlah_data}")
            print(f"Ukuran tabel         : {hashmap.size}")
            print(f"Load factor          : {hashmap.load_factor():.2f}")
            print(f"Slot yang collision  : {hashmap.count_collision_slots()}")

        elif pilihan == "8":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Menu tidak tersedia. Pilih angka 1 sampai 8.")


if __name__ == "__main__":
    main()
