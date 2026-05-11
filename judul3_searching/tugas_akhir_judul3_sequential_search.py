def sequential_search_mahasiswa(data_mahasiswa, target_npm):

    for index in range(len(data_mahasiswa)):
        print(f"Mengecek indeks ke-{index} dengan NPM {data_mahasiswa[index]['npm']}")

        if data_mahasiswa[index]["npm"] == target_npm:
            return index

    return -1


def tampilkan_semua_data(data_mahasiswa):
    print("\nDaftar Data Mahasiswa:")
    print("-" * 60)
    print(f"{'No':<5}{'NPM':<15}{'Nama':<20}{'Kelas':<10}")
    print("-" * 60)

    for i, mahasiswa in enumerate(data_mahasiswa, start=1):
        print(f"{i:<5}{mahasiswa['npm']:<15}{mahasiswa['nama']:<20}{mahasiswa['kelas']:<10}")

    print("-" * 60)


def main():
    
    data_mahasiswa = [
        {"npm": "2515061001", "nama": "ghani jemping", "kelas": "A"},
        {"npm": "2515061005", "nama": "rajuy mber", "kelas": "A"},
        {"npm": "2515061003", "nama": "lutpi mohak", "kelas": "B"},
        {"npm": "2515061008", "nama": "atha cihuy", "kelas": "B"},
        {"npm": "2515061002", "nama": "Eka remblong", "kelas": "C"},
        {"npm": "2515061007", "nama": "Fajar sibutar butar", "kelas": "C"},
        {"npm": "2555061004", "nama": "Gita sitabrakpagar", "kelas": "D"},
        {"npm": "2555061006", "nama": "alam suryajana", "kelas": "D"}
    ]

    print(" PROGRAM PENCARIAN DATA MAHASISWA BERDASARKAN NPM")
    print("              MENGGUNAKAN SEQUENTIAL SEARCH")
    print("======================================================")

    tampilkan_semua_data(data_mahasiswa)

    target_npm = input("\nMasukkan NPM mahasiswa yang ingin dicari: ")

    print("\nProses Sequential Search:")
    hasil_index = sequential_search_mahasiswa(data_mahasiswa, target_npm)

    print("\nHasil Pencarian:")
    if hasil_index != -1:
        mahasiswa = data_mahasiswa[hasil_index]
        print("Data mahasiswa ditemukan!")
        print(f"Indeks : {hasil_index}")
        print(f"NPM    : {mahasiswa['npm']}")
        print(f"Nama   : {mahasiswa['nama']}")
        print(f"Kelas  : {mahasiswa['kelas']}")
    else:
        print("Data mahasiswa tidak ditemukan.")
        print(f"NPM {target_npm} tidak terdapat dalam daftar mahasiswa.")


if __name__ == "__main__":
    main()
