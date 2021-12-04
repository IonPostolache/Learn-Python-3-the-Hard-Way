judete={'Vaslui':'VS', 'Galati':'GL', 'Vrancea' :'VN'}

print(f"Abbrev for Vaslui is: ", judete['Vaslui'])

orase={'VS': 'Barlad', 'GL': 'Tecuci', 'VN': 'Focsani'}

print(f"principalul  oras din Vaslui este:", orase[judete['Vaslui']])

#for judete, prescurtare in list(judete.items()):
#    print(f"{prescurtare} reprezinta judetul {judete}")


for key, value in judete.items():
    print(key, value)
