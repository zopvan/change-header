import os
import random

def rusak_satu_folder(nama_folder):
    # 1. Cek apakah folder target ada
    if not os.path.exists(nama_folder):
        print(f"Error: Folder '{nama_folder}' tidak ditemukan!")
        return

    print(f"--- MULAI OPERASI PADA FOLDER: {nama_folder} ---")
    
    # Ambil daftar semua item di dalam folder
    list_file = os.listdir(nama_folder)
    
    # === [BARU] VALIDASI FOLDER KOSONG ===
    if len(list_file) == 0:
        print(f"⚠️  VALIDASI: Folder '{nama_folder}' KOSONG melompong.")
        print("   Tidak ada file yang diubah headernya.")
        return  # <-- Stop di sini, kembali ke menu utama
    # =====================================

    jumlah_sukses = 0

    # 2. Lakukan Looping (Perulangan) untuk setiap file
    for nama_file in list_file:
        full_path = os.path.join(nama_folder, nama_file)

        # 3. Pastikan yang kita proses adalah FILE (bukan folder lain)
        if os.path.isfile(full_path):
            try:
                with open(full_path, 'r+b') as f:
                    header_acak = os.urandom(16)
                    f.seek(0)
                    f.write(header_acak)
                
                print(f"[RUSAK] {nama_file} -> Header diganti random.")
                jumlah_sukses += 1
                
            except Exception as e:
                print(f"[GAGAL] {nama_file}: {e}")
        else:
            print(f"[SKIP] {nama_file} adalah folder, dilewati.")

    print("-" * 40)
    # Validasi tambahan: Jika folder ada isinya tapi isinya folder semua (bukan file)
    if jumlah_sukses == 0:
        print(f"Info: Folder '{nama_folder}' tidak kosong, tapi tidak ada FILE yang bisa dirusak.")
    else:
        print(f"SELESAI. Total {jumlah_sukses} file telah dirusak di folder '{nama_folder}'.")

# ==========================================
# EKSEKUSI
# ==========================================
target_folder = 'src'

print(f"PERINGATAN: Semua file di dalam folder '{target_folder}' akan corrupt.")
konfirmasi = input("Ketik 'GAS' untuk melanjutkan: ")

if konfirmasi == 'GAS':
    rusak_satu_folder(target_folder)
else:
    print("Dibatalkan.")