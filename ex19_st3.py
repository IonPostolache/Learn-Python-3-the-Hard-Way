def recolta_gradina(ceapa, usturoi, cartofi):
    print(f"So you'll make {ceapa} RON from ceapa, {usturoi} RON from usturoi and {cartofi} RON from cartofi.")

"""
recolta_gradina(3, 5, 12)
"""

kg_ceapa=input("How many kg of ceapa do you have?: ")
kg_usturoi=input("How many kg of usturoi do you have?: ")
kg_cartofi=input("How many kg of cartofi do you have?: ")

print(f"You have {kg_ceapa} kg ceapa, {kg_usturoi} kg usturoi and {kg_cartofi} kg cartofi.")

pret_kg_ceapa=input("How much is the price for 1kg of ceapa?: ")
pret_kg_usturoi=input("How much is the price for 1kg of usturoi?: ")
pret_kg_cartofi=input("How much is the price for 1kg of cartofi?: ")

print(f"The price is {pret_kg_ceapa} RON for 1kg of ceapa, {pret_kg_usturoi} RON for 1kg of usturoi and {pret_kg_cartofi} RON for 1kg of usturoi.")

money_ceapa=float(kg_ceapa)*float(pret_kg_ceapa)
money_usturoi=float(kg_usturoi)*float(pret_kg_usturoi)
money_cartofi=float(kg_cartofi)*float(pret_kg_cartofi)

total_money=float(money_ceapa)+float(money_usturoi)+float(money_cartofi)

recolta_gradina(money_ceapa, money_usturoi, money_cartofi)

print(f"In total you'll make {total_money} RON selling these vegetables.")
