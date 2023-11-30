import matplotlib.pyplot as plt

# Mengimpor fungsi normal dari pustaka numpy.random
# Digunakan untuk menghasilkan sampel data dari distribusi normal
from numpy.random import normal

# Mengimpor fungsi mean dan std dari pustaka numpy
# Digunakan untuk menghitung rata - rata dan standar deviasi data
from numpy import mean, std

# Mengimpor distribusi normal dari pustaka scipy.stats
# Digunakan untuk analisis statistik terkait distribusi normal
from scipy.stats import norm

# Cara buat sample data
sample = normal(loc=50, scale=5, size=1000)
sample_mean = mean(sample)
sample_std = std(sample)

dist = norm(sample_mean, sample_std)
print(dist)

# panggil variable simple untuk mengetahui hasilnya
# plt.hist(sample)
# atau tampilkan dalam bentuk histogram :


# buat list nilai yang akan digunakan dalam perhitungan
values = [value for value in range(30, 70)]  # gunakan list comprehension
# manfaatkan list comprehension untuk menerapkan method pdf
# berdasarkan value (yang telah disiapkan sebelumnya) pada data dist
probabilitas = [dist.pdf(value) for value in values]
print(probabilitas)

plt.figure(figsize=(5, 4))  # perkecil media gambar
plt.hist(sample, bins=10, density=True)
plt.plot(values, probabilitas)

# print('Mean = %.3f \nStandard Deviation = %.3f' % (sample_mean, sample_std))
plt.show()
