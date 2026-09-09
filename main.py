from minstrul import Minstrul, CreateMinstrul, StatBudget, Faction, FACTION_EFFECTIVENESS
from minstrul.archetypes import Archetype


def calcDamage(movePwr: int, attacker: Minstrul, defender: Minstrul, hasStab: bool) -> int:
    stab = 1.25 if hasStab else 1
    effectiveness = getEffectiveness(attacker, defender.faction)

    return int(movePwr * (attacker.attack / defender.defence)
               * (attacker.level / 50 + 1) 
               * stab 
               * effectiveness)

def getEffectiveness(attacker: Minstrul, defender: Minstrul) -> float:
    return FACTION_EFFECTIVENESS.get(attacker.faction, {}).get(defender.faction, 1.0)


hippo = CreateMinstrul("Chungus", Faction.AQUATIC, 10, Archetype.TANK, StatBudget.STAGE1)
cat = CreateMinstrul("Tigo", Faction.UNDEAD, 10, Archetype.SPEEDSTER, StatBudget.STAGE1)

print(hippo)
print("\nVS\n")
print (cat)
print("\n-----------------\n")

print(f"{hippo.nickname} Used Splash")
hippoDmg = calcDamage(20, hippo, cat, True)
print(f"It does {hippoDmg} damage!\n")
cat.takeDamage(hippoDmg)

print(f"{cat.nickname} Used Claw")
catDmg = calcDamage(20, cat, hippo, False)
print(f"It does {catDmg} damage!\n")
hippo.takeDamage(catDmg)

print("\nBATTLE OVER")
print(f"{hippo.nickname} has {hippo.currentHealth} hp remaining\n")
print(f"{cat.nickname} has {cat.currentHealth} hp remaining")
