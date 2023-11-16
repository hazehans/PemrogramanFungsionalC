# currying

def x (a) :
    def x (b) :
        return a * b
    return x

hasil = x (10) (20)
print(hasil)
