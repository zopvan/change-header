import os
import random

def rusak_satu_folder(nama_folder):
    # 1. Cek apakah folder target ada
    if not os.path.exists(nama_folder):
        print(f"Error: Folder '{nama_folder}' tidak ditemukan!")
        return

    print(f"--- MULAI OPERASI PADA FOLDER: {nama_folder} ---")
    
    # Lihat dan Ambil daftar semua item di dalam folder
    list_file = os.listdir(nama_folder)
    
    # validasi apakah folde kosong??
    if len(list_file) == 0:
        print(f"⚠️  VALIDASI: Folder '{nama_folder}' KOSONG coy.")
        print("   Tidak ada file yang diubah headernya.")
        return  # <-- jika tidak ada akan berhenti di sini dan kembali ke menu utama
    # =====================================

    jumlah_sukses = 0

    # 2. Melakukan Looping (Perulangan) 
    # untuk setiap file untuk memproses 1 per 1
    for nama_file in list_file:
        full_path = os.path.join(nama_folder, nama_file) #memberi tahu full path (contoh file foto.jpg terdapat pada src maka src/foto.jpg)

        # 3. validasi proses adalah FILE (bukan folder lain)
        # jadi kalo folder dia akan skip prosesnya
        if os.path.isfile(full_path):
            try:
                with open(full_path, 'r+b') as f: #membuka file sebagai membaca dan menulis file dalam bentuk binary
                    header_acak = os.urandom(16) #menghasilkan str byte acak sebanyak 16byte
                    f.seek(0) #memindah kursor ke awal pada header file
                    f.write(header_acak) #menimpa 16 byte awal pada header file
                
                print(f"[RUSAK] {nama_file} -> Header diganti random.")
                jumlah_sukses += 1
                
            except Exception as e:
                print(f"[GAGAL] {nama_file}: {e}")
        else:
            print(f"[SKIP] {nama_file} adalah folder, dilewati.")

    print("-" * 40)
    
    # menampilkan status, header sukses ditimpa atau tidak 
    if jumlah_sukses == 0:
        print(f"Info: Folder '{nama_folder}' tidak kosong, tapi tidak ada FILE yang bisa dirusak.")
    else:
        print(f"SELESAI. Total {jumlah_sukses} file telah dirusak di folder '{nama_folder}'.")

# ==========================================
# EKSEKUSI sc
# ==========================================
target_folder = 'src'

print(f"PERINGATAN: Semua file di dalam folder '{target_folder}' akan corrupt.")
konfirmasi = input("Ketik 'GAS' untuk melanjutkan: ")

if konfirmasi == 'GAS':
    rusak_satu_folder(target_folder)
else:
    print("Dibatalkan.")