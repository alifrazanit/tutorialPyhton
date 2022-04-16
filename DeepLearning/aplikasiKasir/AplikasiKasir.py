import json
applicationStart = True


def bacaData(fileName):
    userData = []
    f = open(f'./data/{fileName}.json')
    data = json.load(f)
    for i in data['data']:
        userData.append(i)
    f.close()
    return userData


def newLine():
    print("\n")


def Line():
    print("="*120)


def findUser(username, password):
    dataKaryawan = bacaData('karyawan')
    for karyawan in dataKaryawan:
        if karyawan["username"] == username and karyawan["password"] == password:
            return karyawan
        else:
            return False


def login():
    global userLogin
    start = True
    while start:
        Line()
        print("="*51, " SELAMAT DATANG ", "="*51)
        Line()
        username = input("Masukan Username: ")
        password = input("Masukan Password: ")
        userLogin = findUser(username, password)
        if userLogin == False:
            print("USERNAME ATAU PASSWORD SALAH!")
            reload = input(
                "Ingin masukan ulang username atau passowrd ? Y | N: ")
            if(reload.lower() == "y"):
                start = True
            else:
                start = False
                print("Terimakasih dan sampai jumpa")
        else:
            start = False


def fetchTable(data):
    print("KODE", "\t\t\t", "NAMA PRODUK", "\t\t\t",
          "JENIS PRODUK", "\t\t\t", "HARGA", "\t\t\t", "STOK")
    for d in data:
        print(f"{d['kode']}\t\t\t{d['namaProduk']}\t\t\t{d['jenisProduk']}\t\t\t{d['harga']}\t\t\t{d['stok']}")


def operasiKasir():
    Line()
    print(f"NIK\t\t: {userLogin['nik']}")
    print(f"Nama Kasir\t: {userLogin['name']}")
    print("List Produk: ")
    products = bacaData("produk")
    fetchTable(products)
    isRequest = input('Ada Pesanan: Y | N')
    keranjang = []

    while isRequest.lower() == 'y':
       barang = input('Masukan Kode Barang')
       qty = input('Jumlah')

    newLine()
    Line()

def operasiLogout():
    q = input("apakah Anda ingin logout? Y | N")
    if q.lower() == 'y':
        return True
    else:
        return False

while applicationStart:
    login()
    print("\n"*3)
    operasiKasir()
    isLogout = operasiLogout()
    if isLogout:
        applicationStart = False
    else:
        print("ini mode waterfall jadi engga bisa naik lagi, udah yo cabut")
        applicationStart = False