# Data awal
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi untuk memfilter nilai integer dari string
def filter_integers(text):
    return [token for token in text.split() if token.isdigit()]

# Menggunakan filter untuk mengambil hanya nilai integer dari setiap data
filtered_data = list(map(filter_integers, data))

# Menampilkan hasil
for item in filtered_data:
    print(item)
