from minstrul import Minstrul, CreateMinstrul, StatBudget
from minstrul.archetypes import Archetype


def calcDamage(movePwr: int, attacker: Minstrul, defender: Minstrul, hasStab: bool) -> int:
    # TODO add effective multiplier e.g. super, neutral, resist (1.25, 1, 0.75)
    stab = 1.25 if hasStab else 1

    return int(movePwr * (attacker.attack / defender.defence) * (attacker.level / 50 + 1) * stab)

hippo = CreateMinstrul("Mini Hippo Bro", 10, Archetype.TANK, StatBudget.STAGE1)
cat = CreateMinstrul("Tigo", 10, Archetype.SPEEDSTER, StatBudget.STAGE1)


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
