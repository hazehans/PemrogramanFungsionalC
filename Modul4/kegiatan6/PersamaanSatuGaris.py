# lengkapi kode berikut untuk mendapatkan persamaan garis lurus bagi NIM GENAP
def point(x,y):
    return x,y

def line_equation_of(p1, M):
    def calculate_C(p1, M) :
        # rumus C = y - M . x
        return p1[1] - M * p1[0]

    C = calculate_C(p1, M)
    print("Nilai C = " + C)
    return (f"y = {M:.2f}x + {C:.2f}")

print("Persamaan garis yang melalui titik (6,-2) dan bergradien 2:")
print(line_equation_of(point(0, 9), 2))

#ubah nilai input dengan 3 digit nim akhir kalian
#dan lakukan perhitungan manual sesuai rumus yang kalian gunakan dalam fungsi
#untuk membuktikan bahwa output sudah benar

# C   = y - M . x
#     = 9 - 2 . 0
#     = 9
#
# persamaan
# y   = mx + c
#     = 2x + 9

# NOTE : Inner function ditunjukkan oleh fungsi "calculate_C" karena berada di dalam
# NOTE : Sedangkan outer function atau induknya adalah "line_equation_of"
# NOTE : Closure, sesuai dalam modul, adalah inner function yang terlampir dalam outer function
# NOTE : Maka dalam hal ini, closure dapat diimplementasikan dengan penggunaan function calculate_C
# NOTE : yang me return variabel p1 dan M dari lingkup luar fungsi outer atau induk line_equation_of
