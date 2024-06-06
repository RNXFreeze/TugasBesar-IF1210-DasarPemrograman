# PROGRAM K05-C-F06

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : potion.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F06 - Potion
# Penanggung Jawab F06 : 19623065 / Muhammad Alfansya

# KAMUS
# potion : procedure

# ALGORITMA
def potion() :
    # SPESIFIKASI LOKAL
    # I.S. Jenis-jenis potion & efeknya telah terdefinisi di awal.
    # F.S. Menampilkan jenis-jenis potion beserta efeknya ke layar.

    # KAMUS LOKAL
    # keluar : boolean

    # ALGORITMA LOKAL
    print('''
    ▄▄▄·      ▄▄▄▄▄▪         ▐ ▄ .▄▄ · 
    ▐█ ▄█▪     •██  ██ ▪     •█▌▐█▐█ ▀. 
    ██▀· ▄█▀▄  ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄
    ▐█▪·•▐█▌.▐▌ ▐█▌·▐█▌▐█▌.▐▌██▐█▌▐█▄▪▐█
    .▀    ▀█▄▀▪ ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪ ▀▀▀▀ 
    ''')

    print('''
    Potion              | Effect
    Strength Potion     | Meningkatkan ATK Power sebanyak 5% dari ATK Power
    Resilience Potion   | Meningkatkan Def Power sebanyakk 5% dari DEF Power
    Healing Potion      | Mengisi darah sebanyak 25% dari Base HP, tidak akan mengisi lebih dari maks HP

    Tips! Gunakan potion yang tepat di saat yang tepat untuk melawan monster yang lebih kuat!
          Potion bisa dibeli di shop dengan OC.
''')
    keluar = False
    while (not(keluar)) :
        a = input('Masukkan "keluar" untuk kembali ke menu : ').lower()
        if (a == 'keluar') :
            keluar = True
    return()
