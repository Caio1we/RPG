def attack(enemy, weapon, currentEnergy, ammo=None,):
    if currentEnergy < weapon["spent_stamina"] or currentEnergy < weapon["spent_mana"]:
        return 0,0, False
    match weapon["type"]:
        case "sword":
            if try_critic(weapon["chance_to_critic"]):
                return enemy["health"] - weapon["damage_critic"], currentEnergy - weapon["spent_stamina"], True
            return enemy["health"] - weapon["damage"], currentEnergy - weapon["spent_stamina"]
        case "bow":
            if ammo == None:
                return 0,0 , False
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
 
