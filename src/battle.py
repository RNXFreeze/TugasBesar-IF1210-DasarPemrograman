# PROGRAM K05-C-F08

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : battle.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F08 - Battle
# Penanggung Jawab F08 : 19623215 / Muhammad Raihan Nazhim Oktana

# KAMUS
# show_enemy , show_team_monster : procedure
# battle , generate , cint , cstr : function

# ALGORITMA
import time
from src.rng import generate
def show_enemy() :
    # SPESIFIKASI LOKAL
    # Melakukan print gambar monster musuh yang akan dilawan.

    # KAMUS LOKAL
    # -

    # ALGORITMA LOKAL
    print("")
    print("        _/\----/\   ")
    print("       /         \     /\ ")
    print("      |  O    O   |   |  |")
    print("      |  .vvvvv.  |   |  |")
    print("      /  |     |   \  |  |")
    print("     /   `^^^^^'    \ |  |")
    print("   ./  /|            \|  |_")
    print("  /   / |         |\__     /")
    print("  \  /  |         |   |__|")
    print("   `'   |  _      |")
    print("     _.-'-' `-'-'.'_")
    print("__.-'               '-.__")
    return()

def show_team_monster() :
    # SPESIFIKASI LOKAL
    # Melakukan print gambar monster yang digunakan.

    # KAMUS LOKAL
    # -

    # ALGORITMA LOKAL
    print("")
    print("      /\----/\_   ")
    print("     /         \   /|")
    print("    |  | O    O | / |")
    print("    |  | .vvvvv.|/  /")
    print("   /   | |     |   /")
    print("  /    | `^^^^^   /")
    print(" | /|  |         /")
    print("  / |    ___    |")
    print("     \  |   |   |")
    print("     |  |   |   |")
    print("      \._\   \._\ ")
    return()

def cint(data) :
    # SPESIFIKASI LOKAL
    # Mengubah data yang berupa string of integer menjadi integer.

    # KAMUS LOKAL
    # data : matrix of data
    # num_char : list of character
    # i , j : integer (index)

    # ALGORITMA LOKAL
    num_char = '0123456789'
    for i in range (1 , len(data)) :
        for j in range (len(data[i])) :
            if ((data[i][j][0]) in (num_char)) :
                data[i][j] = int(data[i][j])
            elif (data[i][j][0] == '-') :
                if ((data[i][j][1]) in (num_char)) :
                    data[i][j] = int(data[i][j])
    return (data)

def cstr(data) :
    # SPESIFIKASI LOKAL
    # Mengubah data yang berupa anything menjadi string.

    # KAMUS LOKAL
    # data : matrix of data
    # i , j : integer (index)

    # ALGORITMA LOKAL
    for i in range (1 , len(data)) :
        for j in range (len(data[i])) :
            data[i][j] = str(data[i][j])
    return (data)

def battle(uid , username , role , oc , monster , inv_item , inv_monster) :
    # SPESIFIKASI LOKAL
    # Melakukan algoritma battle sesuai spesifikasi yang telah dibuat.

    # KAMUS LOKAL
    # show_enemy , show_team_monster : procedure
    # generate , cint , cstr : function
    # user , monster , inv_item , inv_monster : matrix of data
    # username , role : string
    # uid , oc , get_oc , num , turn , m : integer
    # level_enemy , level_monster , choice , monster_choice , perintah , pilih : integer
    # temp_atk_enemy , temp_def_enemy , temp_hp_enemy , last_hp_enemy : integer
    # temp_atk_monster , temp_def_monster , temp_hp_monster , leave_atk_monster, leave_def_monster , leave_hp_monster , start_hp_monster , last_hp_monster , random_atk_monster , random_atk_enemy : integer
    # true_choice : array of character
    # choice_option : matrix of integer
    # qty_s , qty_r , qty_h : tuple of integer
    # minum_s , minum_r , minum_h , minum_round , fight , run , check_potion , cek : boolean
    # i : integer (index)

    # ALGORITMA LOKAL
    print(">>> BATTLE")
    print("")
    print("________      ________      _________    _________    ___           _______        ")
    print("|\   __  \    |\   __  \    |\___   ___\ |\___   ___\ |\  \         |\  ___ \      ")
    print("\ \  \|\ /_   \ \  \|\  \   \|___ \  \_| \|___ \  \_| \ \  \        \ \   __/|     ")
    print(" \ \   __  \   \ \   __  \       \ \  \       \ \  \   \ \  \        \ \  \_|/__   ")
    print("  \ \  \|\  \   \ \  \ \  \       \ \  \       \ \  \   \ \  \____    \ \  \_|\ \  ")
    print("   \ \_______\   \ \__\ \__\       \ \__\       \ \__\   \ \_______\   \ \_______\ ")
    print("    \|_______|    \|__|\|__|        \|__|        \|__|    \|_______|    \|_______| ")
    start_time = time.time()
    print("")
    uid = int(uid)
    oc = int(oc)
    monster = cint(monster)
    inv_item = cint(inv_item)
    inv_monster = cint(inv_monster)
    show_enemy()
    time.sleep(1)
    num = generate([1 , len(monster)])
    level_enemy = generate([1 , 6])
    temp_atk_enemy = int(monster[num][2] * (1 + (level_enemy - 1) * 0.1))
    temp_def_enemy = int(monster[num][3] * (1 + (level_enemy - 1) * 0.1))
    temp_hp_enemy = int(monster[num][4] * (1 + (level_enemy - 1) * 0.1))
    print(f"RAWRRR, Monster {monster[num][1]} telah muncul !!!")
    print(f"Name\t\t: {monster[num][1]}\nATK Power\t: {monster[num][2]} --> {temp_atk_enemy} \nDEF Power\t: {monster[num][3]} --> {temp_def_enemy}\nHP\t\t: {monster[num][4]} --> {temp_hp_enemy}\nLevel\t\t: {level_enemy}\n")
    time.sleep(1)
    print("============ MONSTER LIST ============")
    m = 1
    choice_option = []
    for i in range (1 , len(inv_monster)) :
        if (uid == inv_monster[i][0]) :
            print(f"{m}. {monster[inv_monster[i][1]][1]}")
            choice_option.append([m - 1 , i , inv_monster[i][1]])
            m = m + 1
    true_choice = [str(i) for i in range (1 , m)]
    choice = str(input("Pilih monster untuk bertarung (masukkan angka saja) : "))
    while (not((choice) in (true_choice))) :
        print("Pilihan nomor tidak tersedia!")
        choice = str(input("Pilih monster untuk bertarung (masukkan angka saja) : "))
    choice = int(choice)
    monster_choice = choice_option[choice - 1][1]
    level_monster = inv_monster[monster_choice][2]
    temp_atk_monster = int(monster[inv_monster[monster_choice][1]][2] * (1 + (level_monster - 1) * 0.1))
    temp_def_monster = int(monster[inv_monster[monster_choice][1]][3] * (1 + (level_monster - 1) * 0.1))
    temp_hp_monster = int(monster[inv_monster[monster_choice][1]][4] * (1 + (level_monster - 1) * 0.1))
    start_hp_monster = temp_hp_monster
    time.sleep(1)
    show_team_monster()
    time.sleep(1)
    print(f"\nRAWRRR, {role} {username} mengeluarkan monster {monster[inv_monster[monster_choice][1]][1]} !!!")
    print(f"Name\t\t: {monster[inv_monster[monster_choice][1]][1]}\nATK Power\t: {monster[inv_monster[monster_choice][1]][2]} --> {temp_atk_monster}\nDEF Power\t: {monster[inv_monster[monster_choice][1]][3]} --> {temp_def_monster}\nHP\t\t: {monster[inv_monster[monster_choice][1]][4]} --> {temp_hp_monster}\nLevel\t\t: {level_monster}")
    turn = 1
    minum_s = False
    minum_r = False
    minum_h = False
    while ((temp_hp_monster != 0) and (temp_hp_enemy != 0)) :
        time.sleep(1)
        print(f"\n============ TURN {turn} ({monster[inv_monster[monster_choice][1]][1]}) ============")
        print("1. Attack\n2. Use Potion\n3. Quit")
        perintah = str(input("Pilih perintah (masukkan angka saja) : "))
        while ((perintah != '1') and (perintah != '2') and (perintah != '3')) :
            print("Perintah tidak ditemukan.")
            perintah = str(input("Pilih perintah (masukkan angka saja) : "))
        perintah = int(perintah)
        fight = False
        minum_round = False
        run = False
        while (perintah != 3) and (not(fight)) :
            while (perintah == 2) :
                cek = False
                check_potion = False
                for i in range (1 , len(inv_item)) :
                    if ((inv_item[i][0] == uid) and (inv_item[i][2] != 0) and ((inv_item[i][1] == "strength") or (inv_item[i][1] == "resilience") or (inv_item[i][1] == "healing"))) :
                        cek = True
                        break
                if not(cek) :
                    print("Anda tidak memiliki Potion dalam inventory.")
                else :
                    print("\n============ POTION LIST ============")
                    qty_s = (0 , 0)
                    qty_r = (0 , 0)
                    qty_h = (0 , 0)
                    for i in range (1 , len(inv_item)) :
                        if ((inv_item[i][0] == uid) and (inv_item[i][1] == "strength")) :
                            qty_s = (i , inv_item[i][2])
                        elif ((inv_item[i][0] == uid) and (inv_item[i][1] == "resilience")) :
                            qty_r = (i , inv_item[i][2])
                        elif ((inv_item[i][0] == uid) and (inv_item[i][1] == "healing")) :
                            qty_h = (i , inv_item[i][2])
                    time.sleep(1)
                    print(f"1. Strength Potion (Qty: {qty_s[1]}) - Increases ATK Power")
                    print(f"2. Resilience Potion (Qty: {qty_r[1]}) - Increases DEF Power")
                    print(f"3. Healing Potion (Qty: {qty_h[1]}) - Restores Health")
                    print(f"4. Cancel")
                    pilih = str(input("Pilih perintah (masukkan angka saja) : "))
                    while ((pilih != '1') and (pilih != '2') and (pilih != '3') and (pilih != '4')) :
                        print("Perintah tidak ditemukan.")
                        pilih = str(input("Pilih perintah (masukkan angka saja) : "))
                    pilih = int(pilih)
                    while (not(check_potion)) :
                        if (pilih == 1) :
                            if (qty_s[1] == 0) :
                                print("Wah, kamu sedang tidak memiliki ramuan ini, silakan pilih ramuan lain!\n")
                            elif (qty_s[1] != 0) and (minum_s) :
                                print(f"Kamu mencoba memberikan ramuan ini kepada {monster[inv_monster[monster_choice][1]][1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n")
                            else :
                                inv_item[qty_s[0]][2] = inv_item[qty_s[0]][2] - 1
                                qty_s = (qty_s[0] , inv_item[qty_s[0]][2])
                                check_potion = True
                                minum_round = True
                                minum_s = True
                                leave_atk_monster = temp_atk_monster
                                temp_atk_monster = int(temp_atk_monster * 1.05)
                                print(f"\nSetelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {monster[inv_monster[monster_choice][1]][1]} dan gerakannya menjadi lebih cepat dan mematikan.")
                                print(f"Update ATK Power : {leave_atk_monster} --> {temp_atk_monster}\n")
                                time.sleep(1)
                        elif (pilih == 2) :
                            if (qty_r[1] == 0) :
                                print("Wah, kamu sedang tidak memiliki ramuan ini, silakan pilih ramuan lain!\n")
                            elif (qty_r[1] != 0) and (minum_r) :
                                print(f"Kamu mencoba memberikan ramuan ini kepada {monster[inv_monster[monster_choice][1]][1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n")
                            else :
                                inv_item[qty_r[0]][2] = inv_item[qty_r[0]][2] - 1
                                qty_r = (qty_r[0] , inv_item[qty_r[0]][2])
                                check_potion = True
                                minum_round = True
                                minum_r = True
                                leave_def_monster = temp_def_monster
                                temp_def_monster = int(temp_def_monster * 1.05)
                                print(f"\nSetelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {monster[inv_monster[monster_choice][1]][1]} yang membuatnya terlihat semakin tangguh dan sulit dilukai.")
                                print(f"Update DEF Power : {leave_def_monster} --> {temp_def_monster}\n")
                                time.sleep(1)
                        elif (pilih == 3) :
                            if (qty_h[1] == 0) :
                                print("Wah, kamu sedang tidak memiliki ramuan ini, silakan pilih ramuan lain!\n")
                            elif (qty_h[1] != 0) and (minum_h) :
                                print(f"Kamu mencoba memberikan ramuan ini kepada {monster[inv_monster[monster_choice][1]][1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n")
                            else :
                                inv_item[qty_h[0]][2] = inv_item[qty_h[0]][2] - 1
                                qty_h = (qty_h[0] , inv_item[qty_h[0]][2])
                                check_potion = True
                                minum_round = True
                                minum_h = True
                                leave_hp_monster = temp_hp_monster
                                temp_hp_monster = int(temp_hp_monster + monster[inv_monster[monster_choice][1]][4] * 1/4)
                                if (temp_hp_monster > start_hp_monster) :
                                    temp_hp_monster = start_hp_monster
                                print(f"\nSetelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {monster[inv_monster[monster_choice][1]][1]} sembuh dengan cepat.\nDalam sekejap, {monster[inv_monster[monster_choice][1]][1]} terlihat kembali prima dan siap melanjutkan pertempuran.")
                                print(f"Update HP : {leave_hp_monster} --> {temp_hp_monster}\n")
                                time.sleep(1)
                        else :
                            print("")
                            break
                        if not(check_potion) :
                            time.sleep(1)
                            print("============ POTION LIST ============")
                            print(f"1. Strength Potion (Qty: {qty_s[1]}) - Increases ATK Power")
                            print(f"2. Resilience Potion (Qty: {qty_r[1]}) - Increases DEF Power")
                            print(f"3. Healing Potion (Qty: {qty_h[1]}) - Restores Health")
                            print("4. Cancel")
                            pilih = str(input("Pilih perintah (masukkan angka saja) : "))
                            while ((pilih != '1') and (pilih != '2') and (pilih != '3') and (pilih != '4')) :
                                print("Perintah tidak ditemukan.")
                                pilih = str(input("Pilih perintah (masukkan angka saja) : "))
                            pilih = int(pilih)
                if (check_potion) :
                    perintah = 1
                else :
                    time.sleep(1)
                    print(f"============ TURN {turn} ({monster[inv_monster[monster_choice][1]][1]}) ============")
                    print("1. Attack\n2. Use Potion\n3. Quit")
                    perintah = str(input("Pilih perintah (masukkan angka saja) : "))
                    while ((perintah != '1') and (perintah != '2') and (perintah != '3')) :
                        print("Perintah tidak ditemukan.")
                        perintah = str(input("Pilih perintah (masukkan angka saja) : "))
                    perintah = int(perintah)
            if (perintah == 1) :
                fight = True
                if (minum_round) :
                    print(f"============ TURN {turn} ({monster[num][1]}) ============")
                    last_hp_monster = temp_hp_monster
                    random_atk_enemy = int(temp_atk_enemy * (100 + generate([-30 , 31]))/100)
                    temp_hp_monster = int(temp_hp_monster - (random_atk_enemy * (100 - temp_def_monster)/100))
                    if (temp_hp_monster <= 0) :
                        temp_hp_monster = 0
                    print(f"SCHWINKKK, {monster[num][1]} menyerang {monster[inv_monster[monster_choice][1]][1]} !!!")
                    print(f"Name\t\t: {monster[inv_monster[monster_choice][1]][1]}\nATK Power\t: {temp_atk_monster}\nDEF Power\t: {temp_def_monster}\nHP\t\t: {last_hp_monster} --> {temp_hp_monster}\nLevel\t\t: {level_monster}")
                    print(f"#Penjelasan Battle - ATT : Attack = {random_atk_enemy} ; Reduced by = {random_atk_enemy * (temp_def_monster)/100} ({temp_def_monster}%) ; Attack Results = {random_atk_enemy * (100 - temp_def_monster)/100}")
                    print(f"#Penjelasan Battle - HP : Attack Results = {random_atk_enemy * (100 - temp_def_monster)/100} ; Last HP = {last_hp_monster} ; Final HP = FLOOR({last_hp_monster} - {random_atk_enemy * (100 - temp_def_monster)/100}) = {temp_hp_monster}")
                    time.sleep(1)
                    if (temp_hp_monster == 0) :
                        break
                else :
                    time.sleep(1)
                    last_hp_enemy = temp_hp_enemy
                    random_atk_monster = int(temp_atk_monster * (100 + generate([-30 , 31]))/100)
                    temp_hp_enemy = int(temp_hp_enemy - (random_atk_monster * (100 - temp_def_enemy)/100))
                    if (temp_hp_enemy <= 0) :
                        temp_hp_enemy = 0
                    print(f"\nSCHWINKKK, {monster[inv_monster[monster_choice][1]][1]} menyerang {monster[num][1]} !!!")
                    print(f"Name\t\t: {monster[num][1]}\nATK Power\t: {temp_atk_enemy}\nDEF Power\t: {temp_def_enemy}\nHP\t\t: {last_hp_enemy} --> {temp_hp_enemy}\nLevel\t\t: {level_enemy}")
                    print(f"#Penjelasan Battle - ATT : Attack = {random_atk_monster} ; Reduced by = {random_atk_monster * (temp_def_enemy)/100} ({temp_def_enemy}%) ; Attack Results = {random_atk_monster * (100 - temp_def_enemy)/100}")
                    print(f"#Penjelasan Battle - HP : Attack Results = {random_atk_monster * (100 - temp_def_enemy)/100} ; Last HP = {last_hp_enemy} ; Final HP = FLOOR({last_hp_enemy} - {random_atk_monster * (100 - temp_def_enemy)/100}) = {temp_hp_enemy}\n")
                    time.sleep(1)
                    if (temp_hp_enemy == 0) :
                        break
                    else :
                        print(f"============ TURN {turn} ({monster[num][1]}) ============")
                        last_hp_monster = temp_hp_monster
                        random_atk_enemy = int(temp_atk_enemy * (100 + generate([-30 , 31]))/100)
                        temp_hp_monster = int(temp_hp_monster - (random_atk_enemy * (100 - temp_def_monster)/100))
                        if (temp_hp_monster <= 0) :
                            temp_hp_monster = 0
                        print(f"SCHWINKKK, {monster[num][1]} menyerang {monster[inv_monster[monster_choice][1]][1]} !!!")
                        print(f"Name\t\t: {monster[inv_monster[monster_choice][1]][1]}\nATK Power\t: {temp_atk_monster}\nDEF Power\t: {temp_def_monster}\nHP\t\t: {last_hp_monster} --> {temp_hp_monster}\nLevel\t\t: {level_monster}")
                        print(f"#Penjelasan Battle - ATT : Attack = {random_atk_enemy} ; Reduced by = {random_atk_enemy * (temp_def_monster)/100} ({temp_def_monster}%) ; Attack Results = {random_atk_enemy * (100 - temp_def_monster)/100}")
                        print(f"#Penjelasan Battle - HP : Attack Results = {random_atk_enemy * (100 - temp_def_monster)/100} ; Last HP = {last_hp_monster} ; Final HP = FLOOR({last_hp_monster} - {random_atk_enemy * (100 - temp_def_monster)/100}) = {temp_hp_monster}")
                        time.sleep(1)
                        if (temp_hp_monster == 0) :
                            break
            elif (perintah != 3) :
                print("Perintah tidak ditemukan.")
                perintah = str(input("Pilih perintah (masukkan angka saja) : "))
                while ((perintah != '1') and (perintah != '2') and (perintah != '3')) :
                    print("Perintah tidak ditemukan.")
                    perintah = str(input("Pilih perintah (masukkan angka saja) : "))
                perintah = int(perintah)
        if (perintah == 3) :
            run = True
            print("Anda berhasil kabur dari BATTLE")
            break
        else :
            turn = turn + 1
    if ((temp_hp_enemy == 0) and (not(run))) :
        time.sleep(1)
        print(f"Selamat, Anda berhasil mengalahkan monster {monster[num][1]} !!!")
        get_oc = generate([5 , 31])
        oc = oc + get_oc
        print(f"Total OC yang diperoleh : {get_oc}")
    elif ((temp_hp_monster == 0) and (not(run))) :
        time.sleep(1)
        print(f"\nYahhh, Anda dikalahkan monster {monster[num][1]}. Jangan menyerah, coba lagi !!!")
    uid = str(uid)
    oc = str(oc)
    monster = cstr(monster)
    inv_item = cstr(inv_item)
    inv_monster = cstr(inv_monster)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Durasi Permainan\t: {int(duration // 3600)} Jam {int((duration % 3600) // 60)} Menit {int((duration % 60 // 1))} Detik")
    return (uid , username , role , oc , monster , inv_item , inv_monster)
