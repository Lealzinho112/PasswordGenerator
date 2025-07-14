import random

#Basic User Interface#
file = input("what file you want to encrypt")

##TXT to Bin##
f = open ("%s" % file)
originalTXT = f.read()
binchrs = []

for z in originalTXT:
    binchrs.append(ord(z)+1)

##Generate Key##
keyChrcs = []
chrcsToUse =["#","!","?","|","~","/","a","e","i","o","u","z","H","K","P","L","M","O"]
p=0
while p < 64:
    num=random.randint(0,17)
    keyChrcs.append(chrcsToUse[num])
    p=p+1
        
key = "".join(map(str,keyChrcs))

##Reads Key##
numadd=0
for z in keyChrcs:
    if (z == "#"):
        numadd = numadd + 7
    if (z == "!"):
        numadd = numadd*8
    if (z == "?"):
        numadd = numadd*9
    if (z == "|"):
        numadd = numadd*10
    if (z == "~"):
        numadd = numadd*11
    if (z == "/"):
        numadd = numadd*12
    if (z == "a"):
        numadd = numadd +50
    if (z == "e"):
        numadd = numadd +70
    if (z == "o"):
        numadd = numadd +90
    if (z == "i"):
        numadd = numadd + 110
    if (z == "u"):
        numadd = numadd +130
    if (z == "z"):
        numadd = numadd +150
    if (z == "H"):
        numadd = numadd -20
    if (z == "K"):
        numadd = numadd -40
    if (z == "P"):
        numadd = numadd -60
    if (z == "L"):
        numadd = numadd +20
    if (z == "M"):
        numadd = numadd +40
    if (z == "O"):
        numadd = numadd +60

##Change Ascii##
chngbin = []
for z in binchrs:
    chngbin.append(z+numadd)

##Transform into txt##
file = open( "encrypt.txt", "w")
file.write(" ".join(map(str,chngbin)))

