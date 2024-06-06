# PROGRAM K05-C-F16

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : exit.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F16 - Exit
# Penanggung Jawab F16 : 19623215 / Muhammad Raihan Nazhim Oktana

# KAMUS
# exit , save : procedure

# ALGORITMA
from src.save import save
def exit(check_logres , user , monster , inv_item , inv_monster , shop_item , shop_monster) :
    # SPESIFIKASI LOKAL
    # Melakukan proses keluar dari program yang sedang berjalan.

    # KAMUS LOKAL
    # save : procedure
    # user , monster , inv_item , inv_monster , shop_item , shop_monster : matrix of data
    # check_logres , end : boolean
    # ending : character
    
    # ALGORITMA LOKAL
    import time
    print(">>> EXIT")
    print("")
    print("_______       ___    ___  ___      _________     ")
    print("|\  ___ \     |\  \  /  /||\  \    |\___   ___\  ")
    print("\ \   __/|    \ \  \/  / /\ \  \   \|___ \  \_|  ")
    print(" \ \  \_|/__   \ \    / /  \ \  \       \ \  \   ")
    print("  \ \  \_|\ \   /     \/    \ \  \       \ \  \  ")
    print("   \ \_______\ /  /\   \     \ \__\       \ \__\ ")
    print("    \|_______|/__/ /\ __\     \|__|        \|__| ")
    print("              |__|/ \|__|                        ")
    print("")
    if (check_logres) :
        ending = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) : ").upper()
        while not ((ending == "Y") or (ending == "N")) :
            print("Masukan Anda tidak valid, silakan ulangi kembali!")
            ending = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) : ").upper()
        if (ending == "Y") :
            time.sleep(1)
            save(user, monster , inv_item , inv_monster , shop_item , shop_monster)
    else :
        print("Tidak ada program yang sedang berjalan.")
    end = True
    return (end)