from data.classes import CLASSES
from system.player import create_player, gain_xp
from system.enemy import create_enemy
from system.combat import battle
from ui.menu import menu
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
                gain_xp(player_data, actual_enemy["xp"])
            if player_data["health"] <= 0:
                print("Você morreu!")
                break

            
        case 2:
            print(player_data)
        case 0:
            break
