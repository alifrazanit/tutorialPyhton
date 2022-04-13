year = input("Tahun lahir kamu: ")
tahunsekarang = input("sekarang tahun berapa? ")

year = int(year)
tahunsekarang = int(tahunsekarang)


umur = tahunsekarang - year
kalimat = "kamu sekarang berumur " + str(umur) + " Tahun"
print(kalimat)