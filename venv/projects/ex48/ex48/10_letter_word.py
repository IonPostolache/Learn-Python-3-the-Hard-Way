indice = "qedhjwzafp"
lettre = "xWl_]k~[k|"
i = 0
titi = ''
while i < len(indice):
    if ord(indice[i]) < 109:
        titi = titi + chr(ord(lettre[i]) + 10)
    else:
        titi = titi + chr(ord(lettre[i]) - 10)
