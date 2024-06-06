# PROGRAM K05-C-F14

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : load.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Subprogram F14 - Load
# Penanggung Jawab F14 - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# Penanggung Jawab F14 - 2 : 19623055 / Athian Nugraha Muarajuang

# KAMUS
# csplit , cstrip : function
# load : procedure

# ALGORITMA
import os , argparse
def csplit(string , delimiter) :
    # SPESIFIKASI LOKAL
    # Membuat fungsi personal yang serupa dengan fungsi split() pada python.
    
    # KAMUS LOKAL
    # result : array of string
    # string , column : string
    # delimiter : character
    # i : integer (index)
    
    # ALGORITMA
    result = []
    column = ""
    for (i) in (string) :
        if (i == delimiter) :
            result.append(column)
            column = ""
        else :
            column = column + i
    result.append(column)
    return (result)

def cstrip(string , chars = None) :
    # SPESIFIKASI LOKAL
    # Membuat fungsi personal yang serupa dengan fungsi strip() pada python.
    
    # KAMUS LOKAL
    # string , output : string
    # chars : array of character
    # start , end : integer (index)
    
    # ALGORITMA
    if (chars == None) :
        chars = ' \t\n\r\x0b\x0c'
    start = 0
    end = len(string) - 1
    while ((start <= end) and (string[start] in chars)) :
        start = start + 1
    while ((end >= start) and (string[end] in chars)) :
        end = end - 1
    output = string[start : (end + 1)]
    return (output)

def load() :
    # SPESIFIKASI LOKAL
    # Melakukan proses pengambilan data dari folder penyimpanan yang dipilih dan mengubahnya menjadi matrix of data.
    # I.S. Menerima data parser dari input yang akan dijalankan.
    # F.S. Data pada csv_directory telah tersimpan ke matrix of data.
    
    # KAMUS LOKAL
    # csplit , cstrip : function
    # parser , args : ArgumentParser
    # folder , path_folder , csv_directory , row path_user , path_monster , path_inv_item , path_inv_monster , path_shop_item , path_shop_monster : string
    # path_data : array of string
    # content : matrix of string
    # data : data
    # user , monster , inv_item , inv_monster , shop_item , shop_monster : matrix of data
    # i , j : integer (index)

    # ALGORITMA LOKAL
    parser = argparse.ArgumentParser(description = "Argument Parser")
    parser.add_argument("folder" , type = str , nargs = '?' , default = None , help = "Directory folder data CSV yang akan digunakan.")
    args = parser.parse_args()
    if (args.folder == None) :
        print("Tidak ada nama folder yang diberikan!")
        print("Usage : python main.py <nama_folder>")
        return (1 , 1 , 1 , 1 , 1 , 1)
    else :
        folder = args.folder
        path_folder = 'data/' + str(folder)
        if (not(os.path.exists(path_folder))) :
            print(f"Folder {folder} tidak ditemukan!")
            return (1 , 1 , 1 , 1 , 1 , 1)
        else :
            path_user = path_folder + '/user.csv'
            path_monster = path_folder + '/monster.csv'
            path_inv_item = path_folder + '/item_inventory.csv'
            path_inv_monster = path_folder + '/monster_inventory.csv'
            path_shop_item = path_folder + '/item_shop.csv'
            path_shop_monster = path_folder + '/monster_shop.csv'
            path_data = [path_user , path_monster , path_inv_item , path_inv_monster , path_shop_item , path_shop_monster]
            content = [[] for j in range (6)]
            for i in range (6) :
                data = open(path_data[i] , 'r')
                for (j) in (data) :
                    row = csplit(cstrip(j) , ';')
                    content[i].append(row)
                data.close()
            user = content[0]
            monster = content[1]
            inv_item = content[2]
            inv_monster = content[3]
            shop_item = content[4]
            shop_monster = content[5]
            print("Selamat datang di program OWCA!")
            return (user , monster , inv_item , inv_monster , shop_item , shop_monster)
