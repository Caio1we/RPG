import random
from ui.menu import battle_menu, select_weapon_menu, clear

def attack(enemy, weapon, ammo=None) :
    enemy_health = enemy["health"]
    dealt_damage = weapon["damage"]
    dealt_critic_damage = weapon["damage_critic"]
    if ammo:
        if try_critic["chance_to_critic"]:
            return enemy_health - ammo["damage_critic"], True
        else:
            return enemy_health - ammo["damage"], False

    if try_critic(weapon["chance_to_critic"]):
        return dealt_critic_damage, True
    else:
        return dealt_damage, False



def try_critic(chance):
    if random.random() < chance:
        return True
    else:
        return False

def battle(enemy, player):
    player_turn = True
    while enemy["health"] > 0:
        clear()
        if player_turn:
            print(f"{enemy["name"]} - {enemy["health"]} HP")
            if player["class"] == "mage":
                print(f"{player["name"]} - {player["health"]} HP - {player["mana"]} mana")
            else:
                print(f"{player["name"]} - {player["health"]} HP {player["stamina"]} stamina")
            battle_menu()
            action_choiced = int(input("Digite a ação acima: "))
            match action_choiced:
                case 1:
                    weapon_choiced = select_weapon_menu(player["inventory"])
                    if player["class"] == "mage":
                        if player["mana"] < weapon_choiced["cost"]:
                            print("NÃO CONSEGUE USAR ATAQUE, MANA INSUFICIENTE")
                            input("Pressione ENTER para continuar...")
                            continue
                    else:
                        if player["stamina"] < weapon_choiced["cost"]:
                            print("NÃO CONSEGUE USAR ATAQUE, STAMINA INSUFICIENTE")
                            input("Pressione ENTER para continuar...")
                            continue
                    damage, critic = attack(enemy, weapon_choiced)
                    if critic:
                        print(f"CRITICO! Você deu {damage}")
                        input("Pressione ENTER para continuar...")
                    else: 
                        print(f"Você deu {damage} de dano")
                        input("Pressione ENTER para continuar...")
                    enemy["health"] -= damage
                    if player["class"] == "mage":
                        player["mana"] -= weapon_choiced["cost"]
                    else:
                        player["stamina"] -= weapon_choiced["cost"]
                    player_turn = False
                    continue
                case 2:
                    print(enemy["description"])
        player["health"] -= enemy["damage"]
        print(f"Você recebeu {enemy["damage"]} de dano")
        input("Pressione ENTER para continuar...")
        player_turn = True
        if player["health"] <= 0:
            return False
    print("Inimigo derrotado!")
    return True
        







 
