CLASSES = {
    "mage": {
        "name": "mage",
        "health": 75,
        "mana": 175,
        "description": "é um feiticeiro muito poderoso, uma lenda da magia que salvava pessoas e fazia missões para o reino, mas foi expulso por desobedecer ordens e vive afastado em uma cabana. Ele começa usando um cajado mágico de madeira.",
        "starter_weapons": {

            "wooden_staff":{
                "rarity": "common",
                "type": "staff",
                "damage": 5
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
