# import library dan define variabel style di global scope
import os
import sys
st = '\033[9m'
fn = '\033[0m'

# deklarasi barang dan diskon
barang = {1:{"Potabee Chips": 16_000}, 2:{"SilverQueen": 10_000}, 3:{"Pocky Strawberry": 8_500}, 4:{"Pocky Coklat": 8_500}, 5:{"Hello Panda": 9_500}, 6:{"Sukro": 10_000}, 7:{"TicTac": 13_000}, 8:{"Good Day": 7_500}, 9:{"Ichi Ocha": 3_500}, 10:{"Fruit Tea": 4_000}}
diskon_persen = {1:{"Potabee Chips": 10}, 2:{"Pocky Coklat": 25}}
diskon_get = {1:{"SilverQueen": (3, 1)}}
#diskon_persen = {}
#diskon_get = {}

# deklarasi list barang yang dibeli dan total belanja
list_barang = {}
total_belanja = 0

while True:
    # opening
    print(("_"*100).center(100))
    print(("Selamat Datang di MintChery").center(100))
    print(("Dimana Kita Buka Tergantung Mood").center(100))
    print(("="*100).center(100))

    # display diskon jika ada
    if len(diskon_persen.keys()) > 0 or len(diskon_get.keys()) > 0:
        print(("PROMO UNTUK HARI INI").center(100))

    # display diskon persen (bakal muncul kalo ada saja)
    for stuff_key in barang.keys():
        for stuff_name in barang[stuff_key].keys():
            for persen_key in diskon_persen.keys():
                for persen_name in diskon_persen[persen_key].keys():
                    if stuff_name.lower() == persen_name.lower():
                        print(f"\n||{stuff_name}\ndiskon {diskon_persen[persen_key][persen_name]}% dengan harga awal Rp {st}{barang[stuff_key][stuff_name]}{fn},- menjadi Rp {barang[stuff_key][stuff_name]-barang[stuff_key][stuff_name]*diskon_persen[persen_key][persen_name]/100},- saja!")

    # display diskon get (bakal muncul kalo ada saja)
    for stuff_key in barang.keys():
        for stuff_name in barang[stuff_key].keys():
            for get_key in diskon_get.keys():
                for get_name in diskon_get[get_key].keys():
                    if stuff_name.lower() == get_name.lower():
                        print(f"\n||{stuff_name}\nbuy {diskon_get[get_key][get_name][0]} get {diskon_get[get_key][get_name][1]}")

    # pembatas (biar pengguna tidak bingung) (cuman bakal tampil kalo ada diskon karena kalo selalu tampil pembatas malah jadi dobel)
    if len(diskon_persen.keys()) > 0 or len(diskon_get.keys()) > 0:
        print(("_"*100).center(100))

    # display barang (selalu muncul)
    for stuff_key in barang.keys():
        for stuff_name in barang[stuff_key].keys():
            print(f"{(" "*50)}\n{stuff_key}\t{stuff_name} | Rp {barang[stuff_key][stuff_name]},-")
    print("")
    # pembatas (biar pengguna tidak bingung)
    print(("_"*100).center(100))

    # total belanja (bakal muncul kalau di keranjang ada barangnya)
    if total_belanja > 0:
        print("rincian belanja:")
        print(f"nama barang\t| harga barang\t| qty\t| total\t|")
        for list_barang_key in list_barang.keys():
            print(f"{"".join(barang[list_barang_key].keys())}\t| Rp {next(iter(barang[list_barang_key].values()))},-\t| {list_barang[list_barang_key]}\t| Rp {next(iter(barang[list_barang_key].values()))*list_barang[list_barang_key]},-")
        print(f"Total belanja kamu: Rp {total_belanja},-")
        print(("-"*100).center(100))

        # konfirmasi pengguna
        konfirmasi = input("1. lanjut belanja\n2. kembalikan barang\n3. selesai belanja\ninput kamu: ")

        os.system('cls')

        # operasi sama (males nulis ulang, lupa kalo python gak punya goto soalnya hehe)
        if konfirmasi == '1':
            # opening
            print(("_"*100).center(100))
            print(("Selamat Datang di MintChery").center(100))
            print(("Dimana Kita Buka Tergantung Mood").center(100))
            print(("="*100).center(100))

            # display diskon jika ada
            if len(diskon_persen.keys()) > 0 or len(diskon_get.keys()) > 0:
                print(("PROMO UNTUK HARI INI").center(100))

            # display diskon persen (bakal muncul kalo ada saja)
            for stuff_key in barang.keys():
                for stuff_name in barang[stuff_key].keys():
                    for persen_key in diskon_persen.keys():
                        for persen_name in diskon_persen[persen_key].keys():
                            if stuff_name.lower() == persen_name.lower():
                                print(f"\n||{stuff_name}\ndiskon {diskon_persen[persen_key][persen_name]}% dengan harga awal Rp {st}{barang[stuff_key][stuff_name]}{fn},- menjadi Rp {barang[stuff_key][stuff_name]-barang[stuff_key][stuff_name]*diskon_persen[persen_key][persen_name]/100},- saja!")

            # display diskon get (bakal muncul kalo ada saja)
            for stuff_key in barang.keys():
                for stuff_name in barang[stuff_key].keys():
                    for get_key in diskon_get.keys():
                        for get_name in diskon_get[get_key].keys():
                            if stuff_name.lower() == get_name.lower():
                                print(f"\n||{stuff_name}\nbuy {diskon_get[get_key][get_name][0]} get {diskon_get[get_key][get_name][1]}")

            # pembatas (biar pengguna tidak bingung) (cuman bakal tampil kalo ada diskon karena kalo selalu tampil pembatas malah jadi dobel)
            if len(diskon_persen.keys()) > 0 or len(diskon_get.keys()) > 0:
                print(("_"*100).center(100))

            # display barang (selalu muncul)
            for stuff_key in barang.keys():
                for stuff_name in barang[stuff_key].keys():
                    print(f"{(" "*50)}\n{stuff_key}\t{stuff_name} | Rp {barang[stuff_key][stuff_name]},-")
            print("")

            # pembatas (biar pengguna tidak bingung)
            print(("_"*100).center(100))

            # input pengguna
            while True:
                pilihan_beli = input("Masukkan nomor barang yang akan dibeli:  ")
                if int(pilihan_beli) >= min(barang) and int(pilihan_beli) <= max(barang):
                    break
            jumlah_beli = input("Masukkan jumlah barang yang akan dibeli: ")

            # operasi total belanja
            for stuff_key in barang.keys():
                for stuff_name in barang[stuff_key].keys():
                    if int(stuff_key) == int(pilihan_beli):
                        total_belanja += int(barang[stuff_key][stuff_name])*int(jumlah_beli)

            # operasi banyaknya barang yang dibeli
            if int(pilihan_beli) in list_barang.keys():
                print(int(list_barang[int(pilihan_beli)]))
                list_barang[int(pilihan_beli)] = int(list_barang[int(pilihan_beli)])+int(jumlah_beli)
            else:
                list_barang[int(pilihan_beli)] = int(jumlah_beli)

            # hapus isi terminal biar tidak penuh
            os.system('cls')

        # operasi pengembalian barang
        if konfirmasi == '2':

            # membersihkan terminal
            os.system('cls')

            # list barang di keranjang
            print("pilih barang yang akan dikeluarkan")
            print("no\t| nama barang\t| qty")
            for list_barang_key in list_barang.keys():
                print(f"{list_barang_key}.\t| {"".join(barang[list_barang_key].keys())}\t| {list_barang[list_barang_key]}")
                print((" "*100).center(100))
            print(("-"*100).center(100))

            # input barang dan jumlah yang akan dikembalikan
            while True:
                back = input("masukkan nomor barang yang akan dikembalikan: ")
                if int(back) <= max(list_barang) and int(back) >= min(list_barang):
                    break
                else:
                    print("barang tidak ada di keranjang")
            while True:
                back_total = input("berapa jumlah yag dikembalikan: ")
                if int(back_total) > 0 and int(back_total) <= list_barang[int(back)]:
                    break
                else:
                    print("input jumlah barang salah")
            
            # operasi harga ketika ada barang yang dikembalikan
            total_belanja -= int(next(iter(barang[int(back)].values())))*int(back_total)

            # operasi jumlah barang yang dikembalikan
            list_barang[int(back)] -= int(back_total)
            if list_barang[int(back)] == 0:
                del list_barang[int(back)]

            # membersihkan terminal
            os.system('cls')
        
        # operasi belanja selesai dn operasi semua diskon yang didapat
        if konfirmasi == '3':
            # membersihkan terminal
            os.system('cls')

            # operasi diskon persen
            dk = 0
            for persen_key in diskon_persen.keys():
                for persen_name in diskon_persen[persen_key].keys():
                    for list_barang_key in list_barang.keys():
                        if "".join(barang[list_barang_key].keys()) == persen_name:
                            dk += diskon_persen[persen_key][persen_name]*next(iter(barang[list_barang_key].values()))/100*list_barang[list_barang_key]

            # menampilkan semua hasil belanja
            print(("-"*100).center(100))
            print("nama barang\t| harga   \t| qty\t| total")
            for list_barang_key in list_barang.keys():
                print(f"{"".join(barang[list_barang_key].keys())}\t| Rp {next(iter(barang[list_barang_key].values()))},-\t| {list_barang[list_barang_key]}\t| Rp {next(iter(barang[list_barang_key].values()))*list_barang[list_barang_key]}")
            print(("-"*100).center(100))

            # operasi diskon get dan menampilkan bonus diskon get
            for get_key in diskon_get.keys():
                for get_name in diskon_get[get_key].keys():
                    for list_barang_key in list_barang.keys():
                        if "".join(barang[list_barang_key].keys()) == get_name and int(list_barang[list_barang_key]/diskon_get[get_key][get_name][0]*diskon_get[get_key][get_name][1]) > 0:
                            print(f"bonus {get_name} sebanyak {int(list_barang[list_barang_key]/diskon_get[get_key][get_name][0]*diskon_get[get_key][get_name][1])} buah")

            # menampilkan semua total belanja dan diskon persen
            print(f"Total belanja:\tRp {total_belanja},-")
            if dk > 0:
                print(f"Total diskon:\tRp {dk},-")
                print(f"\t\tRp {total_belanja-dk}-")
            print(("-"*100).center(100))



            # ucapan terimakasih
            print(("Terimaksih Telah Memilih MintChery :>").center(100))
            print(("BAYAR YAA!!!").center(100))

            # paksa close program
            sys.exit()

    if total_belanja == 0:
        # opening
        print(("_"*100).center(100))
        print(("Selamat Datang di MintChery").center(100))
        print(("Dimana Kita Buka Tergantung Mood").center(100))
        print(("="*100).center(100))

        # display diskon jika ada
        if len(diskon_persen.keys()) > 0 or len(diskon_get.keys()) > 0:
            print(("PROMO UNTUK HARI INI").center(100))

        # display diskon persen (bakal muncul kalo ada saja)
        for stuff_key in barang.keys():
            for stuff_name in barang[stuff_key].keys():
                for persen_key in diskon_persen.keys():
                    for persen_name in diskon_persen[persen_key].keys():
                        if stuff_name.lower() == persen_name.lower():
                            print(f"\n||{stuff_name}\ndiskon {diskon_persen[persen_key][persen_name]}% dengan harga awal Rp {st}{barang[stuff_key][stuff_name]}{fn},- menjadi Rp {barang[stuff_key][stuff_name]-barang[stuff_key][stuff_name]*diskon_persen[persen_key][persen_name]/100},- saja!")

        # display diskon get (bakal muncul kalo ada saja)
        for stuff_key in barang.keys():
            for stuff_name in barang[stuff_key].keys():
                for get_key in diskon_get.keys():
                    for get_name in diskon_get[get_key].keys():
                        if stuff_name.lower() == get_name.lower():
                            print(f"\n||{stuff_name}\nbuy {diskon_get[get_key][get_name][0]} get {diskon_get[get_key][get_name][1]}")

        # pembatas (biar pengguna tidak bingung) (cuman bakal tampil kalo ada diskon karena kalo selalu tampil pembatas malah jadi dobel)
        if len(diskon_persen.keys()) > 0 or len(diskon_get.keys()) > 0:
            print(("_"*100).center(100))

        # display barang (selalu muncul)
        for stuff_key in barang.keys():
            for stuff_name in barang[stuff_key].keys():
                print(f"{(" "*50)}\n{stuff_key}\t{stuff_name} | Rp {barang[stuff_key][stuff_name]},-")
        print("")
        # pembatas (biar pengguna tidak bingung)
        print(("_"*100).center(100))

        # input pilihan dan jumlah barang yang akan dibeli
        while True:
            pilihan_beli = input("Masukkan nomor barang yang akan dibeli:  ")
            if int(pilihan_beli) >= min(barang) and int(pilihan_beli) <= max(barang):
                break
        jumlah_beli = input("Masukkan jumlah barang yang akan dibeli: ")

        # operasi total belanja
        for stuff_key in barang.keys():
            for stuff_name in barang[stuff_key].keys():
                if int(stuff_key) == int(pilihan_beli):
                    total_belanja += int(barang[stuff_key][stuff_name])*int(jumlah_beli)

        # operasi banyaknya barang yang dibeli
        if int(pilihan_beli) in list_barang.keys():
            print(int(list_barang[int(pilihan_beli)]))
            list_barang[int(pilihan_beli)] = int(list_barang[int(pilihan_beli)])+int(jumlah_beli)
        else:
            list_barang[int(pilihan_beli)] = int(jumlah_beli)

        # hapus isi terminal biar tidak penuh
        os.system('cls')
    
    # clear all
    os.system('cls')