from prettytable import PrettyTable

class Pajak:
    def __init__(self, no, nama_pajak, yang_terkena_pajak, penghasilan_pertahun, potongan_persen):
        self.no = no
        self.nama_pajak = nama_pajak
        self.yang_terkena_pajak = yang_terkena_pajak
        self.penghasilan_pertahun = penghasilan_pertahun
        self.potongan_persen = potongan_persen
        
class PajakManager:
    def __init__(self):
        self.pajak_data = []

    def tambah_pajak(self, pajak):
        self.pajak_data.append(pajak)
        print(f"Pajak {pajak.nama_pajak} telah ditambahkan.") 

    def tampilkan_list_pajak(self):
        if not self.pajak_data:
            print("Tidak ada data pajak yang tersedia.")
        else:
            table = PrettyTable(["No", "Nama", "Terkena Pajak", "Penghasilan Pertahun", "Potongan Persen"])
            for pajak in self.pajak_data:
                table.add_row([pajak.no, pajak.nama_pajak, pajak.yang_terkena_pajak, pajak.penghasilan_pertahun, pajak.potongan_persen])
            print(table)

    def perbarui_pajak(self, no_pajak, field, value):
        pajak = self.cari_pajak_by_no(no_pajak)
        if pajak:
            setattr(pajak, field, value)
            print("Data pajak telah diperbarui.")
        else:
            print("Nomor pajak tidak ditemukan.")

    def hapus_pajak(self, no_pajak):
        pajak = self.cari_pajak_by_no(no_pajak)
        if pajak:
            self.pajak_data.remove(pajak)
            print("Data pajak telah dihapus.")
        else:
            print("Nomor pajak tidak ditemukan.")

    def cari_pajak_by_no(self, no_pajak):
        for pajak in self.pajak_data:
            if pajak.no == no_pajak:
                return pajak
        return None


def main():
    manager = PajakManager()
    pembayaran_pajak = [
        {"no": 1, "nama_pajak": "Pajak_PPh", "yang_terkena_pajak": "upah, gaji, tunjangan", "penghasilan_pertahun": 5000, "potongan_persen": "5%"},
        {"no": 2, "nama_pajak": "Pajak_PPn", "yang_terkena_pajak": "pengusaha, perusahaan", "penghasilan_pertahun": 2000, "potongan_persen": "5%"}
    ]
    
    for pajak_data in pembayaran_pajak:
        pajak_baru = Pajak(**pajak_data)
        manager.tambah_pajak(pajak_baru)
    
    while True:
        print("\nMenu Sistem Pendataan Perpajakan:")
        print("1. Tampilkan List Pajak")
        print("2. Tambah Pajak")
        print("3. Perbarui Pajak")
        print("4. Hapus Pajak")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            manager.tampilkan_list_pajak()
        elif pilihan == "2":
            no = int(input("Masukkan nomor pajak: "))
            nama_pajak = input("Masukkan nama pajak: ")
            yang_terkena_pajak = input("Masukkan yang terkena pajak: ")
            penghasilan_pertahun = int(input("Masukkan penghasilan pertahun: "))
            potongan_persen = input("Masukkan potongan persen: ")
            pajak_baru = Pajak(no, nama_pajak, yang_terkena_pajak, penghasilan_pertahun, potongan_persen)
            manager.tambah_pajak(pajak_baru)
        elif pilihan == "3":
            no_pajak = int(input("Masukkan nomor pajak yang akan diperbarui: "))
            field = input("Masukkan field yang akan diperbarui: ")
            value = input("Masukkan nilai baru: ")
            manager.perbarui_pajak(no_pajak, field, value)
        elif pilihan == "4":
            no_pajak = int(input("Masukkan nomor pajak yang akan dihapus: "))
            manager.hapus_pajak(no_pajak)
        elif pilihan == "5":
            print("Program berakhir.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
