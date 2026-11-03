import os
from data.potions import POTIONS
from data.items import SWORDS
from system.shop import get_avaiable_potions_per_class, get_random_item_by_classes, buy_item
def menu():
    print("[1] - Jogar")
    print("[2] - Ver status")
    print("[3] - Loja")
    print("[0] - Sair")


def select_weapon_menu(inventory):
    index = 1
    weapons_name = {}
    for i, weapon in enumerate(inventory.values(), 1):
        print(f"[{index}] - {weapon["name"]} - {weapon["damage"]} de dano - {weapon["cost"]} custo")
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

def shop_menu(player_data):
    if not player_data:
        print("Você precisa criar um personagem antes de acessar a loja.")
        return
    itens = []
    itens_names = {}
    for _ in range(2):
        item = get_random_item_by_classes(player_data["class"])
        itens.append(item)
    potions = get_avaiable_potions_per_class(player_data["class"])
    for potion in potions:
        itens.append(POTIONS[potion])
    for i, item in enumerate(itens, 1):
        print(f"[{i}] - {item["name"]} - Preço: {item["price"]}")
        itens_names.update({i: item["name"]})
    print("[0] - Sair da loja")
    choiced_item = int(input("Selecione o item que deseja comprar: "))
    if choiced_item == 0:
        return
    print(f"Você selecionou: {itens_names[choiced_item]}")
    buy_item(player_data, itens[choiced_item - 1])


def profile_menu(player_data, player_class):
    if not player_data:
        print("Você precisa criar um personagem antes de acessar o perfil.")
        return
    print(f"Nome: {player_data['name']}")
    print(f"Classe: {player_data['class']}")
    print(f"Nível: {player_data['level']}")
    print(f"Experiência: {player_data['xp']}")
    print(f"Vida Maxima: {player_data['max_health']}")
    print(f"Vida: {player_data['health']}")
    if player_class == "mage":
        print(f"Mana Maxima: {player_data['max_mana']}")
        print(f"Mana: {player_data['mana']}")
    else:
        print(f"Stamina Maxima: {player_data['max_stamina']}")
        print(f"Stamina: {player_data['stamina']}")
    print(f"Dinheiro: {player_data['money']}")
    print("Inventário:")
    print("Armas:")
    for item in player_data["inventory"]["weapons"].values():
        print(f"- {item['name']} - Dano: {item['damage']} - Custo: {item['cost']}")
    print("Poções:")
    for item in player_data["inventory"]["potions"].values():
        print(f" {item["name"]} - Atributo: {POTIONS[item["identifier"]]["atribute"]} - Restaura: {POTIONS[item["identifier"]]["restore_amount"]}, Quantidade: {item["quantity"]}")



