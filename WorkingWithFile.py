# mode r = read
# a = append (menambahkan)
# r+ = baca dan nulis 
# w = write
userfile = open('C:/alif_repo/tutorial/pyton/tutorialPyhton/user.txt', 'r')
# userfile.read()
print(userfile.readable())
print(userfile.readline())

lines = userfile.readlines()
print(lines)

userfile.close()