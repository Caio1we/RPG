from data.classes import CLASSES
from system.player import create_player
from system.enemy import create_enemy
from system.combat import battle
from ui.menu import menu, shop_menu, profile_menu

player_data = {}

while True:

    menu()

    option = int(input("Type your choice: "))
    # O 'match' analisa o número que o cara digitou (igual um monte de IF/ELSE, só que mais bonito)
    match option:
        case 1:
            if not player_data:# Se a caixinha player_data estiver VAZIA (ou seja, não tem jogador criado)...
                player_data = create_player() # Chama a função de criar o jogador!
                continue
            while player_data["health"] > 0:
                if player_data["stage_level"] != 1:
                    continuar = input("Deseja continuar para a próxima fase? Y/N: ").upper()
                    if continuar == "N":
                        break
                actual_enemy = create_enemy(player_data["stage_level"])
                print(f"{actual_enemy["name"]} apareceu! Lute com ele")
                battle(actual_enemy, player_data)
                player_data["stage_level"] += 1
            if player_data["health"] <= 0:
                print("Você morreu!")
                break

            
        case 2:
            if not player_data:
                print("Você precisa criar um personagem antes de acessar o perfil.")
                continue
            profile_menu(player_data, player_data["class"])
        case 3:
            shop_menu(player_data)
        case 0:
            break
