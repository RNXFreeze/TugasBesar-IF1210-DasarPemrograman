# PROGRAM K05-C-F04

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : help.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F04 - Menu & Help
# Penanggung Jawab F04 - 1 : 19623055 / Athian Nugraha Muarajuang
# Penanggung Jawab F04 - 2 : 19623065 / Muhammad Alfansya

# KAMUS
# help , menu : procedure

# ALGORITMA
def help(check_login, username , admin) :
    # SPESIFIKASI LOKAL
    # Subprogram dapat menunjukkan serangkaian perintah help yang dapat diakses di dalam program.
    # I.S. Program telah berjalan sebelumnya.
    # F.S. Menampilkan serangkaian help yang dapat diakses.

    # KAMUS LOKAL
    # check_login , admin : boolean
    # username : string

    # ALGORITMA LOKAL
    if (not(check_login)) :        
        print('''                    
                        <!-- ╔══════════════════════════════════╗ -->
                        <!-- ║                                  ║ -->
                        <!-- ║ ██╗  ██╗███████╗██╗     ██████╗  ║ -->
                        <!-- ║ ██║  ██║██╔════╝██║     ██╔══██╗ ║ -->
                        <!-- ║ ███████║█████╗  ██║     ██████╔╝ ║ -->
                        <!-- ║ ██╔══██║██╔══╝  ██║     ██╔═══╝  ║ -->
                        <!-- ║ ██║  ██║███████╗███████╗██║      ║ -->
                        <!-- ║ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝      ║ -->
                        <!-- ║                                  ║ -->
                        <!-- ╚══════════════════════════════════╝ -->
    
    Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.

    1. Register - melakukan registrasi user baru
    2. Login - melakukan login ke akun ter-register
    3. Exit - Keluar dari permainan 

    ========================================================== FOOTNOTE ==============================================================
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.
    2. Jangan lupa untuk memasukkan input yang valid!! 
    ''')
    else :
        if (not(admin)) :
            print(f'''                   
                        <!-- ╔══════════════════════════════════╗ -->
                        <!-- ║                                  ║ -->
                        <!-- ║ ██╗  ██╗███████╗██╗     ██████╗  ║ -->
                        <!-- ║ ██║  ██║██╔════╝██║     ██╔══██╗ ║ -->
                        <!-- ║ ███████║█████╗  ██║     ██████╔╝ ║ -->
                        <!-- ║ ██╔══██║██╔══╝  ██║     ██╔═══╝  ║ -->
                        <!-- ║ ██║  ██║███████╗███████╗██║      ║ -->
                        <!-- ║ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝      ║ -->
                        <!-- ║                                  ║ -->
                        <!-- ╚══════════════════════════════════╝ -->
Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. 
Berikut adalah hal-hal yang dapat kamu lakukan sekarang:

    1. Logout - Keluar dari akun 
    2. Monster - Melihat owca-dex yang dimiliki oleh Agent
    3. Potion - Melihat jenis - jenis potion beserta efeknya
    4. Inventory - Melihat isi inventory milik Agent
    5. Battle - Bertarung dengan monster secara acak secara 1v1
    6. Arena - Memasuki arena bertarung yang berisi 5 stage
    7. Shop - Tempat Agent untuk membeli monster dan potion
    8. Laboratory - Tempat Agent untuk upgrade monster yang ada di inventory
    9. Save - Menyimpan data permainan
    10. Exit - Keluar dari permainan

    ========================================================== FOOTNOTE ==============================================================
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.
    2. Jangan lupa untuk memasukkan input yang valid!!    ''')
        else :
            print(f'''                    
                        <!-- ╔══════════════════════════════════╗ -->
                        <!-- ║                                  ║ -->
                        <!-- ║ ██╗  ██╗███████╗██╗     ██████╗  ║ -->
                        <!-- ║ ██║  ██║██╔════╝██║     ██╔══██╗ ║ -->
                        <!-- ║ ███████║█████╗  ██║     ██████╔╝ ║ -->
                        <!-- ║ ██╔══██║██╔══╝  ██║     ██╔═══╝  ║ -->
                        <!-- ║ ██║  ██║███████╗███████╗██║      ║ -->
                        <!-- ║ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝      ║ -->
                        <!-- ║                                  ║ -->
                        <!-- ╚══════════════════════════════════╝ -->
Selamat datang, Admin {username}. Berikut adalah hal-hal yang dapat kamu lakukan:

    1. Logout - Untuk melakukan registrasi user baru
    2. Shop - Mengatur isi shop, baik menambah stok maupun mengurangi stok
    3. Monster - mengatur monster dalam database
    4. Save - Menyimpan data permainan
    5. Exit - Keluar dari permainan

    ========================================================== FOOTNOTE ==============================================================
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.
    2. Jangan lupa untuk memasukkan input yang valid!! 
''')
    keluar = False
    while not(keluar):
        a = input("'keluar' untuk kembali ke menu : ").lower()
        if a == 'keluar':
            keluar = True

def menu(check_login, username , admin) :
    # SPESIFIKASI LOKAL
    # Subprogram dapat menunjukkan serangkaian perintah menu yang dapat diakses di dalam program.
    # I.S. Program telah berjalan sebelumnya.
    # F.S. Menampilkan serangkaian menu yang dapat diakses.

    # KAMUS LOKAL
    # check_login , admin : boolean
    # username : string

    # ALGORITMA LOKAL
    if (not(check_login)) :        
        print('''
            <!-- ╔════════════════════════════════════════════════════════════════╗ -->
            <!-- ║                                                                ║ -->
            <!-- ║ ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗ ║ -->
            <!-- ║ ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝ ║ -->
            <!-- ║ ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗   ║ -->
            <!-- ║ ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝   ║ -->
            <!-- ║ ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗ ║ -->
            <!-- ║  ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝ ║ -->
            <!-- ║                                                                ║ -->
            <!-- ╚════════════════════════════════════════════════════════════════╝ -->
Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.

    1. Register - melakukan registrasi user baru
    2. Login - melakukan login ke akun ter-register
    3. Exit - Keluar dari permainan 

    ========================================================== FOOTNOTE ==============================================================
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.
    2. Jangan lupa untuk memasukkan input yang valid!! 
    ''')
    else :
        if (not(admin)) :
            print(f'''
                            <!-- ╔════════════════════════════════════════╗ -->
                            <!-- ║                                        ║ -->
                            <!-- ║ ███╗   ███╗███████╗███╗   ██╗██╗   ██╗ ║ -->
                            <!-- ║ ████╗ ████║██╔════╝████╗  ██║██║   ██║ ║ -->
                            <!-- ║ ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║ ║ -->
                            <!-- ║ ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║ ║ -->
                            <!-- ║ ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝ ║ -->
                            <!-- ║ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ║ -->
                            <!-- ║                                        ║ -->
                            <!-- ╚════════════════════════════════════════╝ -->

Halo Agent {username}. Berikut adalah hal hal yang kamu lakukan. Selamat berpetualang bersama monster pilihanmu! 
Berikut adalah hal-hal yang dapat kamu lakukan sekarang:

    1. Logout - Keluar dari akun 
    2. Monster - Melihat owca-dex yang dimiliki oleh Agent
    3. Potion - Melihat jenis - jenis potion beserta efeknya
    4. Inventory - Melihat isi inventory milik Agent
    5. Battle - Bertarung dengan monster secara acak secara 1v1
    6. Arena - Memasuki arena bertarung yang berisi 5 stage
    7. Shop - Tempat Agent untuk membeli monster dan potion
    8. Laboratory - Tempat Agent untuk upgrade monster yang ada di inventory
    9. Save - Menyimpan data permainan
    10. Exit - Keluar dari permainan

    ========================================================== FOOTNOTE ==============================================================
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.
    2. Jangan lupa untuk memasukkan input yang valid!!    ''')
        else :
            print(f'''                        
                            <!-- ╔════════════════════════════════════════╗ -->
                            <!-- ║                                        ║ -->
                            <!-- ║ ███╗   ███╗███████╗███╗   ██╗██╗   ██╗ ║ -->
                            <!-- ║ ████╗ ████║██╔════╝████╗  ██║██║   ██║ ║ -->
                            <!-- ║ ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║ ║ -->
                            <!-- ║ ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║ ║ -->
                            <!-- ║ ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝ ║ -->
                            <!-- ║ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ║ -->
                            <!-- ║                                        ║ -->
                            <!-- ╚════════════════════════════════════════╝ -->
Selamat datang, Admin {username}. Berikut adalah hal-hal yang dapat kamu lakukan:

    1. Logout - Untuk melakukan registrasi user baru
    2. Shop - Mengatur isi shop, baik menambah stok maupun mengurangi stok
    3. Monster - mengatur monster dalam database
    4. Save - Menyimpan data permainan
    5. Exit - Keluar dari permainan

    ========================================================== FOOTNOTE ==============================================================
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.
    2. Jangan lupa untuk memasukkan input yang valid!! 
''')