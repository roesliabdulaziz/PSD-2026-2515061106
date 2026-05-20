class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, pasien: dict):
        """Tambahkan pasien ke belakang antrian."""
        if self.is_full():
            print("\\n[!] Antrian penuh! Tidak dapat mendaftarkan pasien baru.")
            return False
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = pasien
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        pasien = self.q[self.front_idx]
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN
        return pasien

    def peek(self):
        if self.is_empty():
            return None
        return self.q[self.front_idx]

    def size(self):
        if self.is_empty():
            return 0
        if self.rear_idx >= self.front_idx:
            return self.rear_idx - self.front_idx + 1
        return self.MAXN - self.front_idx + self.rear_idx + 1

    def get_all(self):
        if self.is_empty():
            return []
        result = []
        i = self.front_idx
        while True:
            result.append(self.q[i])
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        return result


def cetak_info_pasien(pasien: dict, prefix: str = ""):
    
    print(f"{prefix}Nomor Antrian : {pasien['nomor_antrian']}")
    print(f"{prefix}Nama Pasien   : {pasien['nama']}")
    print(f"{prefix}Keluhan       : {pasien['keluhan']}")


def cetak_separator(char: str = "─", lebar: int = 50):
    print(char * lebar)

def daftarkan_pasien(antrian: QueueArray, counter: list):
    cetak_separator()
    print("  PENDAFTARAN PASIEN BARU")
    cetak_separator()
    if antrian.is_full():
        print("[!] Antrian penuh! Tidak dapat mendaftarkan pasien baru.")
        return counter[0]

    nama = input("Masukkan nama pasien   : ").strip()
    if not nama:
        print("[!] Nama tidak boleh kosong.")
        return counter[0]

    keluhan = input("Masukkan keluhan pasien: ").strip()
    if not keluhan:
        print("[!] Keluhan tidak boleh kosong.")
        return counter[0]

    counter[0] += 1
    pasien = {
        "nomor_antrian": counter[0],
        "nama": nama,
        "keluhan": keluhan
    }
    antrian.enqueue(pasien)

    cetak_separator("─")
    print("  ✔ Pasien berhasil didaftarkan!")
    cetak_info_pasien(pasien, prefix="  ")
    cetak_separator("─")
    return counter[0]

def panggil_pasien(antrian: QueueArray):
    cetak_separator()
    print("  PANGGIL PASIEN")
    cetak_separator()
    if antrian.is_empty():
        print("[!] Antrian kosong. Tidak ada pasien yang bisa dipanggil.")
        return

    pasien = antrian.dequeue()
    print(f"  ✔ Memanggil pasien berikut ke ruang pemeriksaan:")
    cetak_info_pasien(pasien, prefix="  ")
    sisa = antrian.size()
    print(f"  Sisa antrian: {sisa} pasien")
    cetak_separator("─")

def lihat_pasien_berikutnya(antrian: QueueArray):
    cetak_separator()
    print("  PASIEN BERIKUTNYA (PEEK)")
    cetak_separator()
    if antrian.is_empty():
        print("[!] Antrian kosong.")
        return

    pasien = antrian.peek()
    print("  Pasien yang akan dipanggil berikutnya:")
    cetak_info_pasien(pasien, prefix="  ")
    cetak_separator("─")

def tampilkan_antrian(antrian: QueueArray):
    cetak_separator()
    print("  DAFTAR SELURUH ANTRIAN")
    cetak_separator()
    if antrian.is_empty():
        print("[!] Antrian kosong.")
        return

    semua = antrian.get_all()
    print(f"  Total pasien menunggu: {len(semua)}")
    cetak_separator("─")
    for idx, pasien in enumerate(semua, start=1):
        print(f"  [{idx}]")
        cetak_info_pasien(pasien, prefix="      ")
        if idx < len(semua):
            print()
    cetak_separator("─")


def tampilkan_menu():
    print("═" * 50)
    print("    SISTEM ANTRIAN PASIEN RUMAH SAKIT")
    print("═" * 50)
    print("  1. Daftarkan Pasien")
    print("  2. Panggil Pasien (Dequeue)")
    print("  3. Lihat Pasien Berikutnya (Peek)")
    print("  4. Tampilkan Seluruh Antrian")
    print("  5. Keluar")
    print("─" * 50)


def main():
    antrian = QueueArray(max_size=100)
    counter = [0]          
    pilih = 0

    while pilih != 5:
        tampilkan_menu()
        try:
            pilih = int(input("Pilih menu (1-5): "))
        except ValueError:
            print("[!] Input tidak valid! Masukkan angka 1-5.")
            continue

        if pilih == 1:
            daftarkan_pasien(antrian, counter)
        elif pilih == 2:
            panggil_pasien(antrian)
        elif pilih == 3:
            lihat_pasien_berikutnya(antrian)
        elif pilih == 4:
            tampilkan_antrian(antrian)
        elif pilih == 5:
            print("\n Terima kasih. Program selesai.")
            print("═" * 50)
        else:
            print("[!] Pilihan tidak valid! Masukkan angka 1-5.")


if __name__ == "__main__":
    main()
