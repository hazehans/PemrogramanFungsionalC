random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk pisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int_to_units(num):
    ratusan = num // 100
    puluhan = (num % 100) // 10
    satuan = num % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

int_mapped = list(map(lambda x: map_int_to_units(x), int_values))

# Menampilkan hasil
print("Data Float:", float_values)
print("Data Int:")
for item in int_mapped:
    print(item)
print("Data String:", string_values)
