random_list = [9105, 3.1, "Hello", 737, "Python", 2.7, "world", 412, 5.5, "AI"]

int_dict = {}
float_tuple = ()
string_list = []

for item in random_list :
    if isinstance(item, int) :
        # pisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item % 100) // 10
        ratusan = item // 100

        # simpan dalam dict
        int_dict[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float) :
        # simpan dlm bentuk tuple
        float_tuple += (item,)
    elif isinstance(item, str) :
        #simpan string dlm bentuk list
        string_list.append(item)

print("Dictionary utk nilai integer \t: ", int_dict)
print("Tuple utk nilai float \t\t\t: ", float_tuple)
print("List utk nilai string \t\t\t: ", string_list)

