def uppercase_decorator(function) :
    def wrapper() :
        func = function()
        make_uppercase = func.upper()
        return func.upper()
    return wrapper

#tulis kembali kode diatas dan tambahkan sebagai decorator pada fungsi say_hi berikut
@uppercase_decorator
def say_hi() :
    return 'hello there'

print(say_hi())

