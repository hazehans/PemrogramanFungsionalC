import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 10, 14])
ypoints = np.array([3, 10, 5, 14])

plt.figure(figsize=(5, 5))
plt.plot(xpoints, ypoints, color='magenta')
plt.xlim([5, 15])
plt.ylim([5, 15])
plt.title('Percobaan kegiatan 2')
plt.xlabel('Sumbu x')
plt.ylabel('Sumbu y')
plt.show()
