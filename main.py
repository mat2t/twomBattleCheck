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

print(hippo.nickname + " Used Splash!\n")
cat.takeDamage(calcDamage(20, hippo, cat, False))

print(cat.nickname + " Used Claw!\n")
hippo.takeDamage(calcDamage(20, cat, hippo, False))

print("\nBATTLE OVER")
print(f"{hippo.nickname} has {hippo.currentHealth} hp remaining\n")
print(f"{cat.nickname} has {cat.currentHealth} hp remaining")
