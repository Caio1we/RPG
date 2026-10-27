from data.classes import CLASSES
from system.player import create_player
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

            
        case 2:
            print(player_data)
