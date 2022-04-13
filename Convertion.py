year = input("Tahun lahir kamu: ")
tahunsekarang = input("sekarang tahun berapa? ")

year = int(year)
tahunsekarang = int(tahunsekarang)


umur = tahunsekarang - year
kalimat = f"kamu sekarang berumur {umur} Tahun"
# kalimat = f"kamu sekarang berumur " + str(umur) + " Tahun"
print(kalimat)