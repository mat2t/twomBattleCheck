from minstrul.statBudget import StatBudget

class Minstrul:

    def __init__(self, nickname: str, level: int, statBudget: StatBudget, statModifiers: list[float]):
        self.nickname = nickname
        self.level = level
        
        self._statbudget = statBudget
        self._statModifiers = statModifiers
        
        self.health = self._calcHealth()
        self.attack = self._calcAttack()
        self.defence = self._calcDefence()
        self.speed = self._calcSpeed()

        self.currentHealth = self.health

    def takeDamage(self, damage: int):
        self.currentHealth -= damage

    def _calcHealth(self) -> int:
        return int(self._statbudget.value * self._statModifiers[0])
        
    def _calcAttack(self) -> int:
        return int(self._statbudget.value * self._statModifiers[1])

    def _calcDefence(self) -> int:
        return int(self._statbudget.value * self._statModifiers[2])

    def _calcSpeed(self) -> int:
        return int(self._statbudget.value * self._statModifiers[3])

    def __str__(self) -> str:
        return (
            f"--- {self.nickname} (Lv. {self.level}) ---\n"
            f"HP:      {self.currentHealth} / {self.health}\n"
            f"Attack:  {self.attack}\n"
            f"Defence: {self.defence}\n"
            f"Speed:   {self.speed}"
        )    