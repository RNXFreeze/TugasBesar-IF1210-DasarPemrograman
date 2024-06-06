# PROGRAM K05-C-F11

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : laboratory.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F11 - Laboratory
# Penanggung Jawab F07 : 16523135 / Aleta Edna Jessalyn

# KAMUS
# laboratory : function

# ALGORITMA
def laboratory(monster , monster_inventory , oc_user , id_user) :
    # SPESIFIKASI LOKAL
    # Melakukan proses upgrade level monster yang dimiliki sesuai spesifikasi.
    # I.S. Data monster, monster_inventory, oc_user, dan id_user telah terdefinisi di awal.
    # F.S. Data monster_inventory dan oc_user yang baru telah disimpan setelah proses laboratorium dilakukan.

    # KAMUS LOKAL
    # monster , monster_inventory : matrix of data
    # id_user , oc_user , idmon , no_monster , current_level , next_level : integer
    # konfirm , nama_monster : string
    # list_monster : array of string
    # upgrade_cost : array of integer
    # j , k : integer (index)

    # ALGORITMA LOKAL
    print("            Selamat Datang Di Laboratorium Dokter Asep             ")
    print("                                                                   ")
    print("                                           ##.                     ")
    print("                                                     #             ")
    print("                                            ###    ####            ")
    print("                                          #-..-#    ##             ")
    print("                                          #--.-#                   ")
    print("                                  #####     -##                    ")
    print("                                    ########                       ")
    print("                                   ###    ######                   ")
    print("                                  ###         #####-               ")
    print("                                  ##      .  ###                   ")
    print("                                 ###    #   ###                    ")
    print("                                ###        +##                     ")
    print("                             ####  ##      ##                      ")
    print("                           ####      -  ####-                      ")
    print("                        ####       ####   ##+                      ")
    print("                      ######               ##                      ")
    print("                    ####                 ####                      ")
    print("                  ###  ## -+#              ##                      ")
    print("                ###       ..-+#          + +##                     ")
    print("                ##   .........-+##      #- ###                     ")
    print("                ##   ............-+####+-   ##                     ")
    print("                 ###    ..................####                     ")
    print("                  #####     .............   ###                    ")
    print("                     ######      .......... +##                    ")
    print("                         ######       ....  +##                    ")
    print("                              ######        ##                     ")
    print("                                 ############                      ")
    oc_user = int(oc_user)
    while (True) :
        print(f"OC yang anda miliki : {oc_user}")
        print(f"============ Monster List ============")
        list_monster = []
        for j in range (len(monster_inventory)) :
            if (monster_inventory[j][0] == id_user) :
                idmon = monster_inventory[j][1]
                for k in range (len(monster)) :
                    if (monster[k][0] == idmon) :
                        print(f"{len(list_monster) + 1}. {monster[k][1]} (Level: {monster_inventory[j][2]})")
                        list_monster.append([len(list_monster) + 1 , monster[k][1] , monster_inventory[j][2] , j])
        print(f"=========== UPGRADE PRICE ===========")
        print("1. Level 1 -> Level 2: 300 OC")
        print("2. Level 2 -> Level 3: 500 OC")
        print("3. Level 3 -> Level 4: 800 OC")
        print("4. Level 4 -> Level 5: 1000 OC")
        while (True) :
            no_monster = int(input(">>> Pilih Nomor Monster yang akan di Upgrade (0 untuk keluar) : "))
            if (no_monster == 0) :
                print("Terima kasih telah menggunakan Lab Dokter Asep!")
                return (monster_inventory , oc_user)
            elif (1 <= no_monster <= len(list_monster)) :
                break
            else :
                print("Pilihan Monster tidak valid!")
        current_level = int(list_monster[no_monster - 1][2])
        next_level = current_level + 1
        upgrade_cost = [300 , 500 , 800 , 1000 , 0][next_level - 2]
        nama_monster = list_monster[no_monster - 1][1]
        if (current_level > 4) :
            print("Maaf, monster yang Anda pilih sudah memiliki level maksimum.")
        else :
            print(f"\n{nama_monster} akan di-upgrade ke level {next_level}.")
            print(f"Harga untuk melakukan upgrade {nama_monster} adalah {upgrade_cost} OC.")
            while (True) :
                konfirm = input(f"\n>>> Lanjutkan upgrade (Y/N) : ")
                if (konfirm.upper() == "Y") :
                    if (oc_user >= upgrade_cost) :
                        print(f"Selamat, {nama_monster} berhasil di-upgrade ke level {next_level}!")
                        list_monster[no_monster - 1][2] = next_level
                        oc_user = oc_user - upgrade_cost
                        print(f"O.W.C.A Coin anda sekarang: {oc_user}")
                        print(f"Level {nama_monster} sekarang: {list_monster[no_monster - 1][2]}")
                        monster_inventory[list_monster[no_monster - 1][3]][2] = next_level
                    else :
                        print("O.W.C.A Coin Anda tidak cukup.")
                    break
                elif (konfirm.upper() == 'N') :
                    print("Upgrade dibatalkan.")
                    break
                else :
                    print("Masukkan pilihan yang valid!")