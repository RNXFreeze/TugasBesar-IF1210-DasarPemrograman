# PROGRAM K05-C-F02

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : login.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F02 - Login
# Penanggung Jawab F02 : 16523245 / Dede Firman

# KAMUS
# login : procedure

# ALGORITMA
def login(data_user , check_login , username_login , admin , user_loggedin) :
    # SPESIFIKASI LOKAL
    # Melakukan proses login seorang pengguna.
    # I.S. Data user dan login telah terdefinisi di awal.
    # F.S. Memperbarui data user_loggedin terbaru jika dilakukan proses login.
    
    # KAMUS LOKAL
    # data_user , user : matrix of data
    # user_loggedin : array of string
    # username_login , password : string
    # check_login , check1 , check2 , admin : boolean
    # i : integer (index)

    # ALGORITMA LOKAL
    print(" .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.")
    print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print("| |   _____      | || |     ____     | || |    ______    | || |     _____    | || | ____  _____  | |")
    print("| |  |_   _|     | || |   .'    `.   | || |  .' ___  |   | || |    |_   _|   | || ||_   \|_   _| | |")
    print("| |    | |       | || |  /  .--.  \  | || | / .'   \_|   | || |      | |     | || |  |   \ | |   | |")
    print("| |    | |   _   | || |  | |    | |  | || | | |    ____  | || |      | |     | || |  | |\ \| |   | |")
    print("| |   _| |__/ |  | || |  \  `--'  /  | || | \ `.___]  _| | || |     _| |_    | || | _| |_\   |_  | |")
    print("| |  |________|  | || |   `.____.'   | || |  `._____.'   | || |    |_____|   | || ||_____|\____| | |")
    print("| |              | || |              | || |              | || |              | || |              | |")
    print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
    print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'.")
    if (check_login) :
        print(f'Login gagal!\nAnda telah login dengan username {username_login}, silakan lakukan "LOGOUT" sebelum melakukan login kembali.')
    else :
        user = data_user
        while (not(check_login)) :
            check1 = False
            check2 = False
            while ((not(check1)) or (not(check2))) :
                username_login = input("Masukkan Username : ")
                password = input("Masukkan Password : ")
                for i in range (len(user)) :
                    if (user[i][1] == username_login) :
                        check1 = True
                        if (user[i][2] == password) :
                            check2 = True
                            check_login = True
                        break
                if ((check1) and (check2)) :
                    if (user[i][3] == 'Admin') :
                        admin = True
                    else:
                        admin = False
                    user_loggedin = user[i]
                elif ((check1) and (not(check2))) :
                    print("Password salah!")
                else :
                    print("Username tidak terdaftar! \nSilakan register terlebih dahulu!")
                    return (check_login , username_login , admin , user_loggedin)
                break
        print(f'Selamat datang, Agent {username_login}!\nMasukkan command "help" untuk daftar perintah yang dapat kamu panggil.')
    return (check_login , username_login , admin , user_loggedin)
