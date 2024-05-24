# Tic Tac Toe Game

## Deskripsi

Ini adalah implementasi permainan Tic Tac Toe menggunakan bahasa pemrograman Python dan modul Pygame. Tic Tac Toe adalah permainan klasik yang biasa dimainkan oleh dua pemain, yang bergiliran menempatkan tanda mereka (biasanya 'X' atau 'O') pada papan 3x3. Pemain yang pertama berhasil menempatkan tiga tanda mereka secara berurutan secara horizontal, vertikal, atau diagonal, memenangkan permainan.

## Fitur

- Papan permainan 3x3 yang di-render menggunakan modul Pygame.
- Pemain bergantian menempatkan tanda mereka di kotak yang tersedia.
- Pengecekan otomatis untuk menentukan pemenang.
- Garis pemenang yang ditampilkan dengan jelas setelah ada pemenang.
- Kemampuan untuk memulai kembali permainan setelah selesai.
- Tampilan teks yang menunjukkan pemain mana yang menang.

## Cara Menggunakan

1. Pastikan Python dan modul Pygame sudah terinstal di komputer Anda.
2. Unduh semua file dari repositori ini.
3. Jalankan program dengan menjalankan file `tictactoe.py` menggunakan Python.
4. Ikuti petunjuk di layar untuk memainkan permainan.

## Algoritma Pengecekan Pemenang

- **Periksa Kemenangan Horizontal**: Algoritma ini memeriksa setiap baris pada papan permainan untuk melihat apakah terdapat tiga tanda yang sama secara horizontal. Jika ada, pemain dengan tanda tersebut dianggap sebagai pemenang.

- **Periksa Kemenangan Vertikal**: Algoritma ini memeriksa setiap kolom pada papan permainan untuk melihat apakah terdapat tiga tanda yang sama secara vertikal. Jika ada, pemain dengan tanda tersebut dianggap sebagai pemenang.

- **Periksa Kemenangan Diagonal**: Algoritma ini memeriksa dua diagonal utama pada papan permainan untuk melihat apakah terdapat tiga tanda yang sama secara diagonal. Jika ada, pemain dengan tanda tersebut dianggap sebagai pemenang.

- **Penanganan Kasus Khusus**: Algoritma juga menangani kasus khusus untuk diagonal kedua yang berlawanan, yaitu diagonal dari sudut kanan atas ke sudut kiri bawah. Ini dilakukan untuk memastikan semua kemungkinan kemenangan diagonal telah dipertimbangkan.

- **Kondisi Draw**: Jika tidak ada pemain yang memenangkan permainan dan semua kotak telah diisi tanpa ada pemenang yang terjadi, maka permainan dianggap seri (draw).

Algoritma ini diimplementasikan dalam fungsi `check_win(player)` dalam kode permainan Tic Tac Toe. Dengan menggunakan algoritma ini, permainan secara otomatis menentukan pemenang dan menampilkan pesan sesuai hasilnya.


