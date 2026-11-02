import os
from data.potions import POTIONS
def menu():
    print("[1] - Jogar")
    print("[0] - Sair")


def select_weapon_menu(inventory):
    index = 1
    weapons_name = {}
    for i, weapon in enumerate(inventory.values(), 1):
        print(f"[{index}] - {weapon["name"]}")
        weapons_name.update({index: weapon})
        index += 1
    weapon_choiced = int(input("Selecione a arma: "))
    weapon_choiced = weapons_name[weapon_choiced]
    return weapon_choiced

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def battle_menu():
    print("[1] - Atacar")
    print("[2] - Inspecionar")
    print("[3] - potions")

def select_potion_menu(inventory):
    index = 1
    potions_name = {}
    print(inventory)
    for i, key in enumerate(inventory, 1):
        potion = inventory[key]
        print(f"[{index}] - {potion["name"]}")
        potions_name.update({index: key})
        index += 1
    potion_choiced = int(input("Selecione a poção: "))
    potion_choiced = potions_name[potion_choiced]
    atribute = POTIONS[potion_choiced]["atribute"]
    return potion_choiced, atribute
