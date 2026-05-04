def insertion_sort(daftar_konsumsi):
    for i in range(1, len(daftar_konsumsi)):
        kunci = daftar_konsumsi[i]
        j = i - 1
        while j >= 0 and daftar_konsumsi[j] < kunci:
            daftar_konsumsi[j + 1] = daftar_konsumsi[j]
            j -= 1
        daftar_konsumsi[j + 1] = kunci

def main():
    print("Masukkan jumlah rumah tangga:")
    jumlah = int(input())
    
    daftar_konsumsi = []
    for i in range(jumlah):
        print(f"Masukkan konsumsi listrik rumah {i + 1} (dalam kWh):")
        konsumsi = float(input())
        daftar_konsumsi.append(konsumsi)
    
    insertion_sort(daftar_konsumsi)
    
    print("Konsumsi listrik setelah diurutkan (dari tertinggi ke terendah):")
    for konsumsi in daftar_konsumsi:
        print(f"{konsumsi} kWh")

if __name__ == "__main__":
    main()