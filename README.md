Skrip mengubah header file untuk matakuliah Sistem Operasi

⚠️ PERINGATAN KERAS: Script ini bersifat DESTRUKTIF. File yang diproses akan rusak secara permanen (kecuali kamu memiliki backup). Gunakan hanya pada file percobaan (dummy files).

# Change Header

Project ini adalah script Python sederhana yang dirancang untuk mendemonstrasikan konsep File Header (Magic Numbers) dan manipulasi binary file. Script ini bekerja dengan cara menimpa 16 byte pertama dari sebuah file dengan data acak (random hex), sehingga file tersebut tidak dapat dikenali lagi oleh Sistem Operasi atau aplikasi pembuka file.

# Cara pakai
1. Pastikan Python 3 sudah terinstal pada perangkat anda.
2. Siapkan folder `src` di lokasi yang sama dengan `main.py`, lalu isi dengan file yang ingin diubah.
3. Jalankan dengan:
   ''''py main.py''''
4. Boom jika jalan file dalam folder `src` tidak dapat dibuka

# Yang dilakukan skrip
- Membaca semua file pada folder `src`, melewati folder, dan memproses hanya file.
- Menimpa hingga 16 byte pertama dengan nilai acak sehingga header rusak.
- Menampilkan laporan kemajuan, file yang dilewati, dan ringkasan final di terminal.

# Catatan❗❗
- Jangan menggunakan file yang penting
- File yang sudah diproses oleh script kemungkinan besar tidak bisa dibuka normal karena header rusak. Jangan lupa simpan cadangan file asli di luar `Src` bila diperlukan.