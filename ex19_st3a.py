
def recolta_gradina(ceapa, usturoi, cartofi="pai"):
    print(f"So you'll make {ceapa} RON from ceapa,\
    {usturoi} RON from usturoi and {cartofi} RON from cartofi.")

# 1
recolta_gradina(30, 20, 10)

# 2
recolta_gradina("prajita", 20, 30)

# 3
recolta_gradina("prajita", 20+2, 30)

# 4
ceapa_quantity=20
usturoi_quantity=40
recolta_gradina(ceapa_quantity+20, usturoi_quantity+2, 20)

# 5
recolta_gradina(20, 30)

# 6
recolta_gradina(20, 30, 20)

# 7
def recolta_gradina(*legume):
    print(f"So you'll make {leguma1} RON from ceapa,\
     {leguma2} RON from usturoi and\
      {leguma3} RON from cartofi.")

leguma1=20
leguma2=30
leguma3=50
leguma4=40
leguma5=70

recolta_gradina(leguma1, leguma2, leguma3, leguma4, leguma5)

# 8
def recolta_gradina(*legume):
    print(f"So you'll make {leguma1} RON from ceapa,\
     {leguma2} RON from usturoi and\
      {leguma3} RON from cartofi.")

leguma1=20
leguma2=30
leguma3=50
leguma4=40
leguma5=70

recolta_gradina(leguma1, leguma2, leguma3, leguma4, leguma5, 30)


# 9
def recolta_gradina(*legume):
    leguma1, leguma2, leguma3, leguma4=legume
    print(f"So you'll make {leguma1} RON from ceapa,\
    {leguma2} RON from usturoi and\
    {leguma3} RON from cartofi.")



recolta_gradina("20", "30", 40, 35)

# 10
def recolta_gradina(*legume):
    print("legumele: ", legume)

recolta_gradina(20, 30, 55, 54, 87, 564)
