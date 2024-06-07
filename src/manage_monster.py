# PROGRAM K05-C-F13

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : manage_monster.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F13 - Monster Management
# Penanggung Jawab F13 : 16523135 / Aleta Edna Jessalyn

# KAMUS
# monster_mng : function
# samain_panjang , print_mons , delarraymanual , ceknama , cekint , cekdef , ceklen , cekar , cekinputawal , IsDigit : procedure

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
        for j in range(len(listmon)) :
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

def delarraymanual(listmonns , array_index) :
    # SPESIFIKASI LOKAL
    # Menghapus suatu data pada listmonns sesuai index yang diinginkan.
    # I.S. Data listmonss dan nilai variabel array_index telah terdefinisi di awal.
    # F.S. Nilai boolean true / false dikembalikan di akhir.

    # KAMUS LOKAL
    # listmonns : matrix of data
    # listmonbaru : array of data
    # array_index , i : integer (index)

    # ALGORITMA LOKAL
    listmonbaru = []
    for i in range (len(listmonns)) :
        if (i != array_index) :
            listmonbaru.append(listmonns[i])
    return (listmonbaru)

def ceknama(instr) :
    # SPESIFIKASI LOKAL
    # Mengecek apakah input nama yang dimasukkan valid atau tidak.
    # I.S. Nilai variabel instr telah terdefinisi di awal.
    # F.S. Nilai boolean true / false dikembalikan di akhir.

    # KAMUS LOKAL
    # ceknem : array of integer
    # instr : string
    # char : character
    # f : boolean
    # i : integer(index)

    # ALGORITMA LOKAL
    ceknem = [ord(char) for (char) in (instr)]
    f = True
    for i in range (len(ceknem)) :
        if (not((65 <= ceknem[i] <= 90) or (97 <= ceknem[i] <= 122))) :
            f = False
    return (f)

def cekint(inint) :
    # SPESIFIKASI LOKAL
    # Mengecek apakah inint tersebut adalah suatu integer yang tidak negatif atau bukan.
    # I.S. Data inint telah terdefinisi di awal.
    # F.S. Pernyataan true / false dikembalikan di akhir.

    # KAMUS LOKAL
    # cekinte : array of integer
    # inint : string
    # f : boolean
    # i : integer (index)

    # ALGORITMA LOKAL
    cekinte = [ord(char) for (char) in (inint)]
    f = True
    for i in range (len(cekinte)) :
        if (not(48 <= cekinte[i] <= 57)) :
            f = False
    return (f)

def cekdef(indef) :
    # SPESIFIKASI LOKAL
    # Mengecek apakah nilai input def yang dimasukkan telah sesuai spesifikasi.
    # I.S. Nilai variabel indef telah terdefinisi di awal.
    # F.S. Nilai boolean true / false dikembalikan di akhir.

    # KAMUS LOKAL
    # cekdeff : array of integer
    # indef : string

    # ALGORITMA LOKAL
    cekdeff = [ord(char) for (char) in (indef)]
    if (len(cekdeff) == 2) :
        if (49 <= cekdeff[0] <= 52) :
            return (True)
        elif ((cekdeff[0] == 53) and (cekdeff[1] == 48)) :
            return (True)
        else :
            return (False)
    elif (len(cekdeff) == 1) :
        return (True)
    else :
        return (False)
    
def ceklen(instr) :
    # SPESIFIKASI LOKAL
    # Mengecek apakah panjang string 0 atau tidak.
    # I.S. Nilai variabel instr telah terdefinisi di awal.
    # F.S. Nilai boolean true / false dikembalikan di akhir.

    # KAMUS LOKAL
    # instr : string

    # ALGORITMA LOKAL
    if (len(instr) == 0) :
        return (False)
    return (True)

def cekar(instr , cekarray) :
    # SPESIFIKASI LOKAL
    # Mengecek apakah suatu string terdapat dalam suatu array atau tidak.
    # I.S. Nilai variabel instr dan cekarray telah terdefinisi di awal.
    # F.S. Nilai boolean true / false dikembalikan di akhir.

    # KAMUS LOKAL
    # instr : string
    # cekarray : array of string
    # f : boolean
    # i : integer (index)

    # ALGORITMA LOKAL
    f = True
    for i in range (len(cekarray)) :
        if (str(instr) == cekarray[i][1]) :
            f = False
    return (f)

def IsDigit(stri) :
    # SPESIFIKASI LOKAL
    # Mengecek apakah suatu string adalah suatu bilangan bulat tidak negatif atau bukan.
    # I.S. Nilai variabel stri telah terdefinisi di awal.
    # F.S. Nilai boolean true / false dikembalikan di akhir.

    # KAMUS LOKAL
    # char : character
    # stri : string
    # i : integer (index)

    # ALGORITMA LOKAL
    for (char) in (stri) :
        if ((char) not in (chr(i) for i in range (48, 57))) :
            return (False)
    return (True)

def cekinputawal(inte) :
    # SPESIFIKASI LOKAL
    # Mengecek apakah suatu integer adalah 1 atau 2 atau lainnya.
    # I.S. Nilai variabel inte telah terdefinisi di awal.
    # F.S. Nilai boolean true / false dikembalikan di akhir.

    # KAMUS LOKAL
    # inte : integer

    # ALGORITMA LOKAL
    if ((inte == 1) or (inte == 2)) :
        return (True)
    else :
        return (False)

def monster_mng(listmon) :
    # SPESIFIKASI LOKAL
    # Membuat fungsi manage monster yang dapat mengatur monster sesuai spesifikasi.

    # KAMUS LOKAL
    # samain_panjang , print_mons , delarraymanual , ceknama , cekint , cekdef , ceklen , cekar , cekinputawal , IsDigit : procedure
    # listmon , listmonbaru : matrix of data
    # arr1 , MonsterBaru : array of data
    # arr : array of string
    # nama , a , k , h , confirm : string
    # lanjut , tambah : boolean
    # atk , def , hp : integer

    # ALGORITMA LOKAL
    print("   .---.  ,---.   ,-.       .--.              .--.    _______    ,'|'\     .--.    _______   .--.    .-. .-.   ,--,      ,'|'\   ,-. ")
    print("  ( .-._) | .-'   | |      / /\ \  |\    /|  / /\ \  |__   __|   | |\ \   / /\ \  |__   __| / /\ \   |  \| | .' .'       | |\ \  |(| ")
    print(" (_) \    | `-.   | |     / /__\ \ |(\  / | / /__\ \   )| |      | | \ \ / /__\ \   )| |   / /__\ \  |   | | |  |  __    | | \ \ (_) ")
    print(" _  \ \   | .-'   | |     |  __  | (_)\/  | |  __  |  (_) |      | |  \ \|  __  |  (_) |   |  __  |  | |\  | \  \ ( _)   | |  \ \| | ")
    print("( `-'  )  |  `--. | `--.  | |  |)| | \  / | | |  |)|    | |      /(|`-' /| |  |)|    | |   | |  |)|  | | |)|  \  `-) )   /(|`-' /| | ")
    print(" `----'   /( __.' |( __.' |_|  (_) | |\/| | |_|  (_)    `-'     (__)`--' |_|  (_)    `-'   |_|  (_)  /(  (_)  )\____/   (__)`--' `-' ")
    print("         (__)     (_)              '-'  '-'                                                         (__)     (__)                    ")
    print("         ,'|'\     .--.    _______   .--.    ,---.     .--.      .---.  ,---.      ,---.     .--.   ,---.      .--.                  ")
    print("         | |\ \   / /\ \  |__   __| / /\ \   | .-.\   / /\ \    ( .-._) | .-'      | .-.\   / /\ \  | .-.\    / /\ \                 ")
    print("         | | \ \ / /__\ \   )| |   / /__\ \  | |-' \ / /__\ \  (_) \    | `-.      | |-' ) / /__\ \ | `-'/   / /__\ \                ")
    print("         | |  \ \|  __  |  (_) |   |  __  |  | |--. \|  __  |  _  \ \   | .-'      | |--'  |  __  | |   (    |  __  |                ")
    print("         /(|`-' /| |  |)|    | |   | |  |)|  | |`-' /| |  |)| ( `-'  )  |  `--.    | |     | |  |)| | |\ \   | |  |)|                ")
    print("         (__)`--' |_|  (_)    `-'   |_|  (_)  /( `--' |_|  (_)  `----'   /( __.'    /(      |_|  (_) |_| \)\  |_|  (_)               ")
    print("                                    (__)                       (__)       (__)                  (__)                                 ")
    print("                         ▄▀▀▄ ▄▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▀▄  ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄                                            ")
    print("                         █  █ ▀  █ █      █ █  █ █ █ █ █   ▐ █    █  ▐ ▐  ▄▀   ▐ █   █   █                                           ")
    print("                         ▐  █    █ █      █ ▐  █  ▀█    ▀▄   ▐   █       █▄▄▄▄▄  ▐  █▀▀█▀                                            ")
    print("                           █    █  ▀▄    ▄▀   █   █  ▀▄   █     █        █    ▌   ▄▀    █                                            ")
    print("                         ▄▀   ▄▀     ▀▀▀▀   ▄▀   █    █▀▀▀    ▄▀        ▄▀▄▄▄▄   █     █                                             ")
    print("                         █    █             █    ▐    ▐      █          █    ▐   ▐     ▐                                             ")
    print("                         ▐    ▐             ▐                ▐          ▐                                                            ")
    print("Pilihan Aksi Tersedia :")
    print("1. Tampilkan semua monster")
    print("2. Tambah monster baru")
    arr = ["ID" , "Type" , "ATK Power" , "DEF Power" , "HP"]
    listmonbaru = delarraymanual(listmon , 0)
    arr1 = [arr] + listmonbaru
    a = input("Pilih aksi : ")
    while (str(a) != "KELUAR") :
        while ((not(IsDigit(a))) or (not(cekinputawal(int(a))))) :
            print("Pilihan aksi tidak tersedia, pilih kembali!")
            a = input("Pilih aksi : ")
        if (int(a) == 1) :
            print_mons(arr1)
            lanjut = False
            confirm = input("Apakah mau melakukan hal lain? (Y/N) : ").upper()
            while (not(lanjut)) :
                if (str(confirm) == "Y") :
                    a = input("Pilih aksi : ")
                    lanjut = True
                elif (str(confirm) == "N") :
                    a = "KELUAR"
                    lanjut = True
                else :
                    print("Pilihan tidak tersedia, pilih kembali!")
                    confirm = input("Apakah mau melakukan hal lain? (Y/N) : ").upper()
        elif (int(a) == 2) :
            print("Memulai pembuatan monster baru..")
            nama = input("Masukkan Type / Nama : ")
            while (not((cekar(nama , arr1)) and (ceknama(nama)) and (ceklen(nama)))) :
                if (not(cekar(nama , arr1))) :
                    print("Nama sudah terdaftar, coba lagi!")
                elif (not(ceknama(nama))) :
                    print("Masukkan input bertipe string, coba lagi!")
                elif ((not(ceklen(nama))) and (cekar(nama , arr1)) and (ceknama(nama))) :
                    print("Masukkan input harus bernilai, coba lagi!")
                nama = input("Masukkan Type / Nama : ")
            atk = input("Masukkan ATK Power : ")
            while (not((cekint(atk)) and (ceklen(atk)))) :
                if (not(cekint(atk))) :
                    print("Masukkan input bertipe integer dan bernilai positif, coba lagi!")
                elif (not(ceklen(atk))) :
                    print("Masukkan input harus bernilai, coba lagi!")
                atk = input("Masukkan ATK Power : ")
            deff = input("Masukkan DEF Power : ")
            while (not((cekdef(deff)) and (ceklen(deff)) and (cekint(deff)))) :
                if (not(ceklen(deff))) :
                    print("Masukkan input harus bernilai, coba lagi!") 
                elif ((not(cekdef(deff))) and (cekint(deff))) :
                    print("DEF Power harus bernilai 0-50, coba lagi!")
                elif (not(cekint(deff))) :
                    print("Masukkan bertipe integer dan bernilai positif, coba lagi!")
                deff = input("Masukkan DEF Power : ")
            hp = input("Masukkan HP : ")
            while ((not(cekint(hp)) and (ceklen(hp)))) :
                if (not(ceklen(hp))) :
                    print("Masukkan input harus bernilai, coba lagi!")
                elif (not(cekint(hp))) :
                    print("Masukkan input bertipe integer dan bernilai positif, coba lagi!")
                hp = input("Masukkan HP : ")
            print("Monster baru berhasil dibuat!")
            print("Type :" , nama)
            print("ATK Power :" , atk)
            print("DEF Power :" , deff)
            print("HP :" , hp)
            k = input("Tambahkan Monster ke database (Y/N) : ").upper()
            tambah = False
            while (not(tambah)) :
                if (str(k) == "Y") :
                    h = arr1[len(arr1) - 1][0]
                    MonsterBaru = [str(int(h) + 1) , nama , atk , deff , hp]
                    arr1 = arr1 + [MonsterBaru]
                    tambah = True
                    print("Monster baru telah ditambahkan!")
                elif (str(k) == "N") :
                    tambah = True 
                    print("Monster gagal ditambahkan!")
                else :
                    print("Pilihan tidak tersedia, pilih kembali!")
                    k = input("Tambahkan Monster ke database (Y/N) : ").upper()
            lanjut = False
            confirm = input("Apakah mau melakukan hal lain? (Y/N) : ").upper()
            while (not(lanjut)) :
                if (str(confirm) == "Y") :
                    a = input("Pilih aksi : ")
                    lanjut = True
                elif (str(confirm) == "N") :
                    a = "KELUAR"
                    lanjut = True
                else :
                    print("Pilihan tidak tersedia, pilih kembali!")
                    confirm = input("Apakah mau melakukan hal lain? (Y/N) : ").upper()
    print(",---.     .--.   ,---.      .--.      ▄▀▀▄ ▄▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▀▄  ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄               ,---.    .-. .-.   ,--,   .-. .-.   ,--,     .--.    ,---.   ,-. .-.   .--.    .-. .-.   ")
    print(" | .-.\   / /\ \  | .-.\    / /\ \    █  █ ▀  █ █      █ █  █ █ █ █ █   ▐ █    █  ▐ ▐  ▄▀   ▐ █   █   █    |\    /|  | .-'    |  \| | .' .'    | | | | .' .')    / /\ \   | .-.\  | |/ /   / /\ \   |  \| |   ")
    print(" | |-' ) / /__\ \ | `-'/   / /__\ \   ▐  █    █ █      █ ▐  █  ▀█    ▀▄   ▐   █       █▄▄▄▄▄  ▐  █▀▀█▀     |(\  / |  | `-.    |   | | |  |  __ | | | | |  |(_)  / /__\ \  | |-' ) | | /   / /__\ \  |   | |   ")
    print(" | |--'  |  __  | |   (    |  __  |      █    █  ▀▄    ▄▀   █   █  ▀▄   █     █        █    ▌   ▄▀    █    (_)\/  |  | .-'    | |\  | \  \ ( _)| | | | \  \     |  __  |  | |--'  | | \   |  __  |  | |\  |   ")
    print(" | |     | |  |)| | |\ \   | |  |)|    ▄▀   ▄▀     ▀▀▀▀   ▄▀   █    █▀▀▀    ▄▀        ▄▀▄▄▄▄   █     █     | \  / |  |  `--.  | | |)|  \  `-) )| `-')|  \  `-.  | |  |)|  | |     | |) \  | |  |)|  | | |)|   ")
    print(" /(      |_|  (_) |_| \)\  |_|  (_)   █    █             █    ▐    ▐      █          █    ▐   ▐     ▐      | |\/| |  /( __.'  /(  (_)  )\____/ `---(_)   \____\ |_|  (_)  /(      |((_)-' |_|  (_)  /(  (_)   ")
    print("(__)                  (__)            ▐    ▐             ▐                ▐          ▐                     '-'  '-' (__)     (__)     (__)                               (__)     (_)              (__)       ")
    print("                     ░██████╗ ███████╗ ██╗░░░░░ ░█████╗░ ███╗░░░███╗ ░█████╗░ ████████╗   ████████╗ ██╗ ███╗░░██╗ ░██████╗░ ░██████╗░ ░█████╗░ ██╗░░░░░                                                       ")
    print("                     ██╔════╝ ██╔════╝ ██║░░░░░ ██╔══██╗ ████╗░████║ ██╔══██╗ ╚══██╔══╝   ╚══██╔══╝ ██║ ████╗░██║ ██╔════╝░ ██╔════╝░ ██╔══██╗ ██║░░░░░                                                       ")
    print("                     ╚█████╗░ █████╗░░ ██║░░░░░ ███████║ ██╔████╔██║ ███████║ ░░░██║░░░   ░░░██║░░░ ██║ ██╔██╗██║ ██║░░██╗░ ██║░░██╗░ ███████║ ██║░░░░░                                                       ")
    print("                     ░╚═══██╗ ██╔══╝░░ ██║░░░░░ ██╔══██║ ██║╚██╔╝██║ ██╔══██║ ░░░██║░░░   ░░░██║░░░ ██║ ██║╚████║ ██║░░╚██╗ ██║░░╚██╗ ██╔══██║ ██║░░░░░                                                       ")
    print("                     ██████╔╝ ███████╗ ███████╗ ██║░░██║ ██║░╚═╝░██║ ██║░░██║ ░░░██║░░░   ░░░██║░░░ ██║ ██║░╚███║ ╚██████╔╝ ╚██████╔╝ ██║░░██║ ███████╗                                                       ")
    print("                     ╚═════╝░ ╚══════╝ ╚══════╝ ╚═╝░░╚═╝ ╚═╝░░░░░╚═╝ ╚═╝░░╚═╝ ░░░╚═╝░░░   ░░░╚═╝░░░ ╚═╝ ╚═╝░░╚══╝ ░╚═════╝░ ░╚═════╝░ ╚═╝░░╚═╝ ╚══════╝                                                       ")
    return (arr1)