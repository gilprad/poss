import csv

DATABASE = 'contoh.csv'
data_csv_harga = []


def submenu():
    pilihan = input("1.List data\t 2.Input data\t 3.Kembali ke menu utama\nInput: ")
    if pilihan == "1":
        print("%2s \t %10s \t %10s " % ("ID", "NAMA", "HARGA"))
        listBarang()
    elif pilihan == "2":
        print("%2s \t %10s \t %10s " % ("ID", "NAMA", "HARGA"))
        file1 = open(DATABASE, 'r')
        first_number = sum(1 for data in file1)
        while True:
            first_number += 1
            print(first_number)
            idBarang = first_number
            namaBarang = input("Nama Barang: ")
            if namaBarang == '.':
                break
            hargaBarang = input("Harga Barang: ")
            inputBarang(idBarang, namaBarang, hargaBarang)
            print("Data berhasil ditambahkan")
        menu()
    else:
        menu()


def inputBarang(idBarang, namaBarang, hargaBarang):
    file2 = open(DATABASE, 'a')
    write = csv.writer(file2, delimiter=";")
    data = [idBarang, namaBarang, hargaBarang]
    print(data)
    write.writerow(data)


def listBarang():
    file1 = open(DATABASE, 'r')
    read = csv.reader(file1, delimiter=";")
    for data in read:
        # print("%2s \t %12s \t %11s " % (data[0], data[1], data[2]))
        data_csv_harga.append([data[0], data[1], data[2]])
    for i in range(len(data_csv_harga)):
        data_csv_harga[i][2] = int(data_csv_harga[i][2])

    data = data_csv_harga.copy()
    print(data)
    max = len(data_csv_harga)

    for x in range(max-1, 0, -1):
        for y in range(x):
            if data[y][2] < data[y+1][2]:
                data[y][0], data[y+1][0] = data[y+1][0], data[y][0]
                data[y][1], data[y+1][1] = data[y+1][1], data[y][1]
                data[y][2], data[y+1][2] = data[y+1][2], data[y][2]
    print(data)
    file1.close()
    menu()


def menu():
    pilihan = input("1.Data barang\t 2.Pencarian Barang\t \t 3.Penjualan\t 4.Stok\t \t 5.Keluar\nInput: ")
    if pilihan == "1":
        submenu()
    elif pilihan == "2":
        submenu()
    elif pilihan == "3":
        submenu()
    elif pilihan == "4":
        submenu()
    else:
        exit()


menu()
