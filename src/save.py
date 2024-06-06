# PROGRAM K05-C-F15

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : save.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F15 - Save
# Penanggung Jawab F15 - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# Penanggung Jawab F15 - 2 : 19623065 / Muhammad Alfansya

# KAMUS
# cmap , cjoin , save : procedure

# ALGORITMA
import os , time
def cmap(function , map_data) :
    # SPESIFIKASI LOKAL
    # Membuat fungsi personal yang serupa dengan fungsi map() pada python.

    # KAMUS LOKAL
    # function : function
    # map_data : data
    # map_result : array / list of map_data
    # i : integer (index)

    # ALGORITMA LOKAL
    map_result = []
    for (i) in (map_data) :
        map_result.append(function(i))
    return (map_result)

def cjoin(separator , join_data) :
    # SPESIFIKASI LOKAL
    # Membuat fungsi personal yang serupa dengan fungsi join() pada python.

    # KAMUS LOKAL
    # separator : character
    # join_data , item : data
    # join_result : string
    # i : integer (index)

    # ALGORITMA LOKAL
    join_result = ""
    for (i , item) in enumerate(join_data) :
        join_result = join_result + str(item)
        if (i < (len(join_data) - 1)) :
            join_result = join_result + separator
    return (join_result)

def save(user , monster , inv_item , inv_monster , shop_item , shop_monster) :
    # SPESIFIKASI LOKAL
    # Melakukan proses penyimpanan data dari array sementara yang telah dipakai selama program berjalan.
    # I.S. Data user, monster, inv_item, inv_monster, shop_item, dan shop_monster telah terdefinisi.
    # F.S. Data user, monster, inv_item, inv_monster, shop_item, dan shop_monster telah tersimpan di suatu folder.

    # KAMUS LOKAL
    # cmap , cjoin : function
    # user , monster , inv_item , inv_monster , shop_item , shop_monster : matrix of data
    # f_user , f_monster , f_inv_item , f_inv_monster , f_shop_item , f_shop_monster : file data
    # h_user , h_monster , h_inv_item , h_inv_monster , h_shop_item , h_shop_monster : array of string
    # forbidden_character : array / list of character
    # nama , path , parent , directory : string
    # check , check_directory , end : boolean
    # roll : integer
    # i : integer (index)

    # ALGORITMA LOKAL
    print(">>> SAVE")
    time.sleep(1)
    parent = './data/'
    check_directory = False
    while (not (check_directory)) :
        check_directory = True
        check = False
        directory = str(input("Masukkan Nama Folder : "))
        forbidden_character = '/\:*?"><|'
        for i in range (len(directory)) :
            for j in (forbidden_character) :
                if (directory[i] == j) :
                    check_directory = False
                    check = True
                    print('Nama folder yang dimasukkan mengandung karakter yang dilarang yaitu (/\:*?"><|).')
                    break
            if (check) :
                break
    path = os.path.join(parent , directory)
    make = False
    if (not(os.path.exists(path))) :
        os.mkdir(path)
        make = True
    os.chdir(parent + directory)
    f_user = open("user.csv" , 'w' , newline = "")
    h_user = ["id" , "username" , "password" , "role" , "oc"]
    f_user.write(cjoin(';' , cmap(str, h_user)) + '\n')
    roll = 1
    for (i) in (user) :
        if (roll != 1) :
            f_user.write(cjoin(';' , cmap(str, i)) + '\n')
        roll = roll + 1
    f_user.close()
    f_monster = open("monster.csv" , 'w' , newline = "")
    h_monster = ["id" , "type" , "atk_power" , "def_power" , "hp"]
    f_monster.write(cjoin(';' , cmap(str, h_monster)) + '\n')
    roll = 1
    for (i) in (monster) :
        if (roll != 1) :
            f_monster.write(cjoin(';' , cmap(str, i)) + '\n')
        roll = roll + 1
    f_monster.close()
    f_inv_item = open("item_inventory.csv" , 'w' , newline = "")
    h_inv_item = ["user_id" , "type" , "quantity"]
    f_inv_item.write(cjoin(';' , cmap(str, h_inv_item)) + '\n')
    roll = 1
    for (i) in (inv_item) :
        if (roll != 1) :
            f_inv_item.write(cjoin(';' , cmap(str, i)) + '\n')
        roll = roll + 1
    f_inv_item.close()
    f_inv_monster = open("monster_inventory.csv" , 'w' , newline = "")
    h_inv_monster = ["user_id" , "monster_id" , "level"]
    f_inv_monster.write(cjoin(';' , cmap(str, h_inv_monster)) + '\n')
    roll = 1
    for (i) in (inv_monster) :
        if (roll != 1) :
            f_inv_monster.write(cjoin(';' , cmap(str, i)) + '\n')
        roll = roll + 1
    f_inv_monster.close()
    f_shop_item = open("item_shop.csv" , 'w' , newline = "")
    h_shop_item = ["type" , "stock" , "price"]
    f_shop_item.write(cjoin(';' , cmap(str, h_shop_item)) + '\n')
    roll = 1
    for (i) in (shop_item) :
        if (roll != 1) :
            f_shop_item.write(cjoin(';' , cmap(str, i)) + '\n')
        roll = roll + 1
    f_shop_item.close()
    f_shop_monster = open("monster_shop.csv" , 'w' , newline = "")
    h_shop_monster = ["monster_id" , "stock" , "price"]
    f_shop_monster.write(cjoin(';' , cmap(str, h_shop_monster)) + '\n')
    roll = 1
    for (i) in (shop_monster) :
        if (roll != 1) :
            f_shop_monster.write(cjoin(';' , cmap(str, i)) + '\n')
        roll = roll + 1
    f_shop_monster.close()
    print("Saving...") 
    if (make) :
        print(f"Membuat folder {parent + directory}...")
    time.sleep(3)
    print(f"Berhasil menyimpan data di folder {parent + directory}!")
    os.chdir('../')
    end = True
    return (end)