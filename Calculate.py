import numbers


command = ""

while command != "stop":
    command = input("masukan perintah : ")

    if command != "*" and command != "+" and command != "-" and command != "/":
        print("Perintah tidak dikenali !")
        continue

    x = input("masukan nilai x : ")
    y = input("masukan nilai y : ")

    if x.isnumeric() == False or y.isnumeric() == False:
        print("MASUKAN NILAI INT")
        continue

    print(x.isnumeric)
    print(y.isnumeric)

    hasil = 0

    if command == "+":
        hasil = x + y
    elif command == "-":
        hasil = x - y
    elif command == "*":
        hasil = x * y
    elif command == "/":
        hasil = x / y
    
    print(f"Hasil : {hasil}")