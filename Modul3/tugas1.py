# Fungsi untuk mengkonversi waktu dalam format "minggu hari jam menit" menjadi menit
def convert_to_minutes(time_str):
    # Pisahkan waktu menjadi token
    tokens = time_str.split()

    # Konversi token ke dalam integer dan hitung total menit
    weeks = int(tokens[0])
    days = int(tokens[2])
    hours = int(tokens[4])
    minutes = int(tokens[6])
    total_minutes = (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes

    return total_minutes

# Fungsi currying untuk mengonversi waktu dalam format "minggu hari jam menit" menjadi menit
def curried_convert_to_minutes(time_str):
    return convert_to_minutes(time_str)

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Menggunakan fungsi map untuk mengkonversi semua data ke dalam menit
output_data = list(map(curried_convert_to_minutes, data))
print(output_data)


