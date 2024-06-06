# PROGRAM K05-C-MainPY

# IDENTITAS
# Kelompok : K05-C
# NIM/Nama - 1 : 19623215 / Muhammad Raihan Nazhim Oktana
# NIM/Nama - 2 : 19623055 / Athian Nugraha Muarajuang
# NIM/Nama - 3 : 19623065 / Muhammad Alfansya
# NIM/Nama - 4 : 16523245 / Dede Firman
# NIM/Nama - 5 : 16523135 / Aleta Edna Jessalyn
# Instansi : Sekolah Teknik Elektro dan Informatika (STEI) Institut Teknologi Bandung (ITB)
# Nama File : main.py
# Topik : Tugas Besar Dasar Pemrograman 2024
# Tanggal : Senin, 20 Mei 2024
# Deskripsi : Main Program
# Penanggung Jawab - 1 : 19623065 / Muhammad Alfansya
# Penanggung Jawab - 2 : 19623215 / Muhammad Raihan Nazhim Oktana

# KAMUS UTAMA
# register , login , logout , help , menu , monster , potion , inventory , load , save , exit : procedure
# generate , battle , arena , shop , laboratory , manage_shop , monster_mng : function
# data_user , data_monster , data_invent_item , data_invent_monster , data_item_shop , data_shop_monster : matrix of data
# user_loggedin : array of string
# user_id , oc , start_time , end_time , duration : integer
# username , role , pilihan_aksi : string
# check_login , check_logres , admin , end : boolean
# i : integer (index)

# ALGORITMA
import os , time
from src.register import register
from src.login import login
from src.logout import logout
from src.help import help , menu
from src.inventory import inventory
from src.battle import battle
from src.arena import arena
from src.shop import shop
from src.manage_shop import manage_shop
from src.monster import monster
from src.potion import potion
from src.laboratory import laboratory
from src.manage_monster import monster_mng
from src.load import load
from src.save import save
from src.exit import exit
start_time = time.time()
data_user , data_monster , data_invent_item , data_invent_monster , data_item_shop , data_shop_monster = load()
if (data_user == 1) :
     end_time = time.time()
     duration = end_time - start_time
     print(f"Durasi Program\t: {int(duration // 3600)} Jam {int((duration % 3600) // 60)} Menit {int((duration % 60 // 1))} Detik")
     time.sleep(3)
     os.system('cls')
     exit
else :
     user_loggedin = ["" , "" , "" , "" , ""]
     user_id = user_loggedin[0]
     username = user_loggedin[1]
     role = user_loggedin[3]
     oc = user_loggedin[4]
     check_login = False
     admin = False
     end = False
     check_logres = False
     while (not(end)) :
          menu(check_login , username , admin)
          print("Masukkan pilihan aksi :")
          pilihan_aksi = input(">>> ").lower()
          if ((admin) and (pilihan_aksi != "register") and (pilihan_aksi != "login") and (pilihan_aksi != "help") and (pilihan_aksi != "logout") and (pilihan_aksi != "shop") and (pilihan_aksi != "monster") and (pilihan_aksi != "save") and (pilihan_aksi != "exit")) :
               print("Input tidak valid, harap pilih aksi yang tersedia!")
          elif ((not(admin)) and (pilihan_aksi != "register") and (pilihan_aksi != "login") and (pilihan_aksi != "help") and (pilihan_aksi != "logout") and (pilihan_aksi != "monster") and (pilihan_aksi != "potion") and (pilihan_aksi != "inventory") and (pilihan_aksi != "battle") and (pilihan_aksi != "arena") and (pilihan_aksi != "arena") and (pilihan_aksi != "laboratory") and (pilihan_aksi != "save") and (pilihan_aksi != "exit")) :
               print("Input tidak valid, harap pilih aksi yang tersedia!")
          else :
               if (pilihan_aksi == "help") :
                    help(check_login , username , admin)
               elif (pilihan_aksi == "register") :
                    (check_login , username , data_user , data_monster , data_invent_item , data_invent_monster) = register(check_login , username , data_user , data_monster , data_invent_item , data_invent_monster)
                    check_logres = True
               elif (pilihan_aksi == "login") :
                    check_login , username , admin , user_loggedin = login(data_user , check_login , username , admin , user_loggedin)
                    user_id = user_loggedin[0]
                    username = user_loggedin[1]
                    role = user_loggedin[3]
                    oc = user_loggedin[4]
                    check_logres = True
               elif (pilihan_aksi == "logout") :
                    check_login = logout(check_login)
               elif (pilihan_aksi == "exit") :
                    end = exit(check_logres , data_user , data_monster , data_invent_item , data_invent_monster , data_item_shop , data_shop_monster)
               elif ((pilihan_aksi == "monster") and (not(admin))) :
                    monster(data_monster)
               elif ((pilihan_aksi == "monster") and (admin)) :
                    data_monster = monster_mng(data_monster)
               elif (pilihan_aksi == "potion") :
                    potion()
               elif (pilihan_aksi == "inventory") :
                    inventory(username , data_invent_monster , data_user , data_monster , data_invent_item)
               elif (pilihan_aksi == "battle") :
                    user_id , username , role , oc , data_monster , data_invent_item , data_invent_monster = battle(user_id , username , role , oc , data_monster , data_invent_item , data_invent_monster)
                    user_loggedin[4] = oc
                    time.sleep(5)
               elif (pilihan_aksi == "arena") :
                    user_id , username , role , oc , data_monster , data_invent_item , data_invent_monster = arena(user_id , username , role , oc , data_monster , data_invent_item , data_invent_monster)
                    user_loggedin[4] = oc
                    time.sleep(5)
               elif ((pilihan_aksi == "shop") and (not(admin))) :
                    data_shop_monster , data_monster , data_item_shop , data_invent_item , user_loggedin , data_invent_monster = shop(data_shop_monster , data_monster , data_item_shop , data_invent_item , user_loggedin , data_invent_monster)
               elif ((pilihan_aksi == "shop") and (admin)) :
                    data_shop_monster , data_monster , data_item_shop = manage_shop(data_shop_monster , data_monster , data_item_shop) 
               elif (pilihan_aksi == "laboratory") :
                    data_invent_monster , oc = laboratory(data_monster , data_invent_monster , oc , user_id)
                    user_loggedin[4] = oc
               elif (pilihan_aksi == "save") :
                    end = save(data_user , data_monster , data_invent_item , data_invent_monster , data_item_shop , data_shop_monster)
               for i in range (len(data_user)) :
                    if (user_loggedin[0] == data_user[i][0]) :
                         data_user[i] = user_loggedin
          time.sleep(5)
          os.system('cls')
     end_time = time.time()
     duration = end_time - start_time
     print(f"Durasi Program\t: {int(duration // 3600)} Jam {int((duration % 3600) // 60)} Menit ('{int((duration % 60 // 1))} Detik")
     time.sleep(5)
     os.system('cls')
