# PROGRAM K05-C-F01

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : register.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F01 - Register
# Penanggung Jawab F01 : 19623215 / Muhammad Raihan Nazhim Oktana

# KAMUS
# register , convert : procedure

# ALGORITMA
import time
def convert(string) :
    # SPESIFIKASI LOKAL
    # Memecah suatu string menjadi list / array of character.
    # I.S. Menerima input berupa string yang telah terdefinisi di awal.
    # F.S. String telah terpecah menjadi suatu list / array of character.

    # KAMUS LOKAL
    # string : string
    # array : list / array of character
    # i : integer (index)

    # ALGORITMA LOKAL
    array = []
    for i in range (len(string)) :
        array.append(string[i])
    return (array)

def register(check_login , username_login , user , monster , inv_item , inv_monster) :
    # SPESIFIKASI LOKAL
    # Melakukan proses register seorang pengguna baru.
    # I.S. Data check_login, username_login, user, monster, inv_item, dan inv_monster telah terdefinisi di awal.
    # F.S. Data pengguna baru telah tersimpan setelah memasukkan username dan password serta pilihan monster awal.

    # KAMUS LOKAL
    # convert : procedure
    # user , monster , inv_item , inv_monster : matrix of data
    # array_username , allowed_character : array of character
    # check_login , check : boolean
    # username_login , username , password , role : string
    # uid , oc , putar , level , quantity , accepted_character , starting_monster : integer
    # i , j : integer (index) 

    # ALGORITMA LOKAL
    print(">>> REGISTER")
    print("")
    print("________      _______       ________      ___      ________       _________    _______       ________      ")
    print("|\   __  \    |\  ___ \     |\   ____\    |\  \    |\   ____\     |\___   ___\ |\  ___ \     |\   __  \    ")
    print("\ \  \|\  \   \ \   __/|    \ \  \___|    \ \  \   \ \  \___|_    \|___ \  \_| \ \   __/|    \ \  \|\  \   ")
    print(" \ \   _  _\   \ \  \_|/__   \ \  \  ___   \ \  \   \ \_____  \        \ \  \   \ \  \_|/__   \ \   _  _\  ")
    print("  \ \  \\  \|   \ \  \_|\ \   \ \  \|\  \   \ \  \   \|____|\  \        \ \  \   \ \  \_|\ \   \ \  \\  \| ")
    print("   \ \__\\ _\    \ \_______\   \ \_______\   \ \__\    ____\_\  \        \ \__\   \ \_______\   \ \__\\ _\ ")
    print("    \|__|\|__|    \|_______|    \|_______|    \|__|   |\_________\        \|__|    \|_______|    \|__|\|__|")
    print("                                                      \|_________|                                         ")
    print("")
    if (check_login) :
        print(f'Register gagal!\nAnda telah login dengan username {username_login}, silakan lakukan "LOGOUT" sebelum melakukan register.')
    else :
        accepted_character = 0
        array_username = ["-"]
        putar = 1
        while (accepted_character != len(array_username)) :
            if (putar > 1) :
                print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            accepted_character = 0
            check = False
            while (not(check)) :
                username = str(input("Masukkan Username : "))
                password = str(input("Masukkan Password : "))
                uid = len(user)
                allowed_character = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P','p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' , '-' , '_']
                check = True
                for i in range (len(user)) :
                    if ((user[i][1]) == username) :
                        check = False
                        print(f"Username {username} sudah terpakai, silakan gunakan username lain!")
                        break
            if (username == "") :
                print("Username tidak boleh kosong!")
            else :
                array_username = convert(username)
                for i in range (len(array_username)) :
                    for j in range (len(allowed_character)) :
                        if (array_username[i] == allowed_character[j]) :
                            accepted_character = accepted_character + 1
                            break
            putar = putar + 1
        time.sleep(1)
        print("Silakan pilih dalah satu monster sebagai monster awalmu!")
        for i in range (1 , 4) :
            print(f"{i}. {monster[i][1]}")
        starting_monster = str(input("Masukkan Pilihanmu (masukkan angka saja) : "))
        while ((starting_monster != '1') and (starting_monster != '2') and (starting_monster != '3')) :
            print("Monster pilihan Anda tidak tersedia, silakan pilih ulang!")
            starting_monster = str(input("Masukkan Pilihanmu (masukkan angka saja) : "))
        starting_monster = int(starting_monster)
        time.sleep(1)
        uid = str(uid)
        role = "Agent"
        oc = "0"
        user = user + [[uid , username , password , role , oc]]
        level = "1"
        inv_monster = inv_monster + [[uid , monster[starting_monster][0] , level]]
        quantity = "0"
        inv_item  = inv_item + [[uid , "strength" , quantity] , [uid , "resilience" , quantity] , [uid , "healing" , quantity]]
        check_login = False
        username_login = ""
        print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster[starting_monster][1]}!")        
    return (check_login , username_login , user , monster , inv_item , inv_monster)
