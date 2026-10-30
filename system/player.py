from data.classes import CLASSES



def create_player():

    name = input("Type your name: ")     # Pergunta o nome do cidadão e guarda na variável 'name'  

    name_classes = {}    # Outra caixa vazia. Vai servir para numerar as classes (ex: 0 é Mago, 1 é Arqueiro...)

    print("Available classes: ")
    for i, classe in enumerate(CLASSES, 1):  # O loop 'for' vai ler o catálogo de classes e o 'enumerate' vai dando números para elas (0, 1, 2...)
        print(f"[{i}] - {classe}") # Mostra na tela o número e o nome da classe
        name_classes.update({i: classe}) # Guarda na nossa caixinha: {0: "mage", 1: "archer"...}

    while True:     # Loop infinito! Fica rodando até o cara parar de ser burro e escolher uma classe que existe.
        chice = int(input("Select one class available: "))  # Pede um número pro usuário. O int() transforma em numero
        # esse numero vai ser usado pra procurar dentro da caixa name_classes


        if chice not in name_classes: # Se o número que o cara digitou NÃO estiver nas chaves da nossa caixinha (0, 1 ou 2)...
            print("Class not found, try again")
            continue
        
        print(f"Description: {CLASSES[name_classes[chice]]["description"]}") 
        # O usuário digita 1, então: chice = 1
        # O Python lê de dentro para fora:

        # 1. Troca 'chice' pelo valor:    name_classes[1]
        # 2. Busca na tabela de nomes:   name_classes[1] vira "archer"
        # 3. Substitui no código:        classes["archer"]["description"]
        # 4. Busca no catálogo final:    Retorna o texto "um soldado que se rebelou..."

         # Em suma: Número (1) -> vira Nome ("archer") -> vira a Descrição final.
        print(f"Your choice has been {CLASSES[name_classes[chice]]["name"]}, do you have sure?")   # Pergunta se o cara tem certeza absoluta


        # Pergunta se o cara tem certeza absoluta
        choice = input("Y/N : ").upper() # Pede Y (Sim) ou N (Não). O '.upper()' transforma letras minúsculas em MAIÚSCULAS.

        if choice == "Y":        # Se ele digitou Y (Sim)...
            class_choiced = name_classes[chice] # Salva o nome da classe escolhida (ex: "mage")
            print(class_choiced)
            print(f"Class chosen = {class_choiced}")
            if "mana" in CLASSES[class_choiced]: # Se a classe escolhida usa MANA (tipo o Mago)...
                # Enche a ficha do jogador com os status de mago
                player_data = {
                    "name": name,
                    "class": CLASSES[class_choiced]["name"],
                    "level": 0, "xp": 0, "money": 0,
                    "stage_level": 1,
                    "health": CLASSES[class_choiced]["health"],
                    "mana": CLASSES[class_choiced]["mana"], 
                    "inventory": CLASSES[class_choiced]["starter_weapons"] }
                
            if "stamina" in CLASSES[class_choiced]: # Mas se a classe usa STAMINA (tipo o Guerreiro ou Arqueiro)...
                if CLASSES[class_choiced] == "archer":
                    player_data = {
                        "name": name,
                        "class": CLASSES[class_choiced]["name"],
                        "level": 0, "xp": 0, "money": 0,
                        "stage_level": 1,
                        "health": CLASSES[class_choiced]["health"],
                        "stamina": CLASSES[class_choiced]["stamina"],
                        "inventory": CLASSES[class_choiced]["starter_weapons"],
                        "arrows: CLASSES[class_choiced]["starter_arrows"],
                    }
                # Enche a ficha do jogador com os status de stamina
                player_data = {
                    "name": name,
                    "class": CLASSES[class_choiced]["name"],
                    "level": 0, "xp": 0, "money": 0,
                    "stage_level": 1,
                    "health": CLASSES[class_choiced]["health"],
                    "stamina": CLASSES[class_choiced]["stamina"],
                    "inventory": CLASSES[class_choiced]["starter_weapons"] }
            break # Quebra o loop infinito do "While True" porque o jogador foi criado com sucesso!


    return player_data


