weight = input('Weight : ')
question = input('(L)bs or (K)g: ')
konversiBerat = 0
satuanBerat = ''

if question.lower() == 'l':
    konversiBerat = int(weight) * 0.45
    satuanBerat = 'Kilos'
elif question.lower() == 'k':
    konversiBerat = int(weight) / 0.45
    satuanBerat = 'Pounds'
else:
    print('Invalid Input')

konversiBerat = round(konversiBerat)

print(f"You Are {konversiBerat} {satuanBerat}")


