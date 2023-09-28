def hitung_nilai_akhir(uts, uas):
    # Rumus perhitungan nilai akhir (misalnya: rata-rata nilai UTS dan UAS)
    return (uts + uas) / 2

def hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa):
    data_nilai_akhir = {}  # Membuat dictionary untuk menyimpan nilai akhir semua mahasiswa
    
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    
    return data_nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil nilai akhir mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        'Hans Aufa': {'uts': 80, 'uas': 90},
        'DeMarc III': {'uts': 70, 'uas': 85},
        'John Freeman': {'uts': 75, 'uas': 92},
        # and so on
    }

    data_nilai_akhir = hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
