# TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
# drive.mount('/content/drive')
image_path = "E:\KULIAH\Semester 5\Prak. Pemrograman Fungsional 5C\Tugas\Modul6\codelab\gambar1.png"
gambarku = Image.open(image_path)

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert('L')

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.load_default()  # Use the default font
text = "Hans Aufa - 202110370311092"

# Get text bounding box
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

text_x = (gambarku.width - text_width) // 2
text_y = 20
draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save('E:\KULIAH\Semester 5\Prak. Pemrograman Fungsional 5C\Tugas\Modul6\codelab\gambar1After.png')

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
