from minstrul.statBudget import StatBudget
from minstrul.faction import Faction

class Minstrul:

    def __init__(self, nickname: str, faction: Faction, level: int, statBudget: StatBudget, statModifiers: list[float]):
        self.nickname = nickname
        self.faction = faction
        self.level = level
        
        self._statbudget = statBudget
        self._statModifiers = statModifiers
        
        self.health = self._calcHealth()
        self.attack = self._calcAttack()
        self.defence = self._calcDefence()
        self.speed = self._calcSpeed()

        self.currentHealth = self.health

    def takeDamage(self, damage: int):
        self.currentHealth = max(0, self.currentHealth - damage)

    def _calcStat(self, modifier: float) -> int:
        maxStat = (self._statbudget.value * modifier) 
        minStat = maxStat / 10
        return round((maxStat - minStat) / 100 * self.level + minStat)

    def _calcHealth(self) -> int:
        return self._calcStat(self._statModifiers[0])

    def _calcAttack(self) -> int:
        return self._calcStat(self._statModifiers[1])

    def _calcDefence(self) -> int:
        return self._calcStat(self._statModifiers[2])

    def _calcSpeed(self) -> int:
        return self._calcStat(self._statModifiers[3])

    def __str__(self) -> str:
        return (
            f"--- {self.nickname} (Lv. {self.level}) ---\n"
            f"Faction: {self.faction.value}\n"
            f"HP:      {self.currentHealth} / {self.health}\n"
            f"Attack:  {self.attack}\n"
            f"Defence: {self.defence}\n"
            f"Speed:   {self.speed}"
        )    