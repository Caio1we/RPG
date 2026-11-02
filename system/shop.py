import random
from data.items import SWORDS
from data.potions import POTIONS

RARITY_WEIGHTS = {
    "common": 60,
    "uncommon": 25,
    "rare": 10,
    "epic": 4,
    "legendary": 1
}

def get_random_item_by_classes(player_class):
    match player_class:
        case "warrior":
            available_items = list(SWORDS.values())
    weights = []

    for item in available_items:
        rarity = item["rarity"]
        weight = RARITY_WEIGHTS[rarity]
        weights.append(weight)

    selected_items = random.choices(available_items,weights=weights,k=1)[0]
    return selected_items
            
def get_avaiable_potions_per_class(player_class):
    available_potions = []
    match player_class:
        case "mage":
            available_potions = ["mana_potion", "health_potion"]
        case "warrior":
            available_potions = ["health_potion", "stamina_potion"]
    return available_potions


def buy_item(player_data, item):
    if player_data["money"] >= item["price"]:
        player_data["money"] -= item["price"]
        player_data["inventory"]["weapons"].update({item["name"]: item})
        print("Compra realizada com sucesso!")
    else:
        print("Você não tem ouro suficiente para comprar esse item.")

