import random
from data.enemies import ENEMIES
from copy import deepcopy

def create_enemy(stage_level):
    enemy_name = random.choice(list(ENEMIES.keys()))

    enemy = deepcopy(ENEMIES[enemy_name])

    health_multiplier = 1 + 0.12 * (stage_level - 1)

    enemy["health"] = round(
        enemy["health"] * health_multiplier
    )

    return enemy
