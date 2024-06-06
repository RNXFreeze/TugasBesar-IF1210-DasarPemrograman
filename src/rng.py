# PROGRAM K05-C-F00

# IDENTITAS 
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : rng.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F00 - Random Number Generator
# Penanggung Jawab F00 : 19623065 / Muhammad Alfansya

# KAMUS
# a , c , m , seed : integer
# create_lcg , lcg_func , generate : function

# ALGORITMA
import os , time
a = 19623065
c = 19623215
m = 2 ** 15
seed = int((os.getpid()) % (time.time()))
def create_lcg(seed=[int((os.getpid()) % (time.time()))]) :
    # SPESIFIKASI LOKAL
    # Fungsi ini akan mengeluarkan suatu bilangan unik tergantung dari Process ID dan Time saat digunakan.
     
    # KAMUS LOKAL
    # lcg : function
    # seed , a , c , m : integer

    # ALGORITMA LOKAL
    def lcg() :
        seed[0] = (a * seed[0] + c) % m
        return (seed[0])
    return (lcg)

lcg_func = create_lcg()
def generate(range) :
    # SPESIFIKASI LOKAL
    # Fungsi ini akan menerima masukan range [a , b + 1] lalu menghasilkan suatu random number integer dari a sampai b (a <= random number <= b).
    
    # KAMUS LOKAL
    # lcg_func : function
    # random_number , a , b , m , result : integer
    # range : array of integer

    # ALGORITMA LOKAL
    random_number = lcg_func()
    a , b = range
    b = b - 1
    result = int((random_number / (m - 1)) * (b - a + 1) + a)
    return (result)