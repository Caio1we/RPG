def attack(enemy, weapon, ammo=None) :
    enemy_health = enemy["health"]
    dealt_damage = weapon["damage"]
    dealt_critic_damage = weapon["damage_critic"]
    if ammo:
        if try_critic["chance_to_critic"]:
            return enemy_health - ammo["damage_critic"]
            return enemy_health - ammo["damage"]

    if try_critic(weapon["chance_to_critic"]):
        return dealt_critic_damage
    else:
        return dealt_damage



def try_critic(chance):
    if random.random() < chance:
        return True
    else:
        return False
 
