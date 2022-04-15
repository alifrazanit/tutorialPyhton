try:
    level = input('masukan level kamu: ')
    level = int(level)
    print(level)
except ZeroDivisionError:
    print('error tidak bisa dibagi nol')
except ValueError:
    print("yang kamu masukan bukan angka")



try:
    nama = input('name')
    print(nama)
except:
    print('error general')