# PROGRAM K05-C-F07

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : inventory.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F07 - Inventory
# Penanggung Jawab F07 : 16523135 / Aleta Edna Jessalyn

# KAMUS
# cekint , inventory : procedure

# ALGORITMA
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
    i = 0
    while (i < len(cekinte)) :
        if (not(48 <= cekinte[i] <= 57)) :
            f = False
        i = i + 1
    return (f)

def inventory(username, listinvmonster, listuser, listmonster, listinvent):
    # SPESIFIKASI LOKAL
    # Menampilkan data inventory milik seorang pengguna.
    # I.S. Data username, user, monster, inv_item, dan inv_monster telah terdefinisi.
    # F.S. Data inventory milik pengguna dengan username tersebut tampak di layar.

    # KAMUS LOKAL
    # listuser , listmonster , listinvent , listinvmonster : matrix of data
    # array_tumbal2 , array_tumbal3 , array_tumbal4 : array of data
    # username , ids : string
    # id , oc , a , idmon : integer
    # keluar : boolean
    # i , j , k , l , m , n , o : integer (index)

    # ALGORITMA LOKAL
    for i in range (len(listuser)) :
        if (listuser[i][1] == username) :
            id = listuser[i][0]
            break
    print(f"============ INVENTORY LIST (User ID: {listuser[i][0]}) ============")
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {listuser[i][4]}.")
    a = 0
    array_tumbal2 = []
    array_tumbal3 = []
    array_tumbal4 = []
    for j in range (len(listinvmonster)) :
        if (listinvmonster[j][0] == id) :
            idmon = listinvmonster[j][1]
            for k in range (len(listmonster)) :
                if (listmonster[k][0] == idmon) :
                    print(f"{a + 1}. Monster       " , end = "")
                    print(f"(Name: {listmonster[k][1]}, Lvl: {listinvmonster[j][2]}, HP: {listmonster[k][4]})")
                    a = a + 1
                    array_tumbal2.append([a , "Monster" , listmonster[k][1] , listmonster[k][2] , listmonster[k][3] , listmonster[k][4] , listinvmonster[j][2]])
    for l in range (len(listinvent)) :
        if ((listinvent[l][0] == id) and (listinvent[l][1] != "monster_ball")) :
            print(f"{a + 1}. Potion        " , end = "")
            print(f"(Type: {listinvent[l][1]}, Qty: {listinvent[l][2]})")
            a = a + 1
            array_tumbal3.append([a , "Potion" , listinvent[l][1] , listinvent[l][2]])
        elif ((listinvent[l][0] == id) and (listinvent[l][1] == "monster_ball")) :
            print(f"{a + 1}. Monster Ball  " , end = "")
            print(f"(Qty: {listinvent[l][2]})")
            a = a + 1
            array_tumbal4.append([a , "Monster Ball" , listinvent[l][2]])
    keluar = False
    while (keluar == False) :
        print("Ketikkan id untuk menampilkan detail item : ")
        ids = input()
        if (ids != "KELUAR") :
            if (len(ids) == 0) :
                print("Pastikan id harus terisi!")
            elif (not(cekint(str(ids)))) :
                print("Pilihan id tidak tersedia!")
                print('Ketik "KELUAR" untuk keluar dari inventory.')
            elif (int(ids) > a) :
                print("Pilihan id tidak tersedia!")
            elif (cekint(str(ids))) :
                for m in range (len(array_tumbal2)) :
                    if (int(ids) == array_tumbal2[m][0]) :
                        print(array_tumbal2[m][1])
                        print(f"Name      : {array_tumbal2[m][2]}")
                        print(f"ATK Power : {array_tumbal2[m][3]}")
                        print(f"DEF Power : {array_tumbal2[m][4]}")
                        print(f"HP        : {array_tumbal2[m][5]}")
                        print(f"Level     : {array_tumbal2[m][6]}")
                        break
                for n in range (len(array_tumbal3)) :
                    if (int(ids) == array_tumbal3[n][0]) :
                        print(array_tumbal3[n][1])
                        print(f"Type      : {array_tumbal3[n][2]}")
                        print(f"Quantity  : {array_tumbal3[n][3]}")
                        break
                for o in range (len(array_tumbal4)) :
                    if (int(ids) == array_tumbal4[o][0]) :
                        print(array_tumbal4[o][1])
                        print(f"Quantity  : {array_tumbal4[o][2]}")
                        break
        else :
            keluar = True
    return()
