CLASSES = {
    "mage": {
        "name": "mage",
        "max_health": 75,
        "health": 75,
        "max_mana": 175,
        "mana": 175,
        "description": "é um feiticeiro muito poderoso, uma lenda da magia que salvava pessoas e fazia missões para o reino, mas foi expulso por desobedecer ordens e vive afastado em uma cabana. Ele começa usando um cajado mágico de madeira.",
        "starter_weapons": {

            "wooden_staff":{
                "identifier": "wooden_staff",
                "name": "Cajado de madeira",
                "rarity": "common",
                "type": "staff",
                "damage": 5,
                "damage_critic": 10,
                "cost": 0,
                "chance_to_critic": 0.10,
            },

            "thunder": {
                "identifier": "thunder",
                "name": "Feitiço de trovão",
                "rarity": "common",
                "type": "spell",
                "damage": 35,
                "damage_critic": 75,
                "cost": 60,
                "chance_to_critic": 0.10
            }
        }
    },
    "warrior": {
        "name": "warrior",
        "max_health": 120,
        "health": 120,
        "max_stamina": 100,
        "stamina": 100,
        "description": "guardião de um antigo reino perdido e ainda pensa que está protegendo uma cidade. Ele é habilidoso com armas corpo a corpo, mas não tem habilidade com outros tipos de armas. Começa com uma espada longa e uma espada curta.",
        "starter_weapons": {
            "long_sword": {
                "identifier": "long_sword",
                "name": "Espada Longa",
                "rarity": "common",
                "type": "sword",
                "damage": 25,
                "cost": 50,
                "chance_to_critic": 0.10,
                "damage_critic": 50,
            },

        }
    }
}
