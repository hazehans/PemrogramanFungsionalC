import matplotlib.pyplot as plt
# import numpy as np

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

plt.title('Percobaan 4', loc='center', pad=20, fontsize='30', color='lightblue')
plt.xlabel('Titik titik X', fontsize=12)
plt.ylabel('Titik titik Y', fontsize=12)
plt.scatter(x, y)
plt.show()
