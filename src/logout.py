# PROGRAM K05-C-F03

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : logout.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F03 - Logout
# Penanggung Jawab F03 : 16523135 / Aleta Edna Jessalyn

# KAMUS
# logout : procedure

# ALGORITMA
def logout(check_login) :
    # SPESIFIKASI LOKAL
    # I.S. Variabel check_login telah terdefinisi di awal.
    # F.S. Variabel check_login berubah menjadi False di akhir.
    
    # KAMUS LOKAL
    # check_login : boolean

    # ALGORITMA LOKAL
    if (check_login) :
        print("Logout berhasil!")
        print("   .---.   .--.             ,---.     .--.   ,-.    ,---.    ,---.   ,---.       .-, .-. .-.           ,---.     .--.     ,-.       .--.     ,--,   ,-. ")
        print(" (  .-._) / /\ \  |\    /|  | .-.\   / /\ \  |(|    | .-.\   | .-'   | .-.\      | | | | | | |\    /|  | .-.\   / /\ \    | |      / /\ \  .' .'    |(| ")
        print(" (_) \   / /__\ \ |(\  / |  | |-' ) / /__\ \ (_)    | |-' \  | `-.   | `-'/      | | | | | | |(\  / |  | |-' ) / /__\ \   | |     / /__\ \ |  |  __ (_)") 
        print(" _  \ \  |  __  | (_)\/  |  | |--'  |  __  | | |    | |--. \ | .-'   |   (       | | | | | | (_)\/  |  | |--'  |  __  |   | |     |  __  | \  \ ( _)| | ")
        print("( `-'  ) | |  |)| | \  / |  | |     | |  |)| | |    | |`-' / |  `--. | |\ \   (`-' | | `-')| | \  / |  | |     | |  |)|   | `--.  | |  |)|  \  `-) )| | ")
        print(" `----'  |_|  (_) | |\/| |  /(      |_|  (_) `-'    /( `--'  /( __.' |_| \)\   \_ )| `---(_) | |\/| |  /(      |_|  (_)   |( __.' |_|  (_)  )\____/ `-' ")
        print("                  '-'  '-' (__)                    (__)     (__)         (__)    (_)         '-'  '-' (__)                (_)              (__)")
    else :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu.")
    check_login = False
    return (check_login)
