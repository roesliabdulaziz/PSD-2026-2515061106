class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class AntrianRumahSakit:
    def __init__(self):
        self.head = None
        self.tail = None

    def daftar_pasien(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.head is None:
            self.head = new_node


            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        print(f"✅ {nama} berhasil mendaftar. Keluhan: {keluhan}")

    def panggil_pasien(self):
        if self.head is None:
            print("⚠️  Antrian pasien kosong")
        else:
            nama = self.head.nama
            keluhan = self.head.keluhan
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            print(f"🔔 Memanggil: {nama} | Keluhan: {keluhan} — Silakan masuk ke ruang dokter")

    def tampilkan_antrian(self):
        if self.head is None:
            print("Antrian kosong")
            return
        current = self.head
        nomor = 1
        print("📋 Daftar Antrian Pasien:")
        while current:
            print(f"  {nomor}. {current.nama} - {current.keluhan}")
            current = current.next
            nomor += 1

def main():
    antrian = AntrianRumahSakit()
    while True:
        print("\n===== SISTEM ANTRIAN RUMAH SAKIT =====")
        print("1. Daftar pasien baru")
        print("2. Panggil pasien berikutnya")
        print("3. Lihat antrian")
        print("4. Keluar")
        pilih = input("Pilih: ")

        if pilih == "1":
            nama = input("Nama pasien: ")
            keluhan = input("Keluhan: ")
            antrian.daftar_pasien(nama, keluhan)
        elif pilih == "2":
            antrian.panggil_pasien()
        elif pilih == "3":
            antrian.tampilkan_antrian()
        elif pilih == "4":
            print("Sistem antrian ditutup.")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()

