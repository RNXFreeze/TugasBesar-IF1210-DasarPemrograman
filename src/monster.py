# PROGRAM K05-C-F05

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : monster.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F05 - Monster
# Penanggung Jawab F05 : 19623065 / Muhammad Alfansya

# KAMUS
# samain_panjang , print_mons , monster : procedure

# ALGORITMA
def samain_panjang(listmon) :
    # SPESIFIKASI LOKAL
    # Menyamakan panjang setiap subdata dari setiap monster.
    # I.S. Data listmon telah terdefinisi di awal.
    # F.S. Data list monster yang telah disesuaikan panjangnya tersimpan dalam variabel lain.

    # KAMUS LOKAL
    # listmon , hasil : matrix of data
    # b , i , j : integer (index)

    # ALGORITMA LOKAL
    hasil = ['' for i in range (len(listmon))]
    for i in range (len(listmon[0]) - 1) :
        b = 0
        for j in range(len(listmon)) :
            if (b < len(listmon[j][i])) :
                b = len(listmon[j][i])
        for j in range(len(listmon)):
            hasil[j] = hasil[j] + listmon[j][i]
            if (b > len(listmon[j][i])) :
                while (b > len(listmon[j][i])) :
                    hasil[j] = hasil[j] + " "
                    listmon[j][i] = listmon[j][i] + " "
            hasil[j] = hasil[j] + " | "
    for i in range (len(listmon)) :
        hasil[i] = hasil[i] + listmon[i][len(listmon[0]) - 1]
    return (hasil)

def print_mons(listmon) :
    # SPESIFIKASI LOKAL
    # Menampilkan data tiap monster ke layar.
    # I.S. Data listmon telah terdefinisi di awal.
    # F.S. Menampilkan satu per satu data listmon ke layar.

    # KAMUS LOKAL
    # samain_panjang : procedure
    # listmon , listmons : matrix of data
    # i , j : integer (index)

    # ALGORITMA LOKAL
    listmons = samain_panjang(listmon)
    for i in range ((len(listmons))) :
        for j in range (len(listmons[i]) - 1) :
            print(listmons[i][j] , end = "")
        print(listmons[i][len(listmons[i]) - 1])
    return()

def monster(listmon) :
    # Menampilkan data tentang monster dalam permainan.
    # I.S : Data listmon telah terdefinisi di awal.
    # F.S : Data listmon ditampilkan ke layar.

    # KAMUS LOKAL
    # print_mons : procedure
    # listmon : matrix of data
    # a : string
    # keluar : boolean

    # ALGORITMA LOKAL
    print('''
<!--  _____                                                            _____  -->
<!-- ( ___ )----------------------------------------------------------( ___ ) -->
<!--  |   |      _____        ______    _         ____  _______  __    |   |  -->
<!--  |   |     / _ \ \      / / ___|  / \       |  _ \| ____\ \/ /    |   |  -->
<!--  |   |    | | | \ \ /\ / / |     / _ \      | | | |  _|  \  /     |   |  -->
<!--  |   |    | |_| |\ V  V /| |___ / ___ \     | |_| | |___ /  \     |   |  -->
<!--  |   |     \___/  \_/\_/  \____/_/   \_\    |____/|_____/_/\_\    |   |  -->
<!--  |___|                                                            |___|  -->
<!-- (_____)----------------------------------------------------------(_____) -->
''')
    print("WELCOME TO OWCA-DEX UNTUK MELIHAT MONSTER YANG TERSEDIA, AGEN!")
    print_mons(listmon)
    print("Informasi tambahan owca-dex mengenai level :")
    print("Level 1     : Monster menggunakan Base Attribute")
    print("Level 2 - 5 : Ketika sedang Battle, Base Attribute monster ditambah dengan Base Attribute dikalikan dengan ((Level - 1) * 10)%.")
    print("              Ketika monster naik level, Base Attribute tetap disimpan, kalkulasi atribut sesuai level dilakukan saat Battle.")
    print("Tips! Cek level monstermu pada inventory, gunakan command 'inventory'!")
    keluar = False
    while (not(keluar)) :
        a = input('Masukkan "keluar" untuk kembali ke menu : ').lower()
        if (a == "keluar") :
            keluar = True
    return()
