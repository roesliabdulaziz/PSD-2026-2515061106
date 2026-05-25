class Node:

    def __init__(self, nilai):
        self.nilai = nilai
        self.left = None
        self.right = None


class BSTNilai:

    def __init__(self):
        self.root = None

    def _insert_node(self, root, nilai):
        if root is None:
            return Node(nilai), True
        if nilai < root.nilai:
            root.left, berhasil = self._insert_node(root.left, nilai)
            return root, berhasil
        if nilai > root.nilai:
            root.right, berhasil = self._insert_node(root.right, nilai)
            return root, berhasil
        return root, False

    def insert(self, nilai):
        self.root, berhasil = self._insert_node(self.root, nilai)
        return berhasil

    def _search_node(self, root, nilai):
        if root is None:
            return False
        if root.nilai == nilai:
            return True
        if nilai < root.nilai:
            return self._search_node(root.left, nilai)
        return self._search_node(root.right, nilai)

    def search(self, nilai):
        return self._search_node(self.root, nilai)

    def _inorder(self, root, hasil):
        if root is not None:
            self._inorder(root.left, hasil)
            hasil.append(root.nilai)
            self._inorder(root.right, hasil)

    def inorder(self):
        hasil = []
        self._inorder(self.root, hasil)
        return hasil

    def _preorder(self, root, hasil):
        if root is not None:
            hasil.append(root.nilai)
            self._preorder(root.left, hasil)
            self._preorder(root.right, hasil)

    def preorder(self):
        hasil = []
        self._preorder(self.root, hasil)
        return hasil

    def _postorder(self, root, hasil):
        if root is not None:
            self._postorder(root.left, hasil)
            self._postorder(root.right, hasil)
            hasil.append(root.nilai)

    def postorder(self):
        hasil = []
        self._postorder(self.root, hasil)
        return hasil

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.nilai

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.nilai

    def _count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self._count_nodes(root.left) + self._count_nodes(root.right)

    def count_nodes(self):
        return self._count_nodes(self.root)

    def _sum_nodes(self, root):
        if root is None:
            return 0
        return root.nilai + self._sum_nodes(root.left) + self._sum_nodes(root.right)

    def sum_nodes(self):
        return self._sum_nodes(self.root)


def baca_nilai(pesan):

    try:
        nilai = int(input(pesan))
    except ValueError:
        print("Input tidak valid. Masukkan bilangan bulat jon.")
        return None
    if nilai < 0 or nilai > 100:
        print("Nilai harus berada pada rentang 0 sampai 100 pekok.")
        return None
    return nilai


def tampilkan_daftar(label, daftar):
    if daftar:
        print(f"{label}: {' '.join(str(nilai) for nilai in daftar)}")
    else:
        print("Data nilai masih kosong.")


def tampilkan_menu():
    print("\n=== PENGELOLA NILAI UJIAN DENGAN BST ===")
    print("1. Tambah nilai")
    print("2. Cari nilai")
    print("3. Tampilkan nilai terurut (inorder)")
    print("4. Tampilkan preorder")
    print("5. Tampilkan postorder")
    print("6. Tampilkan nilai minimum")
    print("7. Tampilkan nilai maksimum")
    print("8. Tampilkan statistik nilai")
    print("9. Keluar")


def main():
    bst = BSTNilai()
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nilai = baca_nilai("Masukkan nilai (0-100): ")
            if nilai is not None:
                if bst.insert(nilai):
                    print(f"Nilai {nilai} berhasil ditambahkan.")
                else:
                    print(f"Nilai {nilai} sudah tersimpan, data tidak diduplikasi.")
        elif pilihan == "2":
            nilai = baca_nilai("Masukkan nilai yang dicari: ")
            if nilai is not None:
                if bst.search(nilai):
                    print(f"Nilai {nilai} ditemukan dalam data.")
                else:
                    print(f"Nilai {nilai} tidak ditemukan.")
        elif pilihan == "3":
            tampilkan_daftar("Nilai terurut", bst.inorder())
        elif pilihan == "4":
            tampilkan_daftar("Preorder", bst.preorder())
        elif pilihan == "5":
            tampilkan_daftar("Postorder", bst.postorder())
        elif pilihan == "6":
            minimum = bst.find_min()
            if minimum is None:
                print("Data nilai masih kosong.")
            else:
                print(f"Nilai minimum: {minimum}")
        elif pilihan == "7":
            maksimum = bst.find_max()
            if maksimum is None:
                print("Data nilai masih kosong.")
            else:
                print(f"Nilai maksimum: {maksimum}")
        elif pilihan == "8":
            jumlah = bst.count_nodes()
            if jumlah == 0:
                print("Data nilai masih kosong.")
            else:
                total = bst.sum_nodes()
                rata_rata = total / jumlah
                print(f"Jumlah nilai : {jumlah}")
                print(f"Total nilai  : {total}")
                print(f"Rata-rata    : {rata_rata:.2f}")
        elif pilihan == "9":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("BACAAA!!!!!. Pilih angka 1 sampai 9.")


if __name__ == "__main__":
    main()