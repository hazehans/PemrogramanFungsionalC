# lengkapi kode berikut untuk mendapatkan persamaan garis lurus bagi NIM GENAP
def point(x,y):
    return x,y

def line_equation_of(p1, p2):
    # rumus m = (y2 - y1) / (x2 - x1)
    M = (p2[1] - p1[1]) / (p2[0] - p1[0])
    # rumus c = y1 - M . x1
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 0),point(9, 2)))

#ubah nilai input dengan 4 digit nim akhir kalian
#dan lakukan perhitungan manual sesuai rumus yang kalian gunakan dalam fungsi

# M   = (2-0) / (9-1)
#     = 2/8
#     = 1/4 atau 0.25
#
# C   = 0 - 1/4 * 1
#     = -0.25
