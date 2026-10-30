def menu():
    print("[1] - Jogar")
    print("[0] - Sair")


def select_weapon_menu(inventory):
    index = 1
    weapons_name = {}
    for i, weapon in enumerate(inventory, 1):
        print(f"[{index}] - {weapon}")
        weapons_name.update({index: weapon})
        index += 1
    weapon_choiced = int(input("Selecione a arma: "))
    weapon_choiced = inventory[weapons_name[weapon_choiced]]
    return weapon_choiced



def battle_menu():
    print("[1] - Atacar")
    print("[2] - Inspecionar")



