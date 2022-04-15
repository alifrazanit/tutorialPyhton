numbers = input("Masukan Angka: ")

numberMapping = {
    "1": "Satu",
    "2": "Dua",
    "3": "Tiga",
    "4": "Empat",
    "5": "Lima",
    "6": "Enam",
    "7": "Tujuh",
    "8": "Delapan",
    "9": "Sembilan",
    "0": "Nol"
}

output = ""

for n in numbers:
    terbilang  = numberMapping.get(n, "Invalid")
    output += terbilang + " "

print(output)
