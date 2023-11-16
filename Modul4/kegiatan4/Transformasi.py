import math

def translasi (tx, ty):
    def transformasi(p):
        x,y = p
        return x + tx, y + ty
    return transformasi

def dilatasi (sx, sy):
    def transformasi(p) :
        x, y = p
        return x * sx, y * sy
    return transformasi

def rotasi (sudut) :
    def transformasi(p) :
        x, y = p
        radian = math.radians(sudut)
        x_baru = x * math.cos(radian) - y * math.sin(radian)
        y_baru = x * math.sin(radian) - y * math.cos(radian)
        return x_baru, y_baru
    return transformasi

def print_koordinat(label, p) :
    print(f"{label}: ({p[0]}, {p[1]})")

# Titik awal
P = (3,5)

# Translasi
translasi_p = translasi(2, -1)
P_translasi = translasi_p(P)
print_koordinat("koordinat setelah translasi : ", P_translasi)

# Dilatasi
dilatasi_p = dilatasi(2, -1)
P_dilatasi = dilatasi_p(P_translasi)
print_koordinat("koordinat setelah dilatasi : ", P_dilatasi)

# Rotasi
rotasi_p = rotasi(30)
P_rotasi = rotasi_p(P_dilatasi)
print_koordinat("koordinat setelah rotasi : ", P_rotasi)

