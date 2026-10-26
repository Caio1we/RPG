from re import match
import random


player_data = {}

classes = {
    "mage": {
        "name": "mage",
        "health": 75,
        "mana": 175,
        "description": "é um feiticeiro muito poderoso, uma lenda da magia que salvava pessoas e fazia missões para o reino, mas foi expulso por desobedecer ordens e vive afastado em uma cabana. Ele começa usando um cajado mágico de madeira.",
        "starter_weapons": {

            "wooden_staff":{
                "rarity": "common",
                "type": "staff",
                "damage": 5,
                "damage_critic": 10,
                "chance_to_critic": 0.10,
                "spent_mana": 0,
            },

            "thunder": {
                "rarity": "common",
                "type": "spell",
                "damage": 35,
                "damage_critic": 75,
                "spent_mana": 60,
                "chance_to_critic": 0.10
            }
        }
    },
    "archer": {
        "name": "archer",
        "health": 70,
        "stamina": 100,
        "description": "um soldado que se rebelou contra a nobreza e acabou sendo exilado do exercito e começou uma revolução onde ele trabalha roubandos dos nobres. Começa com seu antigo arco que ele usava no exercito e com suas flechas roubadas de quarteis da cidade.",
        "starter_weapons": {
            "wooden_bow": {
                "rarity": "common",
                "type": "bow",
                "spent_stamina": 10
            },

            "normal_arrow": {
                "rarity": "common",
                "type": "arrow",
                "damage": 15,
                "damage_critic": 30,
                "chance_to_critic": 0.10,
            }
        }
    },
    "warrior": {
        "name": "warrior",
        "health": 120,
        "stamina": 100,
        "description": "guardião de um antigo reino perdido e ainda pensa que está protegendo uma cidade. Ele é habilidoso com armas corpo a corpo, mas não tem habilidade com outros tipos de armas. Começa com uma espada longa e uma espada curta.",
        "starter_weapons": {
            "long_sword": {
                "rarity": "common",
                "type": "sword",
                "damage": 25,
                "stamina_spend": 50,
                "chance_to_critic": 0.10,
                "damage_critic": 50,
            },

        }
    }
}

# --- AS FUNÇÕES (AQUILO QUE FAZ ALGUMA COISA QUANDO É CHAMADO) ---

# Função do menu principal. Só serve para desenhar textinho na tela. Não pensa, só cospe texto.
def menu():
    print("[1] - Jogar")
    #print("[2] - Carregar Save") <-- Isso aqui tá desativado porque você ignorou, o Python finge que nem viu
    print("[0] - Sair")

# A fábrica de criar jogador. É aqui que o usuário dita quem ele vai ser.

def attack(enemy, weapon, currentEnergy, ammo=None,):

    if currentEnergy < weapon["spent_stamina"] or currentEnergy < weapon["spent_mana"]:
        return enemy["health"], currentEnergy, False
    match weapon["type"]:
        case "sword":
            if try_critic(weapon["chance_to_critic"]):
                return enemy["health"] - weapon["damage_critic"], currentEnergy - weapon["spent_stamina"], True
            return enemy["health"] - weapon["damage"], currentEnergy - weapon["spent_stamina"]
        case "bow":
            if ammo == None:
                return enemy["health"], currentEnergy , False
            if  try_critic(ammo["chance_to_critic"]):
                return enemy["health"] - ammo["damage_critic"], currentEnergy - weapon["spent_stamina"], True
            return enemy["health"] - ammo["damage"], currentEnergy - weapon["spent_stamina"], True
        case "spell":
            if try_critic(weapon["chance_to_critic"]):
                return enemy["health"] - weapon["damage_critic"], currentEnergy - weapon["spent_mana"], True
            return enemy["health"] - weapon["damage"], currentEnergy - weapon["spent_mana"]
        case "staff":
            if try_critic(weapon["chance_to_critic"]):
                return enemy["health"] - weapon["damage_critic"], 0, True
            return enemy["health"] - weapon["damage"], 0, True


def try_critic(chance):
    if random.random() < chance:
        return True
    else:
        return False
 

def create_player():

    global player_data # Avisa o Python que vamos mexer naquela caixa vazia 'player_data' que está lá fora da função.

    name = input("Type your name: ")     # Pergunta o nome do cidadão e guarda na variável 'name'  

    name_classes = {}    # Outra caixa vazia. Vai servir para numerar as classes (ex: 0 é Mago, 1 é Arqueiro...)

    print("Available classes: ")
    for i, classe in enumerate(classes):  # O loop 'for' vai ler o catálogo de classes e o 'enumerate' vai dando números para elas (0, 1, 2...)
        print(f"[{i}] - {classe}") # Mostra na tela o número e o nome da classe
        name_classes.update({i: classe}) # Guarda na nossa caixinha: {0: "mage", 1: "archer"...}

    while True:     # Loop infinito! Fica rodando até o cara parar de ser burro e escolher uma classe que existe.
        chice = int(input("Select one class available: "))  # Pede um número pro usuário. O int() transforma em numero
        # esse numero vai ser usado pra procurar dentro da caixa name_classes


        if chice not in name_classes: # Se o número que o cara digitou NÃO estiver nas chaves da nossa caixinha (0, 1 ou 2)...
            print("Class not found, try again")
            continue
        
        print(f"Description: {classes[name_classes[chice]]["description"]}") 
        # O usuário digita 1, então: chice = 1
        # O Python lê de dentro para fora:

        # 1. Troca 'chice' pelo valor:    name_classes[1]
        # 2. Busca na tabela de nomes:   name_classes[1] vira "archer"
        # 3. Substitui no código:        classes["archer"]["description"]
        # 4. Busca no catálogo final:    Retorna o texto "um soldado que se rebelou..."

         # Em suma: Número (1) -> vira Nome ("archer") -> vira a Descrição final.
        print(f"Your choice has been {classes[name_classes[chice]]["name"]}, do you have sure?")   # Pergunta se o cara tem certeza absoluta


        # Pergunta se o cara tem certeza absoluta
        choice = input("Y/N : ").upper() # Pede Y (Sim) ou N (Não). O '.upper()' transforma letras minúsculas em MAIÚSCULAS.

        if choice == "Y":        # Se ele digitou Y (Sim)...
            class_choiced = name_classes[chice] # Salva o nome da classe escolhida (ex: "mage")
            print(class_choiced)
            print(f"Class chosen = {class_choiced}")
            if "mana" in classes[class_choiced]: # Se a classe escolhida usa MANA (tipo o Mago)...
                # Enche a ficha do jogador com os status de mago
                player_data = {
                    "name": name,
                    "class": classes[class_choiced]["name"],
                    "level": 0, "xp": 0, "money": 0,
                    "health": classes[class_choiced]["health"],
                    "mana": classes[class_choiced]["mana"], 
                    "inventory": classes[class_choiced]["starter_weapons"] }
                
            if "stamina" in classes[class_choiced]: # Mas se a classe usa STAMINA (tipo o Guerreiro ou Arqueiro)...
                # Enche a ficha do jogador com os status de stamina
                player_data = {
                    "name": name,
                    "class": classes[class_choiced]["name"],
                    "level": 0, "xp": 0, "money": 0,
                    "health": classes[class_choiced]["health"],
                    "stamina": classes[class_choiced]["stamina"],
  
                    "inventory": classes[class_choiced]["starter_weapons"] }
            break # Quebra o loop infinito do "While True" porque o jogador foi criado com sucesso!


    return name, classe



while True:

    menu()

    option = int(input("Type your choice: "))
    # O 'match' analisa o número que o cara digitou (igual um monte de IF/ELSE, só que mais bonito)
    match option:
        case 1:
            if not player_data:# Se a caixinha player_data estiver VAZIA (ou seja, não tem jogador criado)...
                create_player() # Chama a função de criar o jogador!

            
        case 2:
            print(player_data)
